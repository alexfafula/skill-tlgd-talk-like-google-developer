# TLGD Real-Repo Benchmark

The TLGD Real-Repo Benchmark measures whether TLGD makes AI-generated technical communication clearer and more efficient without reducing factual accuracy.

The benchmark gives an AI agent a read-only snapshot of a real repository. It compares the same agent and model under two conditions:

- **Control:** TLGD is unavailable, and the prompt doesn't mention it.
- **TLGD:** TLGD is available as a project skill, and the prompt ends with `TLGD`.

Compare conditions within the same agent and model. Don't use absolute token counts to rank different models because their tokenizers, system prompts, and tool protocols differ.

The current manifest is `tlgd-real-repo-v3`. Version 3 keeps the six tasks of version 2 and changes one sentence in the three short prompts: agents may read files in the snapshot. Version 2 forbade running commands, which stopped Codex from reading any file, including the skill, and turned those tasks into a memory test. Results from earlier manifests aren't comparable with version 3.

## Repository snapshot

The benchmark uses [Express](https://github.com/expressjs/express), a widely used Node.js web framework.

| Field | Value |
| --- | --- |
| Repository | `expressjs/express` |
| Version | `5.2.1` |
| Commit | `a3714473feb3d2908add734d340e7755fd85e0a3` |
| Commit date | 2026-07-27 |

The runner checks out this exact commit. A newer Express commit doesn't silently change the benchmark.

## Tasks

The first three tasks isolate the behavior of short answers. The remaining tasks test deeper repository analysis.

1. **Locate one implementation.** Identify `res.json()` and the method it calls next.
2. **List validation commands.** Give only the required prerequisites and repository-defined commands.
3. **Identify one default.** State whether ETags are enabled, name the default, and identify where it is compiled.
4. **Explain an architecture path.** Trace a request from `express()` to `res.send()` and distinguish repository behavior from behavior delegated to dependencies.
5. **Write a contributor procedure.** Explain how to change `res.json()` safely using only files and commands available in the snapshot.
6. **Troubleshoot a real behavior.** Explain why `res.json()` can produce an HTTP `304` response without a body for a conditional request.

The prompts require exact repository paths and symbol names. Every prompt allows read-only inspection and forbids modifying files, installing dependencies, running tests, and using the web. The runner doesn't give the agent the expected answer or the grading assertions.

## Isolation

The runner creates separate control and TLGD workspaces inside the ignored result directory. It exports the pinned repository snapshot without Git history, initializes each workspace as its own Git repository, and copies TLGD only into the treatment workspace. The workspace-local repository makes every CLI treat the snapshot as its own project, so memory, rules, and settings from an enclosing checkout never reach the agent.

Each agent starts a fresh, noninteractive session with read-only tools:

- Claude Code uses project-only settings, restricted read tools, and no session persistence. The control run disables skills.
- Codex uses a read-only sandbox, no approvals, and an ephemeral session. The control run disables the installed TLGD path through the supported per-skill configuration override.
- Agy uses its documented terminal sandbox and a temporary `proceed-in-sandbox` setting. The runner restores the user's exact settings after the run. The control run disables skill expansion.

The agent can read the repository and the treatment skill. It can't edit the snapshot or browse the web.

## Metrics

The runner records provider-reported usage when the CLI exposes it:

- input tokens,
- cached input tokens,
- cache-creation tokens,
- output tokens,
- reasoning tokens,
- cost,
- elapsed time,
- tool calls,
- final-answer words and characters,
- all visible assistant text,
- terminal-step output tokens and finish reason when the agent protocol exposes them.

The report separates three layers that are easy to confuse:

- **Final answer:** the artifact the user actually receives and the quality gate grades.
- **Visible assistant text:** all user-facing assistant messages across intermediate steps and the final deliverable (defaults to final answer when intermediate steps emit no display text).
- **Agent-loop output:** every output token reported across planning, tool calls, and the final step.

A process that exits with code 0 still fails if it never emits a final answer. The runner records that case as `NO_FINAL_ANSWER`, not `SUCCESS`.

The runner also records deterministic style signals for every answer: the number of phrases from a fixed mannerism lexicon (importance announcements, canned transitions, decorative metaphors, praise, inflated verbs, and chatbot filler that TLGD tells the agent to remove), the mean sentence length, the share of sentences longer than 26 words, and the number of headings, bullets, and bold spans. Code blocks and inline code are excluded. These signals describe prose; they never decide the gate.

By default, the runner makes one fresh retry after any `TRUNCATED` result or when an attempt yields no final-answer text (including `NO_FINAL_ANSWER`, or an `ERROR`/`TIMEOUT` that produced no output). Attempts that return partial text on error or a complete but poor answer are not retried. The result records every attempt. Agent-loop tokens, input tokens, cost, tool calls, and elapsed time include all attempts, so a recovered answer keeps its reliability cost. Final-answer and terminal-step metrics describe the selected final attempt.

It calculates paired metrics as follows:

```text
output savings = 1 - (TLGD output tokens / control output tokens)

skill overhead = TLGD input tokens - control input tokens

total token delta = TLGD total tokens - control total tokens
```

Cached and reasoning tokens remain separate when the provider reports them separately. A missing field means that the CLI didn't expose the metric; it doesn't mean zero usage.

## Quality gate

Token reduction counts only when the TLGD answer passes the quality gate.

The automated gate checks that the response:

- isn't empty,
- cites the required repository paths,
- names the required symbols and commands,
- doesn't add explicitly excluded terms or commands,
- doesn't expose research or tool-use narration,
- doesn't cite nonexistent repository paths,
- shows evidence that TLGD activated in the treatment run and didn't activate in the control run,
- leaves the repository snapshot unchanged,
- completed successfully and returned a final answer.

The case's response limit is a separate word budget. The report shows quality and budget side by side, so a correct answer that runs long is visible as such instead of being counted as a quality failure.

Two model judges then score each pair. `benchmarks/judge.py` hides the condition behind the same A/B assignment as `BLIND_REVIEW.md`, shows both answers in both positions to Claude and Codex, and records per-dimension scores, critical errors, listed mannerisms, a preference, and the reason. `JUDGE.md` reports the outcome per judge, agreement between judges, position dependence, and mean scores per condition. Judges see only the prompt, the review criteria, and the answers; they can't verify facts against the repository, and a visibly structured answer can reveal the condition.

```shell
python3 benchmarks/judge.py benchmarks/results/RUN_DIRECTORY
```

A human blind review is optional and was not performed for the published runs; the worksheet exists for anyone who wants to do one. It scores factual accuracy, completeness, clarity, concision, natural tone, and source traceability, and flags canned praise, decorative metaphors, rhetorical scaffolding, and other AI mannerisms. Reject a token-saving result if it introduces a factual error, invents a command, weakens an important condition, omits required information, or makes the prose choppy and mechanical.

## Run the benchmark

Use the permanent entry points for routine runs.

Run one paired 304 smoke test on Claude Code, Codex, and Agy:

```shell
benchmarks/run-smoke.sh
```

Run all six tasks once:

```shell
benchmarks/run-full.sh
```

Rerun only Agy, for example after an adapter or authentication change:

```shell
benchmarks/run-agy.sh
```

Run the headline 304 task three times for a more stable token comparison:

```shell
benchmarks/run-headline.sh
```

Each entry point accepts additional runner options, such as `--timeout 600` or `--keep-workspaces`.

Set the retry limit explicitly when needed. `--max-attempts 1` disables retries; the default is `2`:

```shell
benchmarks/run-full.sh --max-attempts 2
```

Pin models per agent with `--claude-model`, `--codex-model`, and `--agy-model`, or with the `TLGD_BENCH_*_MODEL` keys in `.env` (see `.env.example`).

Use the Python commands directly when you need a custom agent or case selection.

Check the local tools without calling a model:

```shell
python3 benchmarks/run.py doctor
```

Prepare the pinned Express snapshot:

```shell
python3 benchmarks/run.py prepare
```

Run one paired pass with the currently enabled agents:

```shell
python3 benchmarks/run.py run --agents claude,codex,agy --repetitions 1
```

The runner saves each result immediately under `benchmarks/results/`. If a run is interrupted, completed raw results remain available for inspection.

Generate a self-contained report with prompts, formatted and raw responses, side-by-side comparisons, metrics, filters, and unified diffs:

```shell
benchmarks/render-html.sh benchmarks/results/RUN_DIRECTORY
```

Reparse and regrade a completed run after improving the parser or automated gates. This command uses saved traces and doesn't call a model:

```shell
python3 benchmarks/run.py regrade benchmarks/results/RUN_DIRECTORY
benchmarks/render-html.sh benchmarks/results/RUN_DIRECTORY
```

Repeat the headline case three times before publishing an efficiency claim:

```shell
python3 benchmarks/run.py run \
  --agents claude,codex,agy \
  --cases conditional-get-304 \
  --repetitions 3
```

Condition order is deterministic and alternates across repetitions to reduce run-order bias.

## Results

Run `tlgd-real-repo-v3__20260824T225405Z`: four tasks (the three short tasks and `conditional-get-304`), three repetitions, condition order alternated, Claude Code 2.1.241 with `claude-opus-5`, Codex CLI 0.149.0 with `gpt-5.6-sol` (`model_reasoning_effort="medium"`), and Agy 1.1.19 with `gemini-3.7-flash-high`. All 72 answers completed on their first attempt. The published copy, including the HTML report and the judge output, is under `benchmarks/published/tlgd-real-repo-v3__20260824T225405Z/`.

| Host | Control quality | TLGD quality | Control budget | TLGD budget |
| --- | ---: | ---: | ---: | ---: |
| Claude, `claude-opus-5` | 6/12 | 11/12 | 0/12 | 9/12 |
| Codex, `gpt-5.6-sol` | 9/12 | 12/12 | 9/12 | 9/12 |
| Agy, `gemini-3.7-flash-high` | 7/12 | 12/12 | 3/12 | 9/12 |
| **All** | **22/36** | **35/36** | **12/36** | **27/36** |

| Agent | Case | Control quality | tlgd quality | Control budget | tlgd budget | Control words | tlgd words | Word change | Control mannerisms | tlgd mannerisms | Control tokens | tlgd tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| agy | conditional-get-304 | 3/3 | 3/3 | 0/3 | 0/3 | 827 | 833 | +1% | 0 | 0 | 156677 | 161424 |
| agy | etag-default | 1/3 | 3/3 | 0/3 | 3/3 | 135 | 43 | -70% | 0 | 0 | 76725 | 62839 |
| agy | locate-res-json | 3/3 | 3/3 | 3/3 | 3/3 | 55 | 31 | -44% | 0 | 0 | 70172 | 52054 |
| agy | validation-commands | 0/3 | 3/3 | 0/3 | 3/3 | 128 | 50 | -67% | 0 | 0 | 80691 | 80832 |
| claude | conditional-get-304 | 3/3 | 3/3 | 0/3 | 0/3 | 951 | 785 | -18% | 0 | 0 | 5691 | 4978 |
| claude | etag-default | 0/3 | 3/3 | 0/3 | 3/3 | 246 | 73 | -70% | 0 | 0 | 1442 | 854 |
| claude | locate-res-json | 3/3 | 3/3 | 0/3 | 3/3 | 126 | 53 | -60% | 0 | 0 | 641 | 571 |
| claude | validation-commands | 0/3 | 2/3 | 0/3 | 3/3 | 221 | 41 | -80% | 0 | 0 | 1363 | 333 |
| codex | conditional-get-304 | 3/3 | 3/3 | 0/3 | 0/3 | 699 | 639 | -9% | 0 | 0 | 309245 | 231755 |
| codex | etag-default | 0/3 | 3/3 | 3/3 | 3/3 | 83 | 50 | -48% | 0 | 0 | 73666 | 74656 |
| codex | locate-res-json | 3/3 | 3/3 | 3/3 | 3/3 | 41 | 34 | -17% | 0 | 0 | 71522 | 69093 |
| codex | validation-commands | 3/3 | 3/3 | 3/3 | 3/3 | 50 | 38 | -24% | 0 | 0 | 73756 | 96494 |

What the run shows:

- Every control quality failure was scope creep: eight `etag-default` answers explained where the compiled setting is consumed (`lib/response.js`), and six `validation-commands` answers added `npm run lint:fix` or `npm run test-ci`. TLGD removed both on every host. Its one failure was a 22-word Claude answer that dropped the dependency install.
- On the three short tasks TLGD cut the median answer by 17% to 80% while preserving required paths, symbols, and commands across nearly all answers (one answer omitted a dependency-installation step). On the troubleshooting task the medians moved by -18% (Claude), -9% (Codex), and +1% (Agy).
- The mannerism lexicon matched nothing in all 72 answers, and mean sentence length did not differ systematically. On these hosts TLGD changes what an answer covers and how long it is, not its tone; the README's before-and-after example describes older or chattier models.
- Host-reported total tokens fell with TLGD on Claude for every task and moved both ways on Codex and Agy, so the benchmark makes no compute-cost claim.

### Model judges

`benchmarks/judge.py` judged all 36 pairs with `claude-sonnet-5` and `gpt-5.6-sol` (both at medium reasoning effort), each pair in both positions, and graded every answer's coverage of the case's `semantic_facts`. Judges saw the prompt, the review criteria, and the two answers; they couldn't open the repository.

| Judge | TLGD preferred | Control preferred | Tie | Position-dependent |
| --- | ---: | ---: | ---: | ---: |
| Claude (`claude-sonnet-5`) | 21 | 5 | 1 | 9 |
| Codex (`gpt-5.6-sol`) | 27 | 3 | 1 | 5 |

The judges agreed on 24 pairs: TLGD preferred in 18, control in 2, a tie in 1, and a position-dependent verdict in 3. Mean scores on the 0–2 rubric moved most on concision (control 0.85–0.92, TLGD 1.86–1.90) and, according to the Claude judge, on natural tone (1.35 → 1.93) — a difference the mannerism lexicon didn't register, so it reflects sentence-level judgment rather than the listed phrases. Accuracy, completeness, and clarity stayed at or above the control level; traceability was the only dimension where the Claude judge scored TLGD slightly lower (1.85 → 1.71), consistent with shorter answers citing fewer locations. Semantic-fact coverage was 0.98 for TLGD and 0.92 for control under both judges.

A position-dependent verdict means the judge preferred whichever answer it saw first or second; those pairs count as undecided. The full per-pair table is in `JUDGE.md` of the published run.

**Blinding caveat (found 2026-08-26).** Codex and Agy cite files by absolute path, and in this run the path named the condition (`workspaces/<agent>/tlgd/…` against `…/control/…`). The judge prompts for the 24 Codex and Agy pairs therefore contained a segment that could reveal the condition; the 12 Claude pairs cite relative paths and were unaffected. The judges' stated reasons never refer to that segment, but the verdicts for those 24 pairs can't be called blind. `judge.py` now replaces the condition directory with `CONDITION` before building a prompt, `BLIND_REVIEW.md` is generated the same way, and the deterministic results above are unaffected because no gate reads a path. Until the affected pairs are re-judged with neutral paths, treat the pairwise preferences as unblinded for them.

### Blind review

No human review was performed for this run. Scoring factual accuracy in Express internals needs Express expertise, and key factual elements are partially verified by the deterministic gates (existing citations, required paths and commands, no unrequested steps) and by the judges' fact-coverage mode, subject to model-evaluation limits. The harness still writes a `BLIND_REVIEW.md` worksheet per run for anyone who wants to review pairs blind; the claims above rest on the deterministic gates and the two LLM judges.


The six-task diagnostic run and the calibration check that preceded this run are recorded in [`docs/calibration-log.md`](docs/calibration-log.md).

## Reporting rules

Publish a compatibility claim only after every selected task passes the automated gate and the judged run is published with its caveats. Include the agent version, exact model identifier, Express commit, repetitions, median token change, and any missing provider metrics.

Don't generalize one repository result to all technical writing. Keep the 22 synthetic cases in `tlgd/evals/cases.json` as regression tests for modality, destructive actions, UI procedures, accessibility, markup preservation, multilingual behavior, concise answers, prerequisite preservation, natural tone, AI mannerisms, closed scope, exact commands, evidence boundaries, and unsupported universal claims.
