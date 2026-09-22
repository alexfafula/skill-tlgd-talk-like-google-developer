#!/usr/bin/env python3
"""Validate the TLGD skill package with the Python standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
OPENAI_YAML = ROOT / "agents" / "openai.yaml"
REFERENCES = ROOT / "references"
EVALS = ROOT / "evals" / "cases.json"
LICENSE = ROOT / "LICENSE.txt"
NAME = ROOT.name


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    require(match is not None, "SKILL.md must start with YAML frontmatter")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, separator, raw_value = line.partition(":")
        require(bool(separator), f"invalid frontmatter line: {line}")
        value = raw_value.strip()
        if len(value) >= 2 and value[0] == value[-1] == '"':
            value = value[1:-1]
        values[key.strip()] = value
    return values


def yaml_string(text: str, key: str) -> str:
    match = re.search(rf'^\s*{re.escape(key)}:\s*"([^"]*)"\s*$', text, re.MULTILINE)
    require(match is not None, f"agents/openai.yaml is missing quoted {key}")
    return match.group(1)


def validate_metadata() -> None:
    skill_text = SKILL.read_text(encoding="utf-8")
    values = frontmatter(skill_text)
    require(set(values) == {"name", "description"}, "frontmatter must contain only name and description")
    require(values["name"] == NAME, "skill name must match its directory")
    require("Use when" in values["description"], "description must state when to use the skill")
    require("AI agent" in values["description"], "description must remain host-neutral")
    require(not re.search(r"\b(?:Codex|Claude|ChatGPT)\b", values["description"]), "description names a specific agent host")
    require(len(skill_text.splitlines()) <= 100, "SKILL.md must stay at or below 100 lines")

    ui_text = OPENAI_YAML.read_text(encoding="utf-8")
    display_name = yaml_string(ui_text, "display_name")
    short_description = yaml_string(ui_text, "short_description")
    default_prompt = yaml_string(ui_text, "default_prompt")
    require(display_name == "TLGD — Talk Like a Google Developer", "unexpected display_name")
    require(25 <= len(short_description) <= 64, "short_description must contain 25–64 characters")
    require(f"${NAME}" in default_prompt, "default_prompt must invoke the skill")


def validate_host_neutrality() -> None:
    runtime_files = [SKILL, OPENAI_YAML, EVALS, *sorted(REFERENCES.glob("*.md"))]
    host_pattern = re.compile(r"\b(?:Codex|Claude|ChatGPT)\b")
    for path in runtime_files:
        require(
            host_pattern.search(path.read_text(encoding="utf-8")) is None,
            f"{path.relative_to(ROOT)} names a specific AI host",
        )


def validate_license() -> None:
    text = LICENSE.read_text(encoding="utf-8")
    require(text.startswith("MIT License\n"), "LICENSE.txt must contain the MIT License")
    require(
        "Copyright (c) 2026 Aleksander Fafuła <aleksander@fafula.com>" in text,
        "LICENSE.txt has an unexpected copyright notice",
    )


def validate_links() -> None:
    markdown_files = [SKILL, *sorted(REFERENCES.glob("*.md"))]
    linked_references: set[Path] = set()
    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        if len(text.splitlines()) > 100:
            require("## Contents" in text, f"{source.relative_to(ROOT)} needs a contents section")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if re.match(r"(?:https?://|mailto:|#)", target):
                continue
            resolved = (source.parent / target.split("#", 1)[0]).resolve()
            require(resolved.is_file(), f"broken link from {source.relative_to(ROOT)} to {target}")
            if resolved.parent == REFERENCES.resolve():
                linked_references.add(resolved)

    reference_files = {path.resolve() for path in REFERENCES.glob("*.md")}
    orphaned = sorted(path.name for path in reference_files - linked_references)
    require(not orphaned, f"unrouted reference files: {', '.join(orphaned)}")


def validate_source_map() -> int:
    text = (REFERENCES / "source-map.md").read_text(encoding="utf-8")
    urls = set(re.findall(r"https://developers\.google\.com/style(?:/[a-z0-9-]+)?", text))
    require("https://developers.google.com/style" in urls, "source map must include the guide landing page")
    require(len(urls) >= 70, f"source map has only {len(urls)} unique Google style pages")
    return len(urls)


def validate_evals() -> int:
    data = json.loads(EVALS.read_text(encoding="utf-8"))
    require(data.get("schema_version") == 1, "unsupported eval schema")
    cases = data.get("cases")
    require(isinstance(cases, list) and len(cases) >= 10, "at least 10 eval cases are required")
    ids: set[str] = set()
    routed: set[Path] = set()
    allowed_modes = {"answer", "draft", "rewrite", "review", "light-edit", "full-edit"}
    for case in cases:
        require(isinstance(case, dict), "every eval case must be an object")
        case_id = case.get("id")
        require(isinstance(case_id, str) and re.fullmatch(r"[a-z0-9-]+", case_id) is not None, "invalid eval id")
        require(case_id not in ids, f"duplicate eval id: {case_id}")
        ids.add(case_id)
        require(case.get("mode") in allowed_modes, f"invalid mode in {case_id}")
        require(isinstance(case.get("prompt"), str) and case["prompt"].strip(), f"missing prompt in {case_id}")
        assertions = case.get("assertions")
        require(isinstance(assertions, list) and len(assertions) >= 2, f"insufficient assertions in {case_id}")
        routes = case.get("expected_routes")
        require(isinstance(routes, list), f"expected_routes must be a list in {case_id}")
        for route in routes:
            require((ROOT / route).is_file(), f"unknown route in {case_id}: {route}")
            routed.add((ROOT / route).resolve())
    unrouted = sorted(
        path.name for path in REFERENCES.glob("*.md") if path.resolve() not in routed
    )
    require(not unrouted, f"reference files without an eval route: {', '.join(unrouted)}")
    return len(cases)


def main() -> None:
    required = [SKILL, OPENAI_YAML, EVALS, LICENSE]
    require(all(path.is_file() for path in required), "required package file is missing")
    validate_metadata()
    validate_host_neutrality()
    validate_license()
    validate_links()
    source_count = validate_source_map()
    eval_count = validate_evals()
    print(f"TLGD valid: {source_count} source pages, {eval_count} eval cases")


if __name__ == "__main__":
    main()
