# Links, images, and web accessibility

## Link selectively and descriptively

- Provide brief essential context on the page instead of forcing the reader to follow a link.
- Link to the most relevant page or heading. Avoid multiple links that do the same job and duplicate links to one destination unless distance or separate entry points justify them.
- Use the exact destination title or short, unique, descriptive link text. Put distinguishing words early.
- Never use **click here**, **here**, **this document**, **this link**, **learn more**, a bare URL, or the same text for different destinations.
- Include an abbreviation in link text when the link introduces it. If link text contains a command, format the command as code inside the link where supported.
- Explain why the link is relevant. For a standalone cross-reference, use **For more information, see...** or **For more information about X, see...**—not **on X**.
- Explain unexpected behavior such as a download, email action, same-page jump, or forced new tab. Do not force a new tab unless required.
- Put punctuation outside the link. Do not add quotation marks or italics around linked titles.
- Keep external links out of documentation navigation when possible and do not rely on an external-link icon.

## Preserve heading targets

- Prefer the publishing system's automatic heading anchors unless a stable or shorter custom target is useful.
- Use lowercase anchor text with hyphens between words.
- When revising a heading with an automatically generated anchor, preserve the old ID as a custom anchor so incoming links keep reaching the section.
- Before changing an existing custom anchor, locate and update links that depend on it. Remove a harmful term from an anchor when necessary even if preserving it would be convenient.

## Use images only when they add information

- Use a diagram for relationships or visual structure that prose cannot express efficiently. Use screenshots only for UI that readers need help locating or understanding.
- Never use an image of ordinary text, code, a command, or terminal output. Use copyable text.
- Prefer SVG for diagrams and PNG when SVG is unavailable. Use MP4 or another efficient video format instead of animated GIF.
- Crop to relevant content, use descriptive filenames, and never expose PII. Hide sensitive screenshot data with a fully opaque overlay and flatten layered exports.
- Do not use image maps. Provide ordinary text links after the image.
- Introduce an image in the surrounding prose and provide the context needed to interpret it.

## Write text alternatives and captions

- Give every `img` an `alt` attribute. Use `alt=""` only for a purely decorative image or an icon whose adjacent text supplies the same accessible name.
- Make alt text concise, contextual, and purpose-driven. Do not begin with **Image of** or repeat the caption.
- Use a sentence or noun phrase, punctuation, and generally no more than 155 characters. Put a longer explanation in nearby prose.
- Use the same alt text for repeated instances of the same control or state. Avoid all caps.
- Do not use a caption instead of alt text. Use complete sentences and end punctuation in captions when possible.
- If numbering figures, use **Figure NUMBER. DESCRIPTION**. Refer to the number, not **the image above**.
- Keep text inside diagrams brief and in sentence case. Put descriptions and captions outside the image.

## Make web content operable and perceivable

- Use native semantic elements and ensure every interactive control works with a keyboard.
- Give fields explicit labels outside the field. Write validation errors that identify the problem and the correction.
- Introduce tables and interactive elements before they appear. Use true headers, `scope`, and logical reading order; avoid merged cells.
- Do not communicate state only through color, icon, outline, motion, sound, or position. Add a text cue.
- Avoid flashing content, forced line breaks, unnecessary all caps, and custom controls when a native control works.
- Ensure the document still conveys its intended meaning without sound, images, color, mouse input, or punctuation, and under magnification.
- Use accessible contrast and keep DOM order aligned with visual reading order. Do not hide essential content from assistive technology.
- Provide captions or transcripts for audio and video when the format needs them.
