# Markup and source formatting

## Choose the project format

- Use the markup language, template, and conventions already established by the project.
- Prefer Markdown when its source readability is sufficient. Use HTML when semantic tagging or a required effect is unavailable in the project's Markdown dialect.
- Do not convert an existing document between Markdown and HTML merely for preference.

## Use semantic HTML

- Use elements for their intended meaning and CSS for visual presentation.
- Use headings only for hierarchy, not to enlarge text. Do not use tables or frames for page layout.
- Use `em` for semantic emphasis and `i` for non-emphasis italics, such as a term or title.
- Use `strong` for strong importance and `b` for attention without added importance, such as a UI label.
- Use `cite` for the title of a standalone work where appropriate.
- Use `p` for paragraphs. Use `br` only for a line break that is intrinsically part of the content, such as in an address—not for spacing.
- Prefer native controls and structural elements over custom widgets and presentational substitutes.

## Format source consistently

- Follow the project's formatter first. Otherwise, for HTML-like documentation source, use spaces rather than tabs and two spaces per indentation level.
- Use lowercase HTML elements and attributes. Remove trailing spaces except where the Markdown dialect uses them intentionally.
- Aim for an 80-character source line when the break is safe. Do not break a URL or required one-line metadata.
- Put a long URL in an attribute on its own source line when that improves reviewability without breaking the link.
- Wrap code at 80 characters only when the language permits it and behavior is unchanged. Preserve a legacy file's consistent line length during a small edit instead of reformatting the whole file.

## Preserve accessibility in markup

- Keep heading levels in logical order and give each page one `h1`.
- Give form fields labels, images alt attributes, data tables true headers, and menu separators accessible text.
- Keep the DOM order consistent with the visual and reading order.
- Do not use inline font changes, color, or layout to replace semantic meaning.
