# Punctuation, dates, numbers, and units

## Punctuation

- Use US punctuation and the serial comma.
- Put a comma after an introductory word or phrase. Put a comma before a coordinating conjunction joining independent clauses unless both clauses are very short.
- Usually put a comma before **which** in a nonrestrictive clause. Do not put a comma before **because** unless the clause is nonrestrictive or ambiguity requires it.
- Use a colon to introduce closely related information only when the text before it can stand as a complete sentence. Usually begin the text after a colon with lowercase.
- Use an em dash—with no surrounding spaces—for a real interruption. Do not use an en dash. Use a colon, period, or description list rather than a dash between a label and its description.
- Avoid semicolons when a period is clearer. Use one between closely related independent clauses, before a conjunctive adverb joining clauses, or between complex series items containing internal punctuation.
- Avoid parentheses for important information. Keep a parenthetical short; otherwise, use a separate sentence. Do not put optional plurals in parentheses.
- Avoid ellipses in documentation. Omit unneeded text; in quoted omissions use three periods, not the single ellipsis character. Omit a UI label's trailing ellipsis unless doing so causes confusion.
- Use straight double quotation marks and apostrophes. Reserve single quotation marks for nested quotations or code syntax.
- Put commas and periods inside quotation marks under US style, except when quotes identify a literal string. Format literal strings as code instead of quoting them.
- End complete sentences with periods. Do not end headings with periods. Avoid exclamation marks in concept and reference docs and almost always in procedures.
- Avoid slashes for alternatives, dates, abbreviations, fractions, and rates. Use **and**, **or**, words, decimal notation, or **per**. Keep slashes in code, URLs, and paths.

## Hyphens

- Hyphenate only when convention or clarity requires it. Consult the word list for established compounds.
- Usually close a prefix to its base word. Hyphenate **self-**, **cross-**, before a capital or number, to prevent misreading, or before an already open or hyphenated term.
- Hyphenate a compound modifier before a noun when needed for clarity; avoid compounds longer than two words. Usually omit the hyphen after a verb and after an *-ly* adverb.
- Hyphenate a spelled-out number and unit used before a noun: **a 64-bit system**. Do not hyphenate an abbreviated unit: **a 200 GB disk**.
- Use a hyphen with no spaces for a simple numeric range: **8-20 files**. Use **from 8 to 20**, not **from 8-20**.

## Dates and times

- In prose, spell out the month and use a four-digit year: **January 19, 2017**. Put a comma after the year when the sentence continues.
- For a numeric-only date, use ISO order with hyphens: **2017-04-15**. Never use an ambiguous slash date.
- Put the date before the time: **May 4, 2009, at 6 PM**.
- Use a 12-hour clock unless the documented interface or system uses 24-hour time. Capitalize **AM** and **PM**, include a space, and omit `:00` for a round hour.
- Avoid time zones unless needed. Prefer the interface's timestamp; otherwise, spell out the region and include its UTC or GMT offset.
- Avoid seasons for global content. Use a month, quarter, or explicit temperature range.

## Numbers and measurements

- Spell out ordinal numbers. Generally spell out zero through nine and use numerals for 10 and greater, for a step number such as **step 3**, and for a small number that appears with a larger numeral in the same sentence.
- Use numerals for technical quantities, measurements, dimensions, percentages, decimals, negative values, versions, addresses, and ranges—even below 10.
- Spell out a number that begins a sentence or rewrite the sentence. Use Arabic rather than Roman numerals when possible.
- Use numerals and `%` with no intervening space: **40%**. Use US commas and decimal points.
- Prefer decimals, percentages, or true fraction characters to slash fractions. Keep the leading zero in a decimal below one: **0.75**. Hyphenate a spelled-out fraction.
- Use lowercase `x` with no spaces for dimensions: **192x192**.
- Add practical context or a visual when a numerical concept is difficult to interpret.

## Units, currency, and notation

- Put a nonbreaking space between a number and most units: `64&nbsp;GB`. Do not add a space before `%`, a currency symbol, or an angle degree symbol.
- Write temperatures with a nonbreaking space before the degree symbol and none after it: `50&nbsp;°C`, `50&nbsp;°F`, or `300&nbsp;K` for kelvin.
- In a measurement range, repeat the unit and use **to** when a hyphen could look like subtraction: **-40 °C to 85 °C**.
- Do not pluralize an abbreviated unit. Use the byte system the technology actually uses: MB is not MiB, and GB is not GiB.
- Identify ambiguous currencies, such as **US$10**. Use **per** for a rate when space permits.
- Italicize mathematical variables but not operators. Use semantic mathematical symbols or HTML entities, nonbreaking spaces around operators, `sup` for exponents, and `sub` for subscripts.
- Separate the groups of a phone number with nonbreaking hyphens: **415-555-0132**. Put `+` immediately before the country code of an international number: **+1-415-555-0132**. Write **extension**, not **ext.**, and use only the reserved fictitious range **800-555-0100** through **800-555-0199**.
