# TLGD calibration log

Status: version 3 manifest; diagnostic runs complete; publishable run `tlgd-real-repo-v3__20260824T225405Z` completed and published

Each entry records a run, what the gates and style signals showed, and any change to the skill or the grader that followed. A skill change is made only for a failure that repeats across hosts.

## Run `tlgd-real-repo-v3__20260824T221505Z` — full suite × 1

Agents: Claude Code 2.1.241 with `claude-opus-5`; Codex CLI 0.149.0 with `gpt-5.6-sol` (`model_reasoning_effort="medium"`); Agy 1.1.19 with `gemini-3.7-flash-high`. Six tasks, one repetition, 36 answers. Every answer completed on its first attempt; one Agy control run exited with an error status but still produced an answer.

| Host | Control quality | TLGD quality | Control budget | TLGD budget | Pairs with fewer TLGD words |
| --- | ---: | ---: | ---: | ---: | ---: |
| Claude, `claude-opus-5` | 2/6 | 4/6 | 0/6 | 2/6 | 5/6 |
| Codex, `gpt-5.6-sol` | 6/6 | 4/6 | 4/6 | 5/6 | 5/6 |
| Agy, `gemini-3.7-flash-high` | 3/6 | 5/6 | 4/6 | 5/6 | 6/6 |

Reader-visible word change with TLGD: short tasks -33% to -66% on every host (`locate-res-json` 84→56, 46→31, 51→24; `etag-default` 271→125, 81→52, 131→45; `validation-commands` 190→90, 22→19, 130→70); deep tasks -3% to -18%, with one pair (Claude `request-response-path`) +1%. Mannerism-lexicon hits were 0 in 35 of 36 answers, and mean sentence length did not move systematically, so on these hosts TLGD changes scope and length rather than tone.

### Failures

TLGD quality failures (5 of 18):

- `etag-default` on Claude and Codex: the answer added `lib/response.js`, where the compiled setting is consumed. The prompt asks for the default and the compilation point only.
- `validation-commands` on Claude and Agy: the answer added `npm run test-ci` or `npm run lint:fix`, which `package.json` defines but local validation doesn't require.
- `validation-commands` on Codex: a 19-word answer that gave the right prerequisites and commands but never named `package.json`, which the gate required although the prompt didn't ask for it.

Control quality failures (6 of 18) had the same shapes, plus `npx mocha` in both `res-json-contributor-procedure` control answers, which TLGD removed on both hosts.

Word budgets, which were calibrated on earlier models, were exceeded by `claude-opus-5` in both conditions on five of six tasks. Budget is reported separately from quality and doesn't decide the gate.

### Changes

1. Skill (`tlgd/SKILL.md`, "Honor the output contract"): added one example to the closed-contract rule — a question about where a setting is defined or compiled excludes where it is consumed, and a question about required commands excludes optional, CI, or auto-fix scripts that the same file also defines. Reason: the same scope creep appeared on three hosts in two tasks.
2. Grader (`benchmarks/manifest.json`, `validation-commands`): the prompt now asks the agent to cite the file that defines the commands, so the existing `package.json` path requirement follows from the prompt instead of being an unstated expectation.

The manifest ID stays `tlgd-real-repo-v3`; the run above predates change 2 and is diagnostic evidence, not a publishable result.

## Run `tlgd-real-repo-v3__20260824T224702Z` — calibration check, `etag-default` and `validation-commands` × 1

Same hosts and models. Twelve answers after change 1 and change 2.

| Case | Host | Control | TLGD |
| --- | --- | --- | --- |
| `etag-default` | Claude | 254 words, adds `lib/response.js` | 77 words, passes |
| `etag-default` | Codex | 90 words, adds `lib/response.js` | 47 words, passes |
| `etag-default` | Agy | 166 words, adds `lib/response.js` | 45 words, passes (host error, see below) |
| `validation-commands` | Claude | 162 words, adds `lint:fix` and `test-ci` | 34 words, omits the dependency install |
| `validation-commands` | Codex | 42 words, passes | 25 words, omits the dependency install |
| `validation-commands` | Agy | 116 words, adds `lint:fix` and `test-ci` | 43 words, passes |

The scope creep from the first run didn't recur on any host. Two TLGD answers to `validation-commands` dropped `npm install`, which both hosts had included in the first run; with one repetition this is noise rather than a pattern, so the skill wasn't changed again. The prompt now asks for "prerequisites" in the plural, so the dependency step is clearly inside the question.

### Host-status change

Agy reported `status: ERROR` for three answers across both runs while delivering a complete final response; the attached error was an invalid argument in an intermediate tool call (`missing property 'Pattern'`, `missing properties 'toolSummary', 'toolAction'`). The runner now keeps such an answer as `SUCCESS`, records the message in `host_error`, and shows `host-error` in the report's Finish column. An `ERROR` status without a delivered answer still fails execution.

Neither run above can be regraded against the current manifest because the `validation-commands` prompt changed; both remain diagnostic evidence.

## Run `tlgd-real-repo-v3__20260824T225405Z` — publishable run, 4 tasks × 3 repetitions

Same hosts and models; manifest with the plural "prerequisites" wording; condition order alternated across repetitions. 72 answers, every one on its first attempt.

| Host | Control quality | TLGD quality | Control budget | TLGD budget |
| --- | ---: | ---: | ---: | ---: |
| Claude, `claude-opus-5` | 6/12 | 11/12 | 0/12 | 9/12 |
| Codex, `gpt-5.6-sol` | 9/12 | 12/12 | 9/12 | 9/12 |
| Agy, `gemini-3.7-flash-high` | 7/12 | 12/12 | 3/12 | 9/12 |
| **All** | **22/36** | **35/36** | **12/36** | **27/36** |

Median reader-visible words per case, control → TLGD: `locate-res-json` 126→53 (Claude), 41→34 (Codex), 55→31 (Agy); `etag-default` 246→73, 83→50, 135→43; `validation-commands` 221→41, 50→38, 128→50; `conditional-get-304` 951→785, 699→639, 827→833.

Every control failure was scope creep: `lib/response.js` in eight `etag-default` answers and `npm run lint:fix` or `npm run test-ci` in six `validation-commands` answers. The one TLGD failure was a 22-word Claude answer to `validation-commands` that omitted the dependency install. Mannerism-lexicon hits were zero in all 72 answers; mean sentence length did not differ systematically. Host-reported total tokens fell with TLGD on Claude for every case and moved both ways on Codex and Agy.

No skill change followed this run. Judge output is recorded with the published run.

### Metadata correction

The Codex CLI doesn't report its model in the JSON stream, and the runner recorded `requested_model: null` for Codex answers made without `--codex-model`. The runner now reads the default from `~/.codex/config.toml` and records the reasoning effort each agent ran with. For the publishable run, `environment.json` and `judge.json` were corrected after the fact to `gpt-5.6-sol` (source noted in the file); the raw answer files were left as saved.
