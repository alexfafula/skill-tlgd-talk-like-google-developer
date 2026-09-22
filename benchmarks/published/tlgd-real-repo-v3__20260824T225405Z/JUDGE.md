# Blinded LLM judge for `tlgd-real-repo-v3__20260824T225405Z`

> [!NOTE]
> Model-judged verdicts. Judges saw the prompt, the review criteria, and both answers with hidden conditions, in both positions. They could not inspect the repository or fixture, and a visibly structured answer can reveal the condition. Complete the human blind review before publishing a claim.

Judges: claude, codex. Pairs judged: 36.

## Outcome per judge

| Judge | tlgd preferred | control preferred | tie | neither | position-dependent | unavailable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| claude | 21 | 5 | 1 | 0 | 9 | 0 |
| codex | 27 | 3 | 1 | 0 | 5 | 0 |

Judge agreement: 24 unanimous and 12 split of 36 pairs with every judge's verdict.

## Unanimous outcomes per agent

| Agent | tlgd preferred | control preferred | tie | neither | position-dependent | split |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| agy | 6 | 0 | 0 | 0 | 1 | 5 |
| claude | 9 | 0 | 0 | 0 | 1 | 2 |
| codex | 3 | 2 | 1 | 0 | 1 | 5 |

## Mean dimension scores (0–2)

### claude

| Condition | accuracy | clarity | completeness | concision | natural_tone | traceability |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| control | 1.74 | 1.71 | 1.89 | 0.85 | 1.35 | 1.85 |
| tlgd | 1.94 | 1.92 | 1.9 | 1.9 | 1.93 | 1.71 |

### codex

| Condition | accuracy | clarity | completeness | concision | natural_tone | traceability |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| control | 1.75 | 1.83 | 1.76 | 0.92 | 1.74 | 1.9 |
| tlgd | 1.81 | 1.97 | 1.92 | 1.86 | 2.0 | 1.88 |

## Semantic fact coverage

Share of a case's semantic_facts statements that an answer conveys, judged per answer without a pair.

| Judge | Condition | Mean coverage | Answers |
| --- | --- | ---: | ---: |
| claude | control | 0.92 | 36 |
| claude | tlgd | 0.98 | 36 |
| codex | control | 0.92 | 36 |
| codex | tlgd | 0.98 | 36 |

| Agent | claude/control | claude/tlgd | codex/control | codex/tlgd |
| --- | ---: | ---: | ---: | ---: |
| agy | 0.9 | 1.0 | 0.94 | 1.0 |
| claude | 0.85 | 0.94 | 0.83 | 0.94 |
| codex | 1.0 | 1.0 | 1.0 | 1.0 |

## Pairs

| Agent | Case | Rep | Judge | Order A/B | Order B/A | Combined | Critical error | Reason |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- |
| agy | conditional-get-304 | 1 | claude | tlgd | tlgd | tlgd | none | Both answers cover the same core criteria (res.json delegating to res.send, ETag generation attributed to the etag dependency, req.fresh attributed to the fresh dependency, the 304 header-stripping/empty-body block, and  |
| agy | conditional-get-304 | 1 | codex | control | control | control | control, tlgd | Both answers incorrectly add `QUERY` as a method accepted by `req.fresh`; the cited Express getter permits GET and HEAD, so this invents and weakens a required condition. Both also overstate that disabling automatic ETag |
| agy | conditional-get-304 | 2 | claude | tlgd | control | position-dependent | none | Both answers cover the same required mechanism (res.json delegating to res.send, ETag generation via the etag dependency, req.fresh gating status(304), header stripping/empty body) with essentially identical code citatio |
| agy | conditional-get-304 | 2 | codex | tlgd | control | position-dependent | control, tlgd | B is easier to continue from because it gives a compact, explicit list of required conditions, separates Express’s guards and response mutation from the `etag` and `fresh` dependencies, and includes a useful mismatched-E |
| agy | conditional-get-304 | 3 | claude | tlgd | control | position-dependent | none | Both answers cover the same four review criteria accurately and cite the same implementation lines (res.json delegating to res.send, ETag generation via the external etag package, req.fresh via the external fresh package |
| agy | conditional-get-304 | 3 | codex | tlgd | tlgd | tlgd | control, tlgd | B requires less rereading because its linear code path cleanly connects res.json(), res.send(), ETag generation, req.fresh, header removal, and res.end(), while clearly assigning comparison logic to fresh and digest gene |
| agy | etag-default | 1 | claude | tlgd | tlgd | tlgd | none | Both correctly answer yes, cite the same defaultConfiguration line and compileETag/wetag symbols with exact paths and line ranges, satisfying the core criteria. Answer A adds extra detail beyond the requested scope — a f |
| agy | etag-default | 1 | codex | tlgd | tlgd | tlgd | none | B answers yes first, identifies the `'weak'` default in `lib/application.js` at `app.defaultConfiguration`, and traces compilation through `app.set` to `exports.compileETag` in `lib/utils.js`, including the resulting `'e |
| agy | etag-default | 2 | claude | control | tlgd | position-dependent | none | Both correctly answer yes, cite the weak default in app.defaultConfiguration (lib/application.js) and compileETag in lib/utils.js. A is terser but its citation ranges are muddled (e.g., overlapping/inconsistent line span |
| agy | etag-default | 2 | codex | tlgd | tlgd | tlgd | none | A answers yes immediately, identifies the `'weak'` default in `lib/application.js` at `app.defaultConfiguration`, and names `compileETag` in `lib/utils.js`, with the relevant `app.set` trigger, then stops. B contains the |
| agy | etag-default | 3 | claude | tlgd | control | position-dependent | none | Both correctly lead with 'Yes', identify the 'weak' default set in app.defaultConfiguration in lib/application.js, and cite compileETag in lib/utils.js, satisfying the core criteria with exact paths, symbols, and line ra |
| agy | etag-default | 3 | codex | tlgd | tlgd | tlgd | none | A lets the reader continue with less rereading: it answers yes immediately, gives the `'weak'` default in `lib/application.js` at `app.defaultConfiguration`, and identifies `compileETag` in `lib/utils.js` plus its invoca |
| agy | locate-res-json | 1 | claude | tlgd | tlgd | tlgd | none | Both correctly identify res.json at lib/response.js#L234-L248 delegating to this.send(body). A answers in two tight sentences exactly as the criteria specify. B pads the same facts into headers and bullet lists, and adds |
| agy | locate-res-json | 1 | codex | tlgd | tlgd | tlgd | none | Answer A directly identifies the exact repository path and symbol, then states the delegation to `res.send` via `this.send(body)` in one concise sentence. Answer B contains the same required facts, but repeats the path a |
| agy | locate-res-json | 2 | claude | tlgd | tlgd | tlgd | none | Both correctly cite lib/response.js#L234-L248 for res.json and L247 for the this.send(body) call, satisfying the core criteria. A delivers this in two clean sentences matching the requested tight format and reads like a  |
| agy | locate-res-json | 2 | codex | tlgd | tlgd | tlgd | none | Both identify the exact path and symbols and correctly state that `res.json` delegates through `this.send(body)` to `res.send()`. A is preferable because it answers in one compact sentence without B’s heading, labeled bu |
| agy | locate-res-json | 3 | claude | control | tlgd | position-dependent | none | Both correctly identify res.json in lib/response.js (lines 234-248) delegating to this.send(body). B pinpoints the exact line (247) where the send call occurs within json's body, giving a reader a precise spot to jump to |
| agy | locate-res-json | 3 | codex | tlgd | tlgd | tlgd | none | Both correctly identify `res.json` in `lib/response.js` and its delegation to `res.send()` through `this.send(body)`, with exact symbol and line citations. A is preferable because it delivers the same required informatio |
| agy | validation-commands | 1 | claude | tlgd | tlgd | tlgd | control | The task explicitly says to give npm run lint and npm test as the validation commands and not to add optional coverage scripts or generic explanations. Answer A lists four extra scripts (lint:fix, test-ci, test-cov, test |
| agy | validation-commands | 1 | codex | tlgd | tlgd | tlgd | control | B puts the Node.js and dependency prerequisites first, then gives exactly the two required commands—`npm run lint` and `npm test`—with their underlying scripts and package.json citation. A includes the required informati |
| agy | validation-commands | 2 | claude | tlgd | tlgd | tlgd | control | The review criteria explicitly state 'Do not add optional coverage scripts, focused test adaptations, or generic explanations' and to give only npm run lint and npm test as validation commands. Answer A does exactly this |
| agy | validation-commands | 2 | codex | tlgd | tlgd | tlgd | control | Answer A puts the Node.js and dependency prerequisites first, then gives exactly `npm run lint` and `npm test`, with the defining `package.json` lines cited. Answer B includes the required information and precise citatio |
| agy | validation-commands | 3 | claude | tlgd | tlgd | tlgd | control | Both correctly identify Node >=18, npm install, and cite package.json for scripts. However, the task explicitly instructs not to add optional coverage scripts or focused test adaptations. Answer A violates this directly  |
| agy | validation-commands | 3 | codex | tlgd | tlgd | tlgd | control | B puts the Node.js and dependency prerequisites first, then gives only the two required validation commands—`npm run lint` and `npm test`—with a precise package.json citation. A is internally accurate and well cited, but |
| claude | conditional-get-304 | 1 | claude | tlgd | tlgd | tlgd | control | Both answers cover the same code path with comparable line-level citations (res.json → res.send, ETag generation, req.fresh, the 304 body/header stripping) and both ground verification in test/req.fresh.js and test/res.s |
| claude | conditional-get-304 | 1 | codex | tlgd | tlgd | tlgd | control, tlgd | A cleanly traces res.json() → res.send() → ETag generation → req.fresh → 304 stripping, accurately separates Express policy from dependency internals, and gives bounded verification tied to exact tests and request header |
| claude | conditional-get-304 | 2 | claude | control | control | control | none | Both answers cover the same required ground (res.json→res.send delegation, ETag generation, req.fresh gating, header/body stripping on 304, Express-vs-dependency boundary, and test-grounded verification) with comparable  |
| claude | conditional-get-304 | 2 | codex | tlgd | tlgd | tlgd | control, tlgd | A is easier to follow and correctly separates Express’s orchestration from `etag` and `fresh`. Both answers contain a material false condition: setting `Transfer-Encoding` prevents generated ETags, but does not make a 30 |
| claude | conditional-get-304 | 3 | claude | control | tlgd | position-dependent | none | Both answers correctly cover all four review criteria with comparable code-path detail and Express-vs-dependency tables. B edges ahead on traceability (it gives precise line ranges like test/res.send.js:471-590 for the e |
| claude | conditional-get-304 | 3 | codex | tlgd | tlgd | tlgd | control, tlgd | A would require less reconstruction because its central res.json → res.send → generated ETag → req.fresh → 304/body-strip chain is direct, and it clearly bounds dependency ownership. However, it adds an unsupported requi |
| claude | etag-default | 1 | claude | tlgd | tlgd | tlgd | none | Both correctly answer yes, cite lib/application.js:95 for the weak default and compileETag()/lib/utils.js for compilation, matching the review criteria exactly. A stops there, matching the instruction to stop without exp |
| claude | etag-default | 1 | codex | tlgd | tlgd | tlgd | none | A answers yes immediately, identifies the weak default in `lib/application.js` and the `compileETag()` path in `lib/utils.js`, and stops. B contains the required facts and exact citations, but adds unrelated details abou |
| claude | etag-default | 2 | claude | tlgd | tlgd | tlgd | none | Both correctly answer yes, cite lib/application.js:95 for the 'weak' default and the compileETag call in app.set, and describe compileETag's mapping in lib/utils.js. The task explicitly asks to stop after identifying the |
| claude | etag-default | 2 | codex | tlgd | tlgd | tlgd | none | B answers yes first, identifies the weak default in `lib/application.js` and the compilation through `compileETag()` in `lib/utils.js`, and stops there. A is also correct and more extensively traceable, but its generator |
| claude | etag-default | 3 | claude | tlgd | tlgd | tlgd | none | Both correctly answer yes, cite lib/application.js:95 for the 'weak' default, and describe compileETag in lib/utils.js mapping true/'weak' to wetag, 'strong' to etag, false to none — satisfying the core criteria with exa |
| claude | etag-default | 3 | codex | tlgd | tlgd | tlgd | control | Answer A directly satisfies all criteria: it begins with yes, identifies the weak default in `lib/application.js` under `app.defaultConfiguration`, and traces compilation through `app.set` to `compileETag` in `lib/utils. |
| claude | locate-res-json | 1 | claude | tlgd | tlgd | tlgd | control | Both correctly locate res.json at lib/response.js:234 and its delegation to res.send. A stays strictly within scope: direct, two sentences, exact citation, no extraneous material. B answers the same core question correct |
| claude | locate-res-json | 1 | codex | tlgd | tlgd | tlgd | control | A directly identifies `res.json = function json(obj)` at `lib/response.js:234` and its delegation through `return this.send(body)` with minimal reconstruction. B contains the required path and symbols, but violates the e |
| claude | locate-res-json | 2 | claude | tlgd | tlgd | tlgd | control | The task explicitly instructs not to add JSONP, caching, test, or contributor-workflow details. Answer A violates this by discussing res.jsonp (line 262) and caching/transport mechanics (ETag, Content-Length, charset han |
| claude | locate-res-json | 2 | codex | tlgd | tlgd | tlgd | control | B directly identifies the exact path and symbol—`lib/response.js:234`, `res.json = function json(obj)`—and states that the serialized body is delegated to `this.send(body)`/`res.send`. A reaches the same conclusion but a |
| claude | locate-res-json | 3 | claude | tlgd | tlgd | tlgd | control | Both correctly locate res.json at lib/response.js:234 and its delegation to res.send. Answer A is accurate but directly violates the stated scope constraint by adding JSONP details (res.jsonp discussion), plus unrequeste |
| claude | locate-res-json | 3 | codex | tlgd | tlgd | tlgd | control | B directly identifies `res.json` at `lib/response.js:234` and its delegation through `return this.send(body)` to `res.send`, in one sentence. A contains the required information but violates the explicit scope by adding  |
| claude | validation-commands | 1 | claude | tlgd | tlgd | tlgd | control | The task explicitly instructs not to add optional coverage scripts, focused test adaptations, or generic explanations, and to give only npm run lint and npm test as validation commands. Answer A directly violates this by |
| claude | validation-commands | 1 | codex | tlgd | tlgd | tlgd | control | B puts the required Node.js and installed-development-dependency prerequisites first, then gives exactly `npm run lint` and `npm test`, attributing both to `package.json` and showing their precise script expansions. A co |
| claude | validation-commands | 2 | claude | control | tlgd | position-dependent | control, tlgd | Both answers violate one explicit review criterion each. A correctly puts Node.js and dependency prerequisites first (engine version, npm, dev dependencies, npm install) and gives exact citations with line numbers, but t |
| claude | validation-commands | 2 | codex | control | tlgd | position-dependent | control, tlgd | A lets the reader proceed because it states both required prerequisite categories—Node.js >=18 and installed development dependencies—before giving `npm run lint` and `npm test`, with exact `package.json` citations. Howe |
| claude | validation-commands | 3 | claude | tlgd | tlgd | tlgd | control | The review criteria explicitly says not to add optional coverage scripts, focused test adaptations, or generic explanations, yet Answer A lists test-cov, test-ci, test-tap, test-cov in a table, plus CI workflow details ( |
| claude | validation-commands | 3 | codex | tlgd | tlgd | tlgd | control | B puts the two prerequisites first, then gives exactly the required `npm run lint` and `npm test` commands with their precise script definitions and attributes them to `package.json`. A contains the required information  |
| codex | conditional-get-304 | 1 | claude | control | control | control | none | Both answers are highly similar in structure, coverage of the four review criteria, and citation density (res.json→send delegation, ETag/fresh separation from Express vs dependency logic, 304 header/body stripping, and c |
| codex | conditional-get-304 | 1 | codex | tlgd | tlgd | tlgd | none | Both answers accurately cover the full path: JSON serialization delegates to send(), Express generates or uses an ETag, req.fresh delegates conditional matching to fresh, and the 304 branch strips representation headers  |
| codex | conditional-get-304 | 2 | claude | tlgd | tlgd | tlgd | none | Both answers cover the same required content — res.json() delegating to res.send(), ETag generation, the req.fresh check with dependency attribution, header stripping on 304, and a bounded three-request verification plan |
| codex | conditional-get-304 | 2 | codex | control | tlgd | position-dependent | control | Both answers satisfy every review criterion and clearly separate Express’s control flow from dependency-owned ETag generation and freshness comparison. B is marginally easier to continue from because its “Required condit |
| codex | conditional-get-304 | 3 | claude | tlgd | tlgd | tlgd | none | Both answers cover the same required content (res.json delegating to send, ETag generation via app-level etag fn plus the external etag package, req.fresh gating on method/status, the 304 branch stripping headers and emp |
| codex | conditional-get-304 | 3 | codex | control | tlgd | position-dependent | none | Both answers cover the required path, conditions, dependency boundary, header/body removal, tests, and bounded verification. B requires slightly less reconstruction because it gathers all necessary conditions into a dedi |
| codex | etag-default | 1 | claude | control | control | control | none | Both correctly answer yes and cite app.defaultConfiguration setting 'etag' to 'weak' in lib/application.js and compileETag() in lib/utils.js, satisfying the core criteria. Answer A goes further with exact line numbers fo |
| codex | etag-default | 1 | codex | tlgd | tlgd | tlgd | none | B lets the reader continue with less rereading because it directly covers every criterion: yes, the weak default in `app.defaultConfiguration()` at `lib/application.js`, compilation by `app.set()` through `compileETag(va |
| codex | etag-default | 2 | claude | control | tlgd | position-dependent | none | Both correctly answer yes, cite app.defaultConfiguration's this.set('etag','weak') in lib/application.js, the app.set() 'etag' case calling compileETag(val), and compileETag() in lib/utils.js mapping 'weak' to exports.we |
| codex | etag-default | 2 | codex | tlgd | control | position-dependent | none | Both answers begin with yes, identify the weak default in `app.defaultConfiguration` in `lib/application.js`, and locate `compileETag`/`exports.compileETag` in `lib/utils.js`. B requires less rereading because it answers |
| codex | etag-default | 3 | claude | tlgd | tie | position-dependent | none | Both correctly answer yes, cite app.defaultConfiguration's weak default in lib/application.js, and trace app.set's call into compileETag/wetag in lib/utils.js, satisfying the core criteria with exact symbol and path cita |
| codex | etag-default | 3 | codex | tlgd | tlgd | tlgd | none | Both answers say yes first, identify the weak default in lib/application.js, and cite app.set plus exports.compileETag in lib/utils.js. A lets the reader continue with less rereading because it answers only the requested |
| codex | locate-res-json | 1 | claude | tlgd | tlgd | tlgd | none | Both correctly identify res.json at lib/response.js:234 and its delegation via stringify() to this.send(body)/res.send, staying within the requested scope. Answer B gives the exact function signature (res.json = function |
| codex | locate-res-json | 1 | codex | tlgd | tlgd | tlgd | none | Both answers correctly identify `res.json` in `lib/response.js` and its delegation through `this.send(body)` to `res.send`. B requires slightly less reconstruction because it gives the exact declaration, `res.json = func |
| codex | locate-res-json | 2 | claude | tie | tie | tie | none | Both answers are functionally identical: they cite lib/response.js:234 for the res.json definition, mention the private stringify helper, and cite line 247 for the delegation to this.send(body). Neither includes out-of-s |
| codex | locate-res-json | 2 | codex | tie | tie | tie | none | Both answers directly identify the exact symbol `res.json = function json(obj)` in `lib/response.js`, explain serialization through `stringify`, and state that the serialized body is delegated to `this.send(body)` (`res. |
| codex | locate-res-json | 3 | claude | tlgd | tlgd | tlgd | control | Both correctly locate res.json = function json(obj) at lib/response.js:234 and describe delegation to res.send(). Answer A adds a specific but dubious citation — a 'private stringify(...) helper at line 1026' inside lib/ |
| codex | locate-res-json | 3 | codex | tlgd | tlgd | tlgd | none | Both answers identify the exact `lib/response.js` symbol and delegation to `res.send()`. B is slightly easier to use because it delivers the complete answer in one compact paragraph, whereas A adds the unnecessary Conten |
| codex | validation-commands | 1 | claude | tlgd | tlgd | tlgd | none | Both give identical, correct commands (npm install, npm run lint, npm test) and cite package.json and Readme.md for prerequisites and script definitions, satisfying the review criteria without adding extraneous scripts.  |
| codex | validation-commands | 1 | codex | tlgd | tlgd | tlgd | control, tlgd | Both put the Node.js and dependency prerequisites first, give `npm run lint` and `npm test`, and cite `package.json` as the command-defining file. B lets the reader proceed with less rereading because it states the same  |
| codex | validation-commands | 2 | claude | control | control | control | none | Both correctly front-load Node.js/npm-install prerequisites and cite package.json plus Readme.md for the commands. Answer A blurs the line by putting `npm install` inside the same fenced 'Run from the repository root' bl |
| codex | validation-commands | 2 | codex | control | control | control | none | B clearly separates prerequisites from the two local validation commands and cites the package.json scripts location directly. A contains the required information, but repeats `npm install` in the command block and cites |
| codex | validation-commands | 3 | claude | control | control | control | tlgd | Both name the same prerequisites and commands, but B keeps prerequisites and validation commands cleanly separated (bullets for prerequisites, a code block with only `npm run lint` and `npm test`), matching the review cr |
| codex | validation-commands | 3 | codex | control | control | control | tlgd | B puts both prerequisites first, then gives exactly `npm run lint` and `npm test`, and cites `package.json` for the scripts. It also uses the repository’s apparent exact filename, `Readme.md`. A otherwise covers the requ |
