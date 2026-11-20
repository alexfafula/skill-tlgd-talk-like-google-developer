# TLGD — Talk Like a Google Developer

An [Agent Skill](https://agentskills.io/specification) based on the [Google developer documentation style guide](https://developers.google.com/style). Add `TLGD` to a prompt to get direct technical answers without chatbot filler, unrequested context, or lost commands.

> [!NOTE]
> TLGD is an independent project. It is not affiliated with, endorsed by, or maintained by Google.

## Why use this

Models often bury a simple answer under long introductions, repeated conclusions, and polite phrasing. TLGD strips the presentation overhead while keeping exact commands, caveats, and code intact.

```text
Without TLGD:
In order to successfully initialize the local development environment, it is
important to note that users will need to execute `tool auth --project example-project`
prior to attempting to start the server, which can then be accomplished by running
`tool serve`.

With TLGD:
Authenticate before you start the server:
1. Run `tool auth --project example-project`.
2. Run `tool serve`.
```

## Install

Requires Node.js and `npx`. Uses the [`skills` CLI](https://github.com/vercel-labs/skills) to install the skill globally across projects. Restart your agent session if it doesn't pick up the skill right away.

**Claude Code:**
```shell
npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a claude-code -y
```

**Codex:**
```shell
npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a codex -y
```

**Other agents:**

* **Cursor:** `npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a cursor -y`
* **Agy (Antigravity CLI):** `npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a antigravity-cli -y`
* **GitHub Copilot:** `npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a github-copilot -y`
* **OpenCode:** `npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a opencode -y`
* **Windsurf:** `npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a windsurf -y`
* **Cline:** `npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a cline -y`

See the [`skills` CLI supported agents list](https://github.com/vercel-labs/skills#supported-agents) for other targets.

### Run without installing

Load TLGD for a single session without modifying your global config:

```shell
# Claude Code
npx skills@latest use https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd --agent claude-code

# Codex
npx skills@latest use https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd --agent codex
```

### Update

```shell
npx skills@latest update tlgd
```

Restart the agent session if it continues using a cached version.

## Usage

Add `TLGD` anywhere in your prompt (or `$tlgd` in agents that use explicit skill mentions):

```text
Explain why this HTTP request returns 304. TLGD
```

Agents with automatic skill discovery may also trigger it implicitly on documentation tasks, though explicit mentions are more predictable.

**Examples:**

```text
# Explain a concept
$tlgd Explain eventual consistency to an application developer. Start with the practical consequence.

# Draft a procedure
Use $tlgd to turn these notes into a setup procedure. Preserve every command exactly.

# Rewrite docs
Rewrite this API guide with $tlgd. Keep its scope, caveats, code, and links.

# Review without rewriting
Review this README with $tlgd. Rank the findings by reader impact and don't rewrite the file.

# Other languages (applies clarity and structure rules without forcing English grammar)
Po polsku wyjaśnij, jak działa cache HTTP. Użyj $tlgd.
```

## How it works

TLGD instructs the model to:

* Put the answer, outcome, or first required action at the top.
* Keep facts, caveats, certainty levels, commands, identifiers, and UI labels unchanged.
* Use direct, plain language instead of conversational filler.
* Structure explanations, procedures, and API references around the task.
* Use fuller phrasing when safety, irreversible actions, or complex sequences require it.

It supports separate modes for answering, drafting, rewriting, reviewing, light editing, and full editing. It only applies to the current response or file task and does not persist across sessions unless invoked again.

**Limits:** TLGD does not call a second model, intercept responses, or run background hooks. It is prompt-level guidance for the active agent and operates under that agent's standard file permissions. It improves phrasing and structure, not factual accuracy—if a style rule conflicts with accuracy, safety, or your requirements, meaning takes priority.

## Benchmark results

Tested with Claude Code (Fable 5.2, Opus 5.5), Codex (GPT-5.6-Terra), and Agy (Gemini 3.8 Flash) across 36 prompts on a pinned Express repository snapshot. Full methodology is in [BENCHMARK.md](BENCHMARK.md).

* **Scope discipline:** TLGD passed the closed-scope check in 35/36 runs vs. 22/36 for the baseline.
* **Length:** On three narrow questions, median response length dropped by 17% to 80% while keeping required symbols, paths, and commands (one run omitted a dependency installation step). On an open troubleshooting question, length changed by -18% to +1%.
* **Pairwise judging:** Shown both outputs in randomized order, Claude preferred TLGD in 21/36 pairs (5 for baseline) and Codex preferred TLGD in 27/36 pairs (3 for baseline). They agreed on 24 pairs (18 for TLGD). Judges rated TLGD higher on concision and equal or higher on accuracy, completeness, and clarity (98% of expected facts conveyed vs. 92% for baseline).

**Caveats:**
* Frontier models already avoid most obvious chatbot mannerisms, so the measurable gain here is scope discipline and brevity rather than tone.
* Total token usage moved in both directions depending on the host, so this is not a guaranteed compute-cost optimization.
* Judge prompts for the Codex and Agy runs included a workspace path segment that could leak which condition was active; those pairs are scheduled for re-evaluation with neutral paths.

## Repository layout

`SKILL.md` stays small to keep context overhead low, loading topic-specific rules from `references/` only when needed.

```text
skill-tlgd-talk-like-google-developer/
├── tlgd/
│   ├── SKILL.md                 Core behavior, routing, and safety contract
│   ├── agents/openai.yaml       Display metadata and default invocation
│   ├── references/              Topic-specific style guidance
│   │   └── source-map.md        Index of 70 official guide pages
│   ├── evals/cases.json         22 behavior-evaluation cases
│   ├── scripts/check.py         Package validator (Python stdlib only)
│   └── LICENSE.txt              License included with installed copies
├── CHANGELOG.md                 Version history
├── BENCHMARK.md                 Benchmark methodology
├── benchmarks/                  Runners and HTML report generator
├── LICENSE                      Repository license
└── README.md                    This file
```

### Validate a local checkout

```shell
python3 tlgd/scripts/check.py
# Expected output: TLGD valid: 70 source pages, 22 eval cases
```

## Author & License

Created by [Aleksander Fafuła](mailto:aleksander@fafula.com).

Licensed under the [MIT License](LICENSE). Reference summaries and principles are adapted from the [Google developer documentation style guide](https://developers.google.com/style) ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), code samples under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)).
