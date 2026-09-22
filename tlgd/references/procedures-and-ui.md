# Procedures and user interfaces

## Write procedures

- State prerequisites, preparation, context, and required permissions before the steps.
- Introduce a procedure with a complete sentence when it adds context. Do not repeat the heading or make the steps complete a sentence fragment.
- Use a numbered list for multiple ordered steps. Format a one-step procedure as one bulleted sentence.
- Use lowercase letters for substeps and lowercase Roman numerals for sub-substeps. Punctuate a parent step like an introductory sentence.
- Begin the first sentence of every step with an imperative verb. Use one step for each substantial action or reader decision.
- Put context, location, condition, and goal before the action: **In the console, to create a key, click Add key.**
- Put the action before its immediate result or justification. Keep a short result in the same step; move extended explanation after the action.
- Mark an optional step with **Optional:** at the beginning, not with parentheses.
- Keep steps short, parallel, and in execution order. Limit interruptions and provide all information needed for executive planning before the reader starts.
- Prefer the shortest accessible method for the common case. Separate necessary alternatives under distinct headings or tabs.
- Avoid repeating a procedure. Link to the canonical procedure or refer to the earlier step when that is clearer.
- When a step contains a command, order the material as follows: action, command, placeholder explanations, essential details, representative output, and result.
- Introduce a command by its purpose, not with **Run the following command**.
- Include an instruction to press Enter when required. Do not add keyboard shortcuts to procedures unless the task or project specifically requires them.

## Focus UI instructions on goals

- Prefer an outcome such as **Refresh the page** when the widget or gesture does not help the reader.
- When mechanics matter, refer to a control by its visible or accessible label, not by color, shape, or location.
- Put every visible UI label in bold. Do not quote it or use code formatting unless it is also literal code.
- Preserve official wording. If a UI label is all capitals or labels are inconsistently capitalized, cite the label in sentence case unless capitalization carries meaning.
- Do not bold a product or feature name unless it is also the visible name of the element being referenced.
- Do not use a UI label as an English verb or noun. Write **Click Save**, not **Save the settings** when *Save* is a label.
- Omit a label's trailing ellipsis unless its absence could confuse the reader.

## Name controls precisely

- Use **page** for a web or console page, **window** for an application window, **dialog** for a detached smaller window, **pane** or **panel** for a rectangular region, and **section** for a labeled group of controls.
- Use **navigation menu**, not navigation bar or navigation pane. Use **command** for an item in a desktop menu.
- Refer to a button by its label without adding **button** when the context is clear: **Click OK**.
- For an icon button, use its accessible name or tooltip and include the icon only when useful. Do not use slang such as **hamburger**, **zippy**, or **expando**.
- For a hard-to-find control, give named context, use its accessible icon and label, or add a screenshot. Do not use directional language.
- Use **field** for Google Cloud and Google Workspace text entry controls; elsewhere use the product's established term.
- Use **select** and **clear** for checkboxes. Describe checkbox state as **selected** or **not selected**.
- Do not use **toggle** as a verb. Tell the reader to turn a setting on or off and state the required final position.

## Use consistent interaction verbs and prepositions

- Use **click** for mouse activation, **tap** for touch, **select** for options, **enter** for text, **press** for keys, **go to** for pages, and **turn on** or **turn off** for state.
- Prefer **enter** to **type** when text might also be pasted or dictated.
- Use **in** for dialogs, fields, lists, menus, panes, and windows. Use **on** for pages, tabs, and toolbars.
- For a menu path, bold the entire path and separate menu commands with `>`. In HTML, give each separator an accessible label such as **and then**.

## Format keyboard input

- Use `kbd` in HTML or monospace formatting elsewhere for keys and key combinations.
- Spell modifier names, capitalize letter keys, and use plus signs: `Control+S`, not `Ctrl+s`.
- When relevant to both platforms, give the Windows or Linux shortcut first and the macOS shortcut in parentheses.
- Use code formatting, not `kbd`, for a character that the reader enters as text.
