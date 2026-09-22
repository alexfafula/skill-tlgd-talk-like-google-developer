from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


RENDERER_PATH = Path(__file__).resolve().parents[1] / "render_html.py"
SPEC = importlib.util.spec_from_file_location("tlgd_html_renderer", RENDERER_PATH)
assert SPEC is not None and SPEC.loader is not None
renderer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(renderer)


class HtmlReportTests(unittest.TestCase):
    def write_json(self, path: Path, value: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def make_run(self, root: Path) -> Path:
        run_root = root / "example-run"
        manifest = {
            "id": "example",
            "repository": {"url": "https://example.invalid/repo", "commit": "a" * 40},
            "conditions": {
                "control": {"prompt_suffix": ""},
                "tlgd": {"prompt_suffix": "\n\nUse TLGD."},
            },
            "cases": [
                {
                    "id": "case-one",
                    "mode": "answer",
                    "difficulty": "simple",
                    "prompt": "Explain the path.",
                    "review_criteria": ["Stay grounded."],
                }
            ],
        }
        environment = {"run_id": "example-run", "seed": 42}
        self.write_json(run_root / "manifest.json", manifest)
        self.write_json(run_root / "environment.json", environment)
        common = {
            "agent": "example-agent",
            "case_id": "case-one",
            "repetition": 1,
            "agent_status": "SUCCESS",
            "exit_code": 0,
            "duration_seconds": 2.0,
            "runtime_model": "example-model",
            "evaluation": {"passed": True, "checks": {"nonempty": True}},
            "workspace_mutated": False,
        }
        control = {
            **common,
            "condition": "control",
            "prompt": "Explain the path.",
            "response": "Control answer.",
            "response_words": 10,
            "usage": {"output_tokens": 100},
            "attempt_count": 2,
            "retry_count": 1,
            "attempt_statuses": ["TRUNCATED", "SUCCESS"],
        }
        tlgd = {
            **common,
            "condition": "tlgd",
            "prompt": "Explain the path.\n\nUse TLGD.",
            "response": "TLGD answer. </script><script>alert(1)</script>",
            "response_words": 8,
            "usage": {"output_tokens": 80},
        }
        self.write_json(run_root / "runs" / "control.json", control)
        self.write_json(run_root / "runs" / "tlgd.json", tlgd)
        return run_root

    def test_builds_pairs_prompts_diffs_and_summaries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_root = self.make_run(Path(directory))
            data = renderer.build_report_data(run_root)
        self.assertEqual(data["pairCount"], 1)
        self.assertEqual(data["pairs"][0]["wordReduction"], 20.0)
        self.assertTrue(data["pairs"][0]["comparable"])
        self.assertEqual(data["pairs"][0]["difficulty"], "simple")
        self.assertIn("Use TLGD", data["pairs"][0]["tlgd"]["prompt"])
        self.assertIn("-Control answer.", data["pairs"][0]["diff"])
        self.assertEqual(data["summaries"][0]["outputTokenReduction"], 20.0)
        self.assertEqual(data["summaries"][0]["allWordReduction"], 20.0)
        self.assertEqual(data["summaries"][0]["allOutputTokenReduction"], 20.0)
        self.assertEqual(data["summaries"][0]["comparablePairCount"], 1)
        self.assertEqual(data["summaries"][0]["controlRetries"], 1)
        self.assertFalse(data["summaries"][0]["budgetTracked"])

    def test_render_escapes_script_termination(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_root = self.make_run(Path(directory))
            output = renderer.render_report(run_root)
            rendered = output.read_text(encoding="utf-8")
        self.assertIn("<\\/script><script>alert(1)<\\/script>", rendered)
        self.assertNotIn("</script><script>alert(1)</script>", rendered)
        self.assertIn("Control and TLGD, side by side", rendered)
        self.assertIn('element("details", { open: "" })', rendered)
        self.assertIn("TRUNCATED", rendered)

    def test_summary_excludes_pairs_that_fail_a_gate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_root = self.make_run(Path(directory))
            result_path = run_root / "runs" / "tlgd.json"
            result = json.loads(result_path.read_text())
            result["evaluation"]["passed"] = False
            self.write_json(result_path, result)
            data = renderer.build_report_data(run_root)
        self.assertFalse(data["pairs"][0]["comparable"])
        self.assertEqual(data["summaries"][0]["comparablePairCount"], 0)
        self.assertIsNone(data["summaries"][0]["wordReduction"])
        self.assertEqual(data["summaries"][0]["allWordReduction"], 20.0)
        self.assertEqual(data["summaries"][0]["controlPassed"], 1)
        self.assertEqual(data["summaries"][0]["tlgdPassed"], 0)


if __name__ == "__main__":
    unittest.main()
