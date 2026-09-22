# Code, command-line content, filenames, and API references

## Format code in prose

- Use code font for text entered verbatim and for code-related entities, including attributes, classes, methods, functions, command-line tools, commands, data types, database elements, enum values, environment variables, filenames, paths, folders, headers and content types, HTTP verbs and status codes, IP addresses and ports, language keywords, namespaces, package names, permissions, queries, resource IDs, literal values, and placeholders.
- Do not use code font for ordinary product names or a URL that the reader navigates to in a browser. Preserve project conventions for domain names and email addresses.
- Add a grammatical noun when it clarifies the item: **the `POST` request**, **the `config.yaml` file**, **the `500` status code**.
- Do not form a possessive directly from a code item. Attach the possessive to its descriptive noun or rewrite.
- Preserve exact spelling, capitalization, punctuation, and syntax.

## Present code samples

- Follow the language's project-specific or Google code style. Do not reformat valid code merely to match prose style.
- Use spaces or tabs and indentation according to that language. Wrap near 80 characters only when the break preserves meaning and copy-paste validity.
- Use a fenced block in Markdown or `pre` in HTML. Apply a language identifier when the renderer supports syntax highlighting.
- Introduce every sample with a complete sentence. Use a colon when the sample immediately follows and a period when material intervenes.
- Show the smallest complete sample that teaches the point. Include necessary imports, setup, error handling, or context without unrelated boilerplate.
- Indicate omitted code with a valid comment in the sample language, not an ellipsis. Do not mark an incomplete sample as click-to-copy.

## Document commands

- Link to the command reference and use the fewest options required for the recommended common case.
- Prefer a runnable click-to-copy command that needs no edits except clearly marked placeholder substitution.
- Use a fenced block for a command. If a command exceeds the line limit, break only where its syntax permits, end continued lines with the correct continuation character, and indent continuations by four spaces.
- Do not show a current-directory path in the prompt. A prompt is optional for one line; use it consistently when a page mixes one-line and multiline sessions.
- Separate input and output into different blocks. Introduce output with **The output is similar to the following:** or **The output is the following:**.
- In sample output, put `...` on its own line for omitted lines; do not use the ellipsis character.
- In syntax reference, use `[OPTION]` for optional arguments, `{A|B}` for a required exclusive choice, and `VALUE...` for a repeatable argument.
- Never leave optional, mutually exclusive, or repeat markers in a click-to-copy procedure command. Show the runnable common case and, when the optional behavior matters, provide a separate runnable variant, task, tab, or prose explanation. Reserve `[OPTION]`, `{A|B}`, and `VALUE...` for syntax reference.
- Describe what a Linux or CLI command does instead of overexplaining the names of its syntactic parts.

## Format and explain placeholders

- Use descriptive uppercase names separated by underscores: `PROJECT_ID`. Do not use generic `x`, possessive adjectives such as `MY_`, or inconsistent casing.
- In HTML, use `var`; in Markdown prose, use italicized code when supported. Inside a fenced code block, retain plain uppercase placeholder text.
- Explain a placeholder at first use. For one placeholder, write **Replace `PLACEHOLDER` with DESCRIPTION.**
- For multiple placeholders, introduce **Replace the following:** and list them in command order. After each placeholder and colon, begin the description with lowercase and punctuate it according to list rules.
- Explain placeholders in output after the output block under **This output includes the following values:**.
- Repeat explanations on a long, non-linear page when readers might enter at different points.

## Write API reference comments

- Document every public class, interface, struct, constant, field, enum, typedef, method, parameter, return value, and thrown exception.
- Put API names and literals in code font and link names to their reference pages when possible.
- At the top of a type page, provide a concise purpose statement, a short representative sample, usage guidance, key features, and important constraints or best practices.
- Do not repeat the class name or begin **This class does...**. Use present tense.
- Describe a method by what it does: **Adds**, **Creates**, **Gets**, **Checks whether**, **Returns**, or another precise third-person verb.
- Capitalize parameter descriptions and end each description or phrase with a period.
- For a non-Boolean parameter, start with **The** or **A** when natural. For an action Boolean, explain both true and false behavior; for a state Boolean, use **True if...; false otherwise.** In these Boolean descriptions, do not put the words **true** and **false** in code font or quotation marks.
- Explain behavior by range and state the default with **Default:**.
- Begin a non-Boolean return description with **The**. For a Boolean return, use **True if...; false otherwise.** End return and exception descriptions with appropriate punctuation.
- Describe exceptions consistently, such as **If...** or **Thrown when...**, according to the generator's conventions.
- A deprecation notice must state the replacement, migration action, and version where relevant. Do not use *deprecated* to mean removed or unavailable.

## Refer to files

- In prose, put an exact filename in code font and follow it with **file**. Refer to a type by its formal name: **a PNG file**, not **a `.png` file**.
- Do not turn a file type into a verb. Write **Extract the ZIP file**, not **Unzip the file**.
- For new documentation filenames, prefer lowercase ASCII and hyphens, but follow an established directory convention rather than creating inconsistency.
