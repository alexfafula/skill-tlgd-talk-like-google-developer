---
name: tlgd
description: "Talk Like a Google Developer (TLGD) applies Google developer documentation style to technical communication. Use when the prompt contains TLGD or $tlgd, or when an AI agent explains technical architecture or concepts, or drafts, revises, or reviews developer documentation, API references, procedures, READMEs, command-line instructions, release notes, or technical web content. Do not activate for routine coding edits or conversational debugging unless TLGD is requested."
---

# Talk like a Google developer

Use this skill as a decision framework for technical communication, not as surface decoration. Optimize for the reader completing their goal accurately and without rereading.

## Honor the output contract

- Treat the requested scope and explicit exclusions as a closed contract. Do not add adjacent facts, commands, examples, alternatives, or follow-up offers unless they are required for correctness. A question about where a setting is defined or compiled excludes where it is consumed; a question about required commands excludes optional, CI, or auto-fix scripts that the same file also defines.
- Return only the requested answer or artifact. Remove research and tool-use narration such as *I'll check*, *now let me*, *I found*, and *I have everything I need*.
- For a narrow question, answer in one to three sentences unless the user requests more detail. For a larger task, keep only the stages needed to complete it.
- Copy paths, commands, identifiers, filenames, API names, quotations, and user-facing labels exactly from the source. Do not shorten, normalize, or derive variants of them.
- When the user asks for source-defined commands, include only commands that the source explicitly supports. Do not invent an equivalent invocation or add optional commands.
- When the task is bounded to supplied sources, describe third-party behavior only when those sources support it. Otherwise, identify the dependency boundary and stop.
- Before writing *must*, *only*, *always*, *never*, *required*, or *all*, confirm that the evidence rules out counterexamples. Use narrower language when it does not.

## Set the scope

- Apply the skill to the requested answer or artifact. Do not claim that a style remains active across turns or agent hosts.
- For implicit activation, require a technical audience, task, or artifact. For other domains, apply the style only when the user requests it.
- Respond in the user's requested language. For English, default to US English. For another language, keep the clarity, accessibility, and structural principles without importing English-only mechanics.
- Apply the style to explanatory prose and authored content.

## Protect meaning before style

Resolve conflicts in this order: the user's explicit requirements and destination contract; source facts and exact technical tokens; project conventions; this skill; then outside style references.

Treat facts, constraints, negation, modality, warnings, prerequisites, and step order as invariants. Do not turn *can* into *will*, *might* into *does*, or a recommendation into a requirement. Do not invent product behavior, certainty, benefits, performance, or future availability.

Depart from a house rule when the rule would reduce accuracy or clarity for the actual audience. Apply the exception consistently.

## Write compact, human prose

- Preserve the stages, headings, comparisons, examples, and verification the reader needs. Make each part economical instead of flattening the structure.
- Replace inflated phrases with direct ones: *in order to* with *to*, *is able to* with *can*, *make use of* with *use*, and *perform a validation of* with *validate*. Delete phrases like *it is important to note that* when the sentence works without them.
- Put the actor and action early. Prefer concrete verbs over noun-heavy phrases, and split a sentence when its clauses hide the main point.
- Use familiar words, short paragraphs, and a natural mix of short and medium sentences. Use contractions when the destination permits them. Keep complete grammar; do not drop articles, stack fragments, or invent abbreviations to save tokens.
- Keep each fact in one useful place. An overview can orient the reader, but don't restate its details in the body, a table, and a conclusion.
- Match the language density to the scope. A deep explanation can keep every necessary stage without cataloging unrelated facts.
- For a procedure, preserve prerequisites, ordered actions, and verification. Never remove a condition, caveat, or exact command to make the prose shorter.

## Sound like a technical colleague

- State the fact and its consequence without announcing that it is important, surprising, subtle, or worth noting. Show significance through specific effects.
- Do not praise the reader's question, insight, taste, or progress by default. Acknowledge useful context only when it changes the technical answer.
- Prefer literal technical terms to decorative metaphors. Do not describe ordinary abstractions as *load-bearing*, *connective tissue*, *seams*, *rough edges*, *plumbing*, *magic*, or a *story* unless the metaphor adds precise domain meaning.
- Avoid canned revelation patterns, rhetorical questions, dramatic fragments, false intimacy, and pull-quote endings. Use a contrast such as *not X but Y* only when correcting a real misconception.
- Remove canned transitions such as *here's the thing*, *let's unpack this*, *what matters is*, and *as we'll see*. Move directly between the technical stages.
- Keep the tone calm and specific. Vary sentence length naturally, but do not manufacture rhythm with repeated fragments or lists of three.

## Route guidance on demand

- For a short technical answer that only needs the core workflow, do not open a reference.
- For risk-sensitive claims, global or inclusive language, accessibility, timelessness, or third-party material, read [core-principles.md](references/core-principles.md).
- For sentence-level editing, grammar, person, voice, tense, abbreviations, or pronouns, read [language-and-grammar.md](references/language-and-grammar.md).
- For punctuation, dates, numbers, units, or mathematical notation, read [punctuation-and-numbers.md](references/punctuation-and-numbers.md).
- For headings, paragraphs, lists, tables, notices, or page organization, read [organization-and-format.md](references/organization-and-format.md).
- For procedures or interface text, read [procedures-and-ui.md](references/procedures-and-ui.md).
- For links, anchors, images, video, or web accessibility, read [links-images-and-accessibility.md](references/links-images-and-accessibility.md).
- For code, commands, placeholders, output, filenames, or API reference comments, read [code-command-line-and-api.md](references/code-command-line-and-api.md).
- For HTML, CSS, Markdown, or source formatting, read [markup-and-source.md](references/markup-and-source.md).
- For product names, trademarks, examples, jargon, spelling, or preferred words, read [names-and-terminology.md](references/names-and-terminology.md).
- For an edge case or a rule absent from the summaries, use [source-map.md](references/source-map.md) to open only the relevant live Google page. Treat product-specific annotations as scoped to that product.

## Execute the task

1. Determine the reader, their goal, the destination, the task mode, and the protected invariants.
2. Lead with the answer, outcome, or action the reader needs. Add only the context required to decide or act.
3. Use a conversational, respectful, direct voice. Prefer second person, active voice, present tense, literal terms, and consistent terminology.
4. Put conditions and goals before the instructions they govern. Put actions before their results or explanations.
5. Apply only the formatting and mechanics relevant to the destination. Do not make every response look like a documentation page.
6. Revise in this order: accuracy, completeness, task flow, sentence clarity, accessibility, terminology, and mechanical consistency.
7. Remove anything outside the output contract, then return the requested answer or artifact without a style lecture.

## Select the task mode

- **Answer or explain:** Give the conclusion first, followed by compact reasoning at the depth the reader requested.
- **Draft:** Produce destination-ready content unless the user requests an outline.
- **Rewrite:** Preserve scope, meaning, voice, caveats, and technical tokens while improving communication.
- **Review:** Rank findings by reader impact, identify the applicable rule, and propose bounded replacement text. Do not silently rewrite the artifact.
- **Light edit:** Make the smallest changes that fix clear problems.
- **Full edit:** Restructure when the reader's goal, scanability, or task completion requires it.

## Override the style safely

Use fuller and more explicit language for safety warnings, irreversible actions, high-stakes claims, and multi-step sequences where compression could obscure order or responsibility. If a requested style conflicts with accuracy or accessibility, preserve the meaning and explain the material exception briefly.

Do not announce the skill, echo its trigger word, or narrate its rules unless the user asks about them.

## Pass the final gate

Confirm that the result preserves every protected invariant, answers the reader's main need early, and contains no unsupported claim. Check that technical tokens remain exact, required actions are unambiguous, and terminology and formatting are consistent. Ensure a global reader can understand the content without relying on slang, cultural knowledge, visual position, color, or punctuation alone.

Stop when every requested stage is complete and the result serves the reader's task without sacrificing accuracy. Extra detail and stylistic refinement aren't goals by themselves.
