# TLGD — Talk Like a Google Developer

> [!TIP]
> ## Clear, scope-disciplined answers with less filler
>
> **Make it talk like a Google engineer—just add `TLGD` anywhere in your prompt.**
>
> One word. Any prompt. Clearer technical communication.

An AI can know the answer and still bury it in filler, scope creep, and unrequested detail. TLGD turns that answer into clear, direct technical communication without changing the facts, commands, caveats, or code.

TLGD is an [Agent Skill](https://agentskills.io/specification) built on the principles of the [Google developer documentation style guide](https://developers.google.com/style). It helps an AI agent explain, draft, rewrite, and review technical content.

TLGD is inspired by `TL;DR` (`too long; didn't read`) and designed to be just as memorable. Install it once. Then write `TLGD` anywhere in your prompt.

> [!NOTE]
> TLGD is an independent project. It isn't affiliated with, endorsed by, or maintained by Google.

## Spend working memory on the problem

Technical work already consumes a limited working-memory budget: you must track state, constraints, commands, and consequences at the same time. [Cognitive load theory](https://journals.sagepub.com/doi/10.1177/0963721420922183) calls mental effort caused by the presentation instead of the problem *extraneous cognitive load*. Chatbot filler, repeated conclusions, buried prerequisites, and decorative language all spend that budget without helping you act.

TLGD is designed to reduce presentation overhead while preserving the problem's real complexity. It keeps the conditions, caveats, and technical tokens you need, then makes their relationships easier to see. Clarity isn't cosmetic: a prerequisite hidden in a wall of text is still hard to use.

## Claude one-line install

Install TLGD globally for Claude Code:

```shell
npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a claude-code -y
```

## Codex one-line install

Install TLGD globally for Codex:

```shell
npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a codex -y
```

These commands install TLGD globally for use across projects. They use the open source [`skills` CLI](https://github.com/vercel-labs/skills) and require Node.js and `npx`. Start a new agent session if TLGD doesn't appear immediately.

## Other popular agents

The following commands are also ready to paste.

### Cursor

```shell
npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a cursor -y
```

### Agy (Antigravity CLI)

```shell
npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a antigravity-cli -y
```

### GitHub Copilot

```shell
npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a github-copilot -y
```

### OpenCode

```shell
npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a opencode -y
```

### Windsurf

```shell
npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a windsurf -y
```

### Cline

```shell
npx skills@latest add https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd -g -a cline -y
```

For every supported target, see the [`skills` CLI agent list](https://github.com/vercel-labs/skills#supported-agents).

## Try without installing

### Claude Code

Start a supported agent with TLGD loaded for one session:

```shell
npx skills@latest use https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd --agent claude-code
```

### Codex

```shell
npx skills@latest use https://github.com/alexfafula/skill-tlgd-talk-like-google-developer/tree/main/tlgd --agent codex
```

These commands don't install TLGD or change the agent's persistent configuration.

## Same meaning. Less chatbotese.

TLGD removes friction without removing meaning. The following comparison keeps both commands and their required order.

<table>
  <thead>
    <tr>
      <th scope="col">Before TLGD</th>
      <th scope="col">After TLGD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td valign="top">In order to successfully initialize the local development environment, it is important to note that users will need to execute <code>tool auth --project example-project</code> prior to attempting to start the server, which can then be accomplished by running <code>tool serve</code>.</td>
      <td valign="top">Authenticate before you start the server:<ol><li>Run <code>tool auth --project example-project</code>.</li><li>Run <code>tool serve</code>.</li></ol></td>
    </tr>
  </tbody>
</table>

## Use TLGD

After installation, write `TLGD` anywhere in your prompt:

```text
Explain why this HTTP request returns 304. TLGD
```

In agents that support explicit `$skill` mentions, you can also use `$tlgd`:

```text
Explain why this HTTP request returns 304. $tlgd
```

TLGD also supports implicit activation when the agent discovers skills automatically and the task involves technical communication. Use an explicit invocation when you want predictable activation.

### Explain a technical concept

```text
$tlgd Explain eventual consistency to an application developer. Start with the practical consequence.
```

### Draft a procedure

```text
Use $tlgd to turn these notes into a concise setup procedure. Preserve every command exactly.
```

### Rewrite documentation

```text
Rewrite this API guide with $tlgd. Preserve its scope, caveats, code, and links.
```

### Review without rewriting

```text
Review this README with $tlgd. Rank the findings by reader impact and don't rewrite the document.
```

### Respond in another language

```text
Po polsku wyjaśnij, jak działa cache HTTP. Użyj $tlgd.
```

TLGD keeps the requested language. For languages other than English, it applies the guide's clarity, accessibility, and structural principles without forcing English-specific grammar rules.

## What TLGD does

TLGD helps an AI agent:

- Lead with the answer, outcome, or required action.
- Preserve facts, caveats, certainty levels, commands, identifiers, and UI labels.
- Use direct, conversational, inclusive, and globally understandable language.
- Organize explanations, procedures, API references, and reviews around the reader's task.
- Apply detailed guidance only when the content needs it.
- Use fuller language when safety, irreversible actions, or complex sequences require it.

TLGD includes separate modes for answering, drafting, rewriting, reviewing, light editing, and full editing. It applies to the current answer or artifact; it doesn't claim to remain active across sessions.

## Evidence

The [real-repository benchmark](BENCHMARK.md) gives the same agent and model the same question about a pinned Express snapshot with and without TLGD. In the published run on Claude Code (`claude-opus-5`), Codex (`gpt-5.6-sol`), and Agy (`gemini-3.7-flash-high`), TLGD answers passed the closed-scope quality gate 35 times out of 36; the control answers passed 22 times. On the three narrow questions TLGD cut the median answer by 17% to 80% while preserving required paths, symbols, and commands across nearly all answers (one answer omitted a dependency-installation step); on the troubleshooting question it changed length by -18% to +1%.

What the benchmark doesn't show: a tone effect on these models, whose control answers already contained none of the mannerisms TLGD removes, and a compute-cost saving, because host-reported tokens moved both ways. The effect on current frontier models is scope discipline and length.

Two model judges, shown each pair in both positions, preferred the TLGD answer in 21 (Claude judge) and 27 (Codex judge) of 36 pairs and the control answer in 5 and 3; they agreed on 24 pairs, 18 of them for TLGD. Both judges scored TLGD answers higher on concision and at least as high on accuracy, completeness, and clarity, and found them to convey 98% of the expected facts against 92% for the control. One caveat: the judge prompts for the Codex and Agy pairs contained a workspace path segment that could reveal the condition; `BENCHMARK.md` records it, and those pairs are due for re-judging with neutral paths.

## Style never outranks meaning

TLGD treats facts, constraints, caveats, certainty levels, warnings, step order, and exact technical tokens as protected information. If a style preference conflicts with accuracy, safety, accessibility, or the user's requirements, meaning wins.

TLGD doesn't call a second model, intercept every response, or run a background hook that edits files. It guides the agent producing the original response. An agent can change a document only as part of the task you give it and under that agent's normal permissions.

## Architecture

TLGD keeps its execution contract small and loads detailed guidance only when a task needs it:

```text
skill-tlgd-talk-like-google-developer/
├── tlgd/
│   ├── SKILL.md                 Core behavior, routing, and safety contract
│   ├── agents/openai.yaml       Display metadata and default invocation
│   ├── references/              Topic-specific style guidance
│   │   └── source-map.md        Index of 70 official guide pages
│   ├── evals/cases.json         Twenty-two behavior-evaluation cases
│   ├── scripts/check.py         Deterministic package validator
│   └── LICENSE.txt              License included with installed copies
├── CHANGELOG.md                 Version history
├── BENCHMARK.md                 TLGD real-repository benchmark method
├── benchmarks/                  Reusable runners and HTML report generator
├── LICENSE                      Repository license
└── README.md                    Installation and usage guide
```

This progressive-disclosure design gives short answers a small context footprint while retaining detailed guidance for procedures, API references, accessibility, terminology, markup, and other specialized tasks.

## Validate a checkout

Clone the repository, and run the validator from its root:

```shell
python3 tlgd/scripts/check.py
```

A valid package reports the following result:

```text
TLGD valid: 70 source pages, 22 eval cases
```

The validator checks metadata, internal links, reference routing, source coverage, evaluation cases, and host-neutral language. It uses only the Python standard library.

## Update TLGD

Update installed skills with the `skills` CLI:

```shell
npx skills@latest update tlgd
```

Restart the agent session if it continues to use a cached version.

## Source and scope

TLGD condenses the public Google developer documentation style guide into an original decision framework for AI agents. The official guide remains authoritative for edge cases; TLGD's source map routes the agent to the relevant live page instead of loading the entire guide for every request.

TLGD improves communication. It doesn't verify technical facts, replace domain expertise, or override the user's explicit requirements and project conventions.

## Author

Created by [Aleksander Fafuła](mailto:aleksander@fafula.com).

## License

TLGD is available under the [MIT License](LICENSE). Portions of the reference summaries and principles are adapted from the [Google developer documentation style guide](https://developers.google.com/style), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (code samples under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)).
