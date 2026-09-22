from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


RUNNER_PATH = Path(__file__).resolve().parents[1] / "run.py"
SPEC = importlib.util.spec_from_file_location("tlgd_benchmark_runner", RUNNER_PATH)
assert SPEC is not None and SPEC.loader is not None
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class ManifestTests(unittest.TestCase):
    def test_manifest_is_valid(self) -> None:
        manifest = runner.load_manifest()
        self.assertEqual(manifest["id"], "tlgd-real-repo-v3")
        self.assertEqual(len(manifest["cases"]), 6)
        self.assertEqual(
            [case["difficulty"] for case in manifest["cases"][:3]],
            ["simple", "simple", "simple"],
        )

    def test_condition_order_is_stable(self) -> None:
        first = runner.stable_condition_order(42, "claude", "conditional-get-304", 1)
        second = runner.stable_condition_order(42, "claude", "conditional-get-304", 1)
        self.assertEqual(first, second)
        self.assertEqual(set(first), {"control", "tlgd"})

    def test_agy_print_receives_the_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            original = runner.find_executable
            runner.find_executable = lambda agent: "/example/agy"
            try:
                command, _ = runner.build_command(
                    "agy", "control", Path(directory), "EXPECTED PROMPT", {}
                )
            finally:
                runner.find_executable = original
        self.assertEqual(command[-2:], ["--print", "EXPECTED PROMPT"])
        self.assertLess(command.index("--output-format"), command.index("--print"))
        self.assertNotIn("--mode", command)
        self.assertIn("--new-project", command)
        self.assertIn("--effort", command)

    def test_agent_environment_drops_unrelated_variables(self) -> None:
        environment = {
            "HOME": "/home/test",
            "PATH": "/bin",
            "LC_ALL": "C.UTF-8",
            "TLGD_BENCH_CODEX_MODEL": "example-model",
            "UNRELATED_SECRET": "do-not-pass",
        }
        agy = runner.agent_environment("agy", environment)
        self.assertEqual(
            agy, {"HOME": "/home/test", "PATH": "/bin", "LC_ALL": "C.UTF-8", "NO_COLOR": "1"}
        )
        codex = runner.agent_environment("codex", environment)
        self.assertEqual(codex["TLGD_BENCH_CODEX_MODEL"], "example-model")
        self.assertNotIn("UNRELATED_SECRET", codex)

    def test_agy_requested_model_replaces_effort_flag(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            original = runner.find_executable
            runner.find_executable = lambda agent: "/example/agy"
            try:
                command, requested = runner.build_command(
                    "agy",
                    "tlgd",
                    Path(directory),
                    "TLGD",
                    {"TLGD_BENCH_AGY_MODEL": "gemini-3.6-flash-medium"},
                )
            finally:
                runner.find_executable = original
        self.assertEqual(requested, "gemini-3.6-flash-medium")
        self.assertIn("--model", command)
        self.assertNotIn("--effort", command)

    def test_run_parser_accepts_model_overrides(self) -> None:
        args = runner.build_parser().parse_args(
            [
                "run",
                "--agents",
                "claude,codex,agy",
                "--claude-model",
                "claude-example",
                "--codex-model",
                "codex-example",
                "--agy-model",
                "agy-example",
            ]
        )
        self.assertEqual(args.claude_model, "claude-example")
        self.assertEqual(args.codex_model, "codex-example")
        self.assertEqual(args.agy_model, "agy-example")
        self.assertEqual(args.max_attempts, 2)

    def test_regrade_parser_accepts_saved_run(self) -> None:
        args = runner.build_parser().parse_args(["regrade", "benchmarks/results/example"])
        self.assertEqual(args.command, "regrade")
        self.assertEqual(args.run_root, Path("benchmarks/results/example"))





class ParserTests(unittest.TestCase):
    def test_agy_stream(self) -> None:
        stdout = "\n".join(
            [
                json.dumps(
                    {
                        "event": "init",
                        "init": {
                            "model": "gemini-example",
                            "permission_mode": "proceed-in-sandbox",
                        },
                    }
                ),
                json.dumps(
                    {
                        "event": "step_update",
                        "step_update": {
                            "state": "ACTIVE",
                            "step_type": "tool",
                            "tool_name": "view_file",
                            "tool_info": {
                                "parameters": {"path": ".agents/skills/tlgd/SKILL.md"}
                            },
                        },
                    }
                ),
                json.dumps(
                    {
                        "event": "result",
                        "result": {
                            "status": "SUCCESS",
                            "response": "Final answer",
                            "usage": {
                                "input_tokens": 200,
                                "output_tokens": 20,
                                "thinking_tokens": 5,
                                "cache_read_tokens": 50,
                                "total_tokens": 220,
                            },
                        },
                    }
                ),
            ]
        )
        events = runner.json_events(stdout)
        self.assertEqual(runner.extract_response("agy", events), "Final answer")
        usage = runner.extract_usage("agy", events)
        self.assertEqual(usage["reasoning_tokens"], 5)
        self.assertEqual(usage["cached_input_tokens"], 50)
        self.assertEqual(runner.extract_model(events, None), "gemini-example")
        self.assertEqual(runner.extract_status("agy", events, 0, False), "SUCCESS")
        self.assertEqual(runner.skill_activation_evidence(events), ["read-tlgd-skill"])
        self.assertEqual(len(runner.tool_objects(events)), 1)
        self.assertEqual(runner.mutation_tool_evidence(events), [])
        self.assertEqual(runner.extract_finish_reason("agy", events), "SUCCESS")

    def test_measurement_extractions(self) -> None:
        codex_events = [
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Step 1: Reading file"}},
            {"type": "turn.completed", "usage": {"input_tokens": 100, "output_tokens": 15}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Step 2: Analysis complete", "finish_reason": "stop"}},
            {"type": "turn.completed", "usage": {"input_tokens": 120, "output_tokens": 25}},
        ]
        self.assertEqual(
            runner.extract_visible_text("codex", codex_events, "Step 2: Analysis complete"),
            "Step 1: Reading file\n\nStep 2: Analysis complete"
        )
        final_usage = runner.extract_final_step_usage("codex", codex_events)
        self.assertEqual(final_usage["output_tokens"], 25)
        self.assertEqual(runner.extract_finish_reason("codex", codex_events), "stop")

        # Codex turn with intermediate tool steps: turn usage should NOT be attributed to final step
        codex_events_with_tools = [
            {"type": "item.completed", "item": {"type": "tool_call", "name": "exec_command"}},
            {"type": "item.completed", "item": {"type": "tool_result", "output": "ok"}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Final answer", "finish_reason": "stop"}},
            {"type": "turn.completed", "usage": {"input_tokens": 500, "output_tokens": 100}},
        ]
        self.assertIsNone(runner.extract_final_step_usage("codex", codex_events_with_tools)["output_tokens"])
        self.assertEqual(runner.extract_usage("codex", codex_events_with_tools)["output_tokens"], 100)

        # Codex turn with explicit item-level usage
        codex_events_item_usage = [
            {"type": "item.completed", "item": {"type": "tool_call", "name": "exec_command"}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Final answer", "usage": {"output_tokens": 18}}},
            {"type": "turn.completed", "usage": {"input_tokens": 500, "output_tokens": 100}},
        ]
        self.assertEqual(runner.extract_final_step_usage("codex", codex_events_item_usage)["output_tokens"], 18)

        # Claude: excludes user prompt, does not duplicate multi-block assistant response, extracts assistant.message.usage
        claude_events = [
            {"type": "user", "message": {"role": "user", "content": [{"type": "text", "text": "USER PROMPT"}]}},
            {
                "type": "assistant",
                "message": {
                    "role": "assistant",
                    "content": [
                        {"type": "text", "text": "First paragraph."},
                        {"type": "text", "text": "Second paragraph."},
                    ],
                    "usage": {"input_tokens": 50, "output_tokens": 8},
                    "stop_reason": "end_turn",
                },
            },
            {"type": "result", "result": "First paragraph.\n\nSecond paragraph."},
        ]
        self.assertEqual(
            runner.extract_visible_text("claude", claude_events, "First paragraph.\n\nSecond paragraph."),
            "First paragraph.\n\nSecond paragraph."
        )
        self.assertEqual(runner.extract_final_step_usage("claude", claude_events)["output_tokens"], 8)
        self.assertEqual(runner.extract_final_step_usage("claude", claude_events)["input_tokens"], 50)
        self.assertEqual(runner.extract_finish_reason("claude", claude_events), "end_turn")

        # Claude: stream_event wrapping
        claude_stream_events = [
            {
                "type": "stream_event",
                "event": {
                    "type": "assistant",
                    "message": {
                        "role": "assistant",
                        "content": [{"type": "text", "text": "Stream answer"}],
                        "usage": {"input_tokens": 40, "output_tokens": 12},
                        "stop_reason": "end_turn",
                    },
                },
            },
            {"type": "result", "result": "Stream answer"},
        ]
        self.assertEqual(runner.extract_final_step_usage("claude", claude_stream_events)["output_tokens"], 12)
        self.assertEqual(runner.extract_finish_reason("claude", claude_stream_events), "end_turn")

        # Claude: intermediate tool use step followed by final answer
        claude_tool_events = [
            {
                "type": "assistant",
                "message": {
                    "role": "assistant",
                    "content": [{"type": "tool_use", "id": "t1", "name": "read"}],
                    "usage": {"input_tokens": 30, "output_tokens": 15},
                    "stop_reason": "tool_use",
                },
            },
            {"type": "user", "message": {"role": "user", "content": [{"type": "tool_result", "content": "file data"}]}},
            {
                "type": "assistant",
                "message": {
                    "role": "assistant",
                    "content": [{"type": "text", "text": "Final answer after tool"}],
                    "usage": {"input_tokens": 70, "output_tokens": 25},
                    "stop_reason": "end_turn",
                },
            },
            {"type": "result", "result": "Final answer after tool", "usage": {"input_tokens": 100, "output_tokens": 40}},
        ]
        self.assertEqual(runner.extract_final_step_usage("claude", claude_tool_events)["output_tokens"], 25)
        self.assertEqual(runner.extract_finish_reason("claude", claude_tool_events), "end_turn")
        self.assertEqual(runner.extract_usage("claude", claude_tool_events)["output_tokens"], 40)

        # Claude: preserves legitimate repeated intermediate narration
        claude_repeat_events = [
            {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": "Retrying step..."}]}},
            {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": "Retrying step..."}]}},
            {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": "Success."}]}},
        ]
        self.assertEqual(
            runner.extract_visible_text("claude", claude_repeat_events, "Success."),
            "Retrying step...\n\nRetrying step...\n\nSuccess."
        )

        # Codex: earlier message has usage, but final answer message does not -> final_step_usage must be None
        codex_earlier_usage_events = [
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Intermediate step", "usage": {"output_tokens": 7}}},
            {"type": "item.completed", "item": {"type": "tool_call", "name": "exec_command"}},
            {"type": "item.completed", "item": {"type": "tool_result", "output": "ok"}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Final answer without usage", "finish_reason": "stop"}},
            {"type": "turn.completed", "usage": {"input_tokens": 500, "output_tokens": 100}},
        ]
        self.assertIsNone(runner.extract_final_step_usage("codex", codex_earlier_usage_events)["output_tokens"])
        self.assertEqual(runner.extract_usage("codex", codex_earlier_usage_events)["output_tokens"], 100)

        # Codex: earlier message has usage (7), final answer message has usage (18) -> returns 18, not 7
        codex_both_usage_events = [
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Intermediate step", "usage": {"output_tokens": 7}}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Final answer", "usage": {"output_tokens": 18}}},
            {"type": "turn.completed", "usage": {"input_tokens": 500, "output_tokens": 100}},
        ]
        self.assertEqual(runner.extract_final_step_usage("codex", codex_both_usage_events)["output_tokens"], 18)

        # Claude: earlier message has usage (7), but final answer message does not -> final_step_usage must be None
        claude_earlier_usage_events = [
            {
                "type": "assistant",
                "message": {
                    "role": "assistant",
                    "content": [{"type": "text", "text": "Earlier message"}],
                    "usage": {"input_tokens": 20, "output_tokens": 7},
                },
            },
            {
                "type": "assistant",
                "message": {
                    "role": "assistant",
                    "content": [{"type": "text", "text": "Final answer"}],
                    "stop_reason": "end_turn",
                },
            },
            {"type": "result", "result": "Final answer", "usage": {"input_tokens": 100, "output_tokens": 40}},
        ]
        self.assertIsNone(runner.extract_final_step_usage("claude", claude_earlier_usage_events)["output_tokens"])
        self.assertEqual(runner.extract_usage("claude", claude_earlier_usage_events)["output_tokens"], 40)

        # Claude: earlier message has usage (7), final answer message has usage (25) -> returns 25, not 7
        claude_both_usage_events = [
            {
                "type": "assistant",
                "message": {
                    "role": "assistant",
                    "content": [{"type": "text", "text": "Earlier message"}],
                    "usage": {"input_tokens": 20, "output_tokens": 7},
                },
            },
            {
                "type": "assistant",
                "message": {
                    "role": "assistant",
                    "content": [{"type": "text", "text": "Final answer"}],
                    "usage": {"input_tokens": 50, "output_tokens": 25},
                    "stop_reason": "end_turn",
                },
            },
            {"type": "result", "result": "Final answer", "usage": {"input_tokens": 100, "output_tokens": 40}},
        ]
        self.assertEqual(runner.extract_final_step_usage("claude", claude_both_usage_events)["output_tokens"], 25)

        # Claude stream: earlier message has usage (7), final stream generation has usage (14) -> returns 14, not 7
        claude_stream_generation_events = [
            {
                "type": "assistant",
                "message": {
                    "role": "assistant",
                    "content": [{"type": "text", "text": "Earlier message"}],
                    "usage": {"input_tokens": 20, "output_tokens": 7},
                },
            },
            {"type": "stream_event", "event": {"type": "message_start", "message": {"usage": {"input_tokens": 45}}}},
            {
                "type": "stream_event",
                "event": {
                    "type": "message_delta",
                    "delta": {"stop_reason": "end_turn"},
                    "usage": {"output_tokens": 14},
                },
            },
            {"type": "result", "result": "Stream final answer"},
        ]
        final_stream_usage = runner.extract_final_step_usage("claude", claude_stream_generation_events)
        self.assertEqual(final_stream_usage["output_tokens"], 14)
        self.assertEqual(final_stream_usage["input_tokens"], 45)

    def test_configured_codex_model_reads_config_toml(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "config.toml"
            config.write_text('model = "gpt-example"\nmodel_reasoning_effort = "xhigh"\n', encoding="utf-8")
            self.assertEqual(runner.configured_codex_model(config), "gpt-example")
            self.assertIsNone(runner.configured_codex_model(Path(directory) / "missing.toml"))
        self.assertEqual(runner.reasoning_effort("codex", None), "medium")
        self.assertEqual(runner.reasoning_effort("claude", "claude-opus-5"), "medium")
        self.assertEqual(runner.reasoning_effort("agy", "gemini-3.7-flash-high"), "high")
        self.assertEqual(runner.reasoning_effort("agy", None), "medium")

    def test_find_executable_waits_out_a_vanished_binary(self) -> None:
        original_locate = runner.locate_executable
        original_sleep = runner.time.sleep
        calls = {"count": 0}

        def flaky(agent: str) -> str | None:
            calls["count"] += 1
            return None if calls["count"] == 2 else "/usr/local/bin/fake-claude"

        runner.locate_executable = flaky
        runner.time.sleep = lambda seconds: None
        try:
            runner.KNOWN_EXECUTABLES.pop("claude", None)
            self.assertEqual(runner.find_executable("claude"), "/usr/local/bin/fake-claude")
            self.assertEqual(runner.find_executable("claude"), "/usr/local/bin/fake-claude")
            self.assertEqual(calls["count"], 3)
        finally:
            runner.locate_executable = original_locate
            runner.time.sleep = original_sleep
            runner.KNOWN_EXECUTABLES.pop("claude", None)

    def test_agy_error_status_without_answer_invalidates_execution(self) -> None:
        events = runner.json_events(
            json.dumps(
                {
                    "event": "result",
                    "result": {"status": "ERROR", "response": "", "error": "sandbox failed"},
                }
            )
        )
        self.assertEqual(runner.extract_status("agy", events, 0, False), "ERROR")
        self.assertEqual(runner.extract_host_error("agy", events), "sandbox failed")

    def test_agy_error_status_with_delivered_answer_keeps_the_answer(self) -> None:
        events = runner.json_events(
            json.dumps(
                {
                    "event": "result",
                    "result": {
                        "status": "ERROR",
                        "response": "Complete answer.",
                        "error": "invalid arguments:\n- missing property 'Pattern'",
                    },
                }
            )
        )
        self.assertEqual(runner.extract_status("agy", events, 0, False), "SUCCESS")
        self.assertEqual(
            runner.extract_host_error("agy", events), "invalid arguments: - missing property 'Pattern'"
        )
        self.assertIsNone(runner.extract_host_error("claude", events))

    def test_claude_stream(self) -> None:
        stdout = "\n".join(
            [
                json.dumps(
                    {
                        "type": "assistant",
                        "message": {
                            "content": [
                                {
                                    "type": "tool_use",
                                    "name": "Skill",
                                    "input": {"skill": "tlgd"},
                                }
                            ]
                        },
                    }
                ),
                json.dumps(
                    {
                        "type": "result",
                        "result": "Use `lib/response.js`.",
                        "usage": {"input_tokens": 100, "output_tokens": 12},
                        "total_cost_usd": 0.01,
                        "modelUsage": {"claude-example": {}},
                    }
                ),
            ]
        )
        events = runner.json_events(stdout)
        self.assertEqual(runner.extract_response("claude", events), "Use `lib/response.js`.")
        self.assertEqual(runner.extract_usage("claude", events)["total_tokens"], 112)
        self.assertEqual(runner.extract_model(events, None), "claude-example")
        self.assertEqual(runner.skill_activation_evidence(events), ["skill-tool-tlgd"])

    def test_claude_primary_model_ignores_small_helper_call(self) -> None:
        events = [
            {
                "type": "result",
                "modelUsage": {
                    "claude-haiku-helper": {"outputTokens": 16},
                    "claude-opus-5": {"outputTokens": 7257},
                },
            }
        ]
        self.assertEqual(runner.extract_model(events, "opus"), "claude-opus-5")

    def test_codex_jsonl(self) -> None:
        stdout = "\n".join(
            [
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {
                            "type": "command_execution",
                            "command": "sed -n 1,80p .agents/skills/tlgd/SKILL.md",
                        },
                    }
                ),
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {"type": "agent_message", "text": "Final answer"},
                    }
                ),
                json.dumps(
                    {
                        "type": "turn.completed",
                        "usage": {
                            "input_tokens": 200,
                            "cached_input_tokens": 50,
                            "output_tokens": 20,
                        },
                    }
                ),
            ]
        )
        events = runner.json_events(stdout)
        self.assertEqual(runner.extract_response("codex", events), "Final answer")
        self.assertEqual(runner.extract_usage("codex", events)["output_tokens"], 20)
        self.assertEqual(runner.skill_activation_evidence(events), ["read-tlgd-skill"])






class EvaluationTests(unittest.TestCase):
    def test_retry_for_any_empty_or_truncated_answer(self) -> None:
        self.assertTrue(runner.should_retry_incomplete_answer("TRUNCATED", "", 1, 2))
        self.assertTrue(runner.should_retry_incomplete_answer("TRUNCATED", "partial", 1, 2))
        self.assertTrue(runner.should_retry_incomplete_answer("NO_FINAL_ANSWER", "", 1, 2))
        self.assertFalse(runner.should_retry_incomplete_answer("NO_FINAL_ANSWER", "partial", 1, 2))
        self.assertTrue(runner.should_retry_incomplete_answer("ERROR", "", 1, 2))
        self.assertTrue(runner.should_retry_incomplete_answer("TIMEOUT", "", 1, 2))
        self.assertFalse(runner.should_retry_incomplete_answer("ERROR", "partial", 1, 2))
        self.assertFalse(runner.should_retry_incomplete_answer("TRUNCATED", "", 2, 2))

    def test_regrade_keeps_retry_cost_and_selects_the_final_attempt(self) -> None:
        first_stdout = json.dumps(
            {
                "type": "result",
                "subtype": "success",
                "result": "",
                "usage": {"input_tokens": 100, "output_tokens": 30},
            }
        )
        second_stdout = json.dumps(
            {
                "type": "result",
                "subtype": "success",
                "result": "Final answer.",
                "usage": {"input_tokens": 200, "output_tokens": 20},
            }
        )
        result = {
            "agent": "claude",
            "condition": "control",
            "requested_model": "example-model",
            "workspace_mutated": False,
            "attempts": [
                {
                    "attempt_number": 1,
                    "exit_code": 0,
                    "timed_out": False,
                    "duration_seconds": 1.0,
                    "raw_stdout": first_stdout,
                    "raw_stderr": "",
                },
                {
                    "attempt_number": 2,
                    "exit_code": 0,
                    "timed_out": False,
                    "duration_seconds": 2.0,
                    "raw_stdout": second_stdout,
                    "raw_stderr": "",
                },
            ],
        }
        case = {
            "required_paths": [],
            "required_term_groups": [],
            "required_commands": [],
            "max_response_words": 10,
        }
        with tempfile.TemporaryDirectory() as directory:
            runner.regrade_result(result, case, Path(directory))
        self.assertEqual(result["agent_status"], "SUCCESS")
        self.assertEqual(result["attempt_statuses"], ["NO_FINAL_ANSWER", "SUCCESS"])
        self.assertEqual(result["attempt_count"], 2)
        self.assertEqual(result["retry_count"], 1)
        self.assertEqual(result["usage"]["output_tokens"], 50)
        self.assertEqual(result["selected_attempt_usage"]["output_tokens"], 20)
        self.assertIsNone(result["final_step_usage"]["output_tokens"])

    def test_grounding_and_activation_gate(self) -> None:
        case = {
            "required_paths": ["lib/response.js", "test/res.send.js"],
            "required_term_groups": [["res.send"], ["ETag"]],
            "required_commands": ["npm test"],
        }
        response = (
            "`lib/response.js` implements `res.send` and handles the ETag. "
            "`test/res.send.js` covers the behavior. Run `npm test`."
        )
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory)
            (repository / "lib").mkdir()
            (repository / "test").mkdir()
            (repository / "lib" / "response.js").touch()
            (repository / "test" / "res.send.js").touch()
            evaluation = runner.evaluate_response(
                case, "tlgd", response, repository, ["skill-tool-tlgd"]
            )
        self.assertTrue(evaluation["passed"])
        self.assertEqual(evaluation["invalid_paths"], [])

    def test_nonexistent_citation_fails(self) -> None:
        case = {
            "required_paths": [],
            "required_term_groups": [],
            "required_commands": [],
        }
        with tempfile.TemporaryDirectory() as directory:
            evaluation = runner.evaluate_response(
                case,
                "control",
                "See `lib/not-real.js`.",
                Path(directory),
                [],
            )
        self.assertFalse(evaluation["passed"])
        self.assertEqual(evaluation["invalid_paths"], ["lib/not-real.js"])

    def test_scope_and_visible_narration_gates(self) -> None:
        case = {
            "required_paths": [],
            "required_term_groups": [],
            "required_commands": ["npm test"],
            "forbidden_commands": ["npm run test-ci"],
            "forbidden_terms": ["optional coverage"],
            "max_response_words": 8,
        }
        response = "Run npm test. Do not add optional coverage."
        visible = "Now let me inspect the scripts.\n" + response
        with tempfile.TemporaryDirectory() as directory:
            evaluation = runner.evaluate_response(
                case,
                "control",
                response,
                Path(directory),
                [],
                visible_text=visible,
            )
        self.assertFalse(evaluation["passed"])
        self.assertFalse(evaluation["checks"]["forbidden_terms"])
        self.assertFalse(evaluation["checks"]["no_process_narration"])
        self.assertTrue(evaluation["checks"]["response_word_limit"])
        self.assertEqual(evaluation["process_narration"], ["Now let me inspect the scripts."])

    def test_style_metrics_count_mannerisms_and_sentence_length(self) -> None:
        text = (
            "It is important to note that the cache is the connective tissue of the system. "
            "In order to reset it, run `npm run in-order-to-not-count` and then wait.\n\n"
            "```js\n// in order to: code is ignored\nconst crucial = leverage();\n```\n\n"
            "- Delete the folder.\n"
            "- Great question! Restart the service, which takes about a minute, and confirm that the "
            "health check reports a passing status before you continue with the next deployment step "
            "in the release checklist."
        )
        style = runner.style_metrics(text)
        self.assertEqual(
            style["mannerisms"],
            ["it is important to note", "connective tissue", "in order to", "great question"],
        )
        self.assertEqual(style["mannerism_count"], 4)
        self.assertEqual(style["sentence_count"], 5)
        self.assertEqual(style["long_sentence_share"], 0.2)
        self.assertGreater(style["mean_sentence_words"], 5)
        self.assertEqual(style["bullet_count"], 2)
        self.assertEqual(style["heading_count"], 0)
        self.assertEqual(runner.style_metrics("")["sentence_count"], 0)

    def test_evaluation_separates_quality_from_word_budget(self) -> None:
        case = {
            "required_paths": [],
            "required_term_groups": [],
            "required_commands": [],
            "max_response_words": 3,
        }
        with tempfile.TemporaryDirectory() as directory:
            evaluation = runner.evaluate_response(
                case, "control", "One two three four five.", Path(directory), []
            )
        self.assertTrue(evaluation["passed"])
        self.assertTrue(evaluation["quality_passed"])
        self.assertFalse(evaluation["budget_passed"])
        self.assertFalse(evaluation["all_checks_passed"])
        self.assertIn("mannerism_count", evaluation["style"])

    def test_reader_word_count_ignores_hidden_markdown_link_destinations(self) -> None:
        response = (
            "Open [beta](file:///a/very/long/temporary/workspace/reports/beta.json) "
            "and [the source](https://example.com/repository/source.py#L20)."
        )

        self.assertEqual(runner.reader_response_word_count(response), 5)
        self.assertGreater(
            runner.response_word_count(response),
            runner.reader_response_word_count(response),
        )

    def test_reader_word_count_keeps_markdown_syntax_inside_code(self) -> None:
        response = "`[label](file:///tmp/example)`\n```md\n[label](file:///tmp/example)\n```"

        self.assertEqual(
            runner.reader_response_word_count(response),
            runner.response_word_count(response),
        )

    def test_reader_word_count_handles_inline_code_inside_link_label(self) -> None:
        response = "Read [`request.blueprints`](file:///tmp/workspace/src/wrappers.py#L181)."

        self.assertEqual(runner.reader_response_word_count(response), 3)
        self.assertGreater(
            runner.response_word_count(response),
            runner.reader_response_word_count(response),
        )


if __name__ == "__main__":
    unittest.main()


class BlindingTests(unittest.TestCase):
    def test_workspace_paths_hide_the_condition_segment(self) -> None:
        treatment = (
            "See file://RUN_ROOT/workspaces/agy/tlgd/repository/lib/response.js#L234-L248 and "
            "[`package.json`](RUN_ROOT/workspaces/codex/tlgd/repository/package.json:82)."
        )
        control = treatment.replace("/tlgd/", "/control/")
        neutral = runner.neutralize_workspace_paths(control)
        self.assertEqual(runner.neutralize_workspace_paths(treatment), neutral)
        self.assertNotIn("/control/", neutral)
        self.assertNotIn("/tlgd/", neutral)
        self.assertIn("file://RUN_ROOT/workspaces/agy/CONDITION/repository/lib/response.js#L234-L248", neutral)
        self.assertIn("(RUN_ROOT/workspaces/codex/CONDITION/repository/package.json:82)", neutral)
        untouched = "workspace/runs/beta/report.md, the control group, and `workspaces/agy` alone"
        self.assertEqual(runner.neutralize_workspace_paths(untouched), untouched)

