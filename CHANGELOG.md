# Changelog

All notable changes to TLGD are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Three TLGD eval cases: release notes with dates and numbers, page restructuring, and no trigger-word echo. The validator now requires every reference file to be routed by at least one eval case.
- Three simple real-repository benchmark cases before the deeper architecture, procedure, and troubleshooting cases.
- Four synthetic regression cases for narrow-answer stopping, concise procedures, performative validation, and AI mannerisms.
- Five synthetic regression cases for closed scope, tool narration, source-defined commands, dependency boundaries, and unsupported universal claims.
- A self-contained HTML benchmark report with prompts, side-by-side answers, raw Markdown, filters, metrics, and unified diffs.
- Benchmark gates for excluded terms and commands, response limits, process narration, missing final answers, and truncated output.
- Separate benchmark metrics for all agent-loop output and the terminal answer step.
- Bounded retries for missing `NO_FINAL_ANSWER` output and any `TRUNCATED` run, with every attempt and its full token and time cost preserved in the report.
- Deterministic style signals for every benchmark answer: mannerism-lexicon hits, mean sentence length, long-sentence share, and heading, bullet, and bold counts, reported beside quality and budget but never gating.
- A blinded pairwise LLM judge, `benchmarks/judge.py`, that hides the condition behind the same A/B assignment as `BLIND_REVIEW.md`, asks Claude and Codex to score both answers in both positions, and writes `JUDGE.md` and `judge.json` with per-judge outcomes, agreement, position dependence, and mean dimension scores. Its `--facts` mode grades each answer's coverage of a case's `semantic_facts` statements.
- `benchmarks/summarize.py`, which reports per host and case the quality and budget pass counts and the medians of reader words, mannerisms, tokens, and duration over repetitions, plus the median per-pair word change.
- `benchmarks/publish_run.py`, which copies only reports and summaries of a run into `benchmarks/published/`, redacts run-local paths, and refuses to publish a machine path, `file://` URL, or `.env` value.
- A GitHub Actions workflow that runs the validator, the benchmark unit tests, and `doctor`, plus `.env.example`.
- `docs/calibration-log.md`, which records every benchmark run that changed the skill or the grader.

### Changed

- Reworked the README with framed positioning, a side-by-side before-and-after example, and copy-and-paste installation commands for Claude Code, Codex, Cursor, Agy (Antigravity CLI), GitHub Copilot, OpenCode, Windsurf, and Cline.
- Added compact, human prose rules for direct syntax, natural rhythm, information preservation, repetition removal, and prerequisite protection.
- Added a technical-colleague voice contract that removes canned praise, decorative metaphors, rhetorical scaffolding, false intimacy, and performative insight.
- Added a closed output contract for narrow scope, exact source tokens, source-defined commands, bounded dependency evidence, quantifier checks, and final-answer-only output. The closed-contract rule gives one example of scope: where a setting is defined or compiled excludes where it is consumed, and required commands exclude optional, CI, or auto-fix scripts the same file defines (see the calibration log).
- Positioned TLGD as a way to reduce extraneous cognitive load without removing the task's intrinsic complexity.
- Aligned the references with the current Google guide: temperatures as `50&nbsp;°C`, phone numbers with nonbreaking hyphens and the `800-555-0100` example range, numerals for step numbers, a leading zero in decimals, and lettered substeps.
- TLGD no longer echoes its trigger word when it applies the style.
- The benchmark manifest is `tlgd-real-repo-v3`: the three short prompts allow read-only inspection explicitly (the version 2 wording forbade running commands, which stopped Codex from reading any file, including the skill), and `validation-commands` asks for the file that defines the commands.
- Every benchmark workspace is initialized as its own Git repository, so an agent no longer inherits memory, rules, or settings from the enclosing checkout; a Claude control run had answered in Polish because it loaded the maintainer's project memory.
- The benchmark gate separates quality from the word budget; a correct answer that runs long is reported as such instead of failing quality.
- Results record the Codex model even without a `--codex-model` flag by reading `~/.codex/config.toml`, plus the reasoning effort each agent ran with; the judge records its judge models the same way.
- The benchmark runner and the judge wait out a briefly missing agent CLI, such as during a Claude Code auto-update, instead of aborting the run; the judge also records progress after every pair, resumes with `--resume` by redoing only verdicts that were unusable (for example after an HTTP 429 session limit), and records the host error behind an unusable verdict.
- An Agy answer that arrives with `status: ERROR` from an invalid intermediate tool call counts as delivered; the message is recorded in `host_error`. An error without an answer still fails execution.

### Removed

- OpenCode and Qwen support from the benchmark harness, its tests, `run-qwen.sh`, and the documentation. The benchmark agents are Claude Code, Codex, and Agy.

## [0.1.0] - 2026-08-19

### Added

- The `tlgd` skill for explaining, drafting, rewriting, reviewing, and editing technical communication.
- A compact execution contract with protected meaning, task modes, safety overrides, and conditional reference routing.
- Nine topic-specific reference summaries and a source map covering 70 official Google developer documentation style pages.
- Ten original behavior-evaluation cases for answers, procedures, API references, reviews, multilingual responses, accessibility, and meaning preservation.
- A standard-library validator for package metadata, links, routing, source coverage, evaluation cases, and host-neutral runtime content.
- Universal installation and usage instructions for supported AI agents.

[Unreleased]: https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/releases/tag/v0.1.0
