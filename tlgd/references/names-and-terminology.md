# Names, examples, jargon, and preferred terms

## Product names and trademarks

- Follow the owner's official spelling and capitalization for every company, product, service, feature, open source term, and brand.
- Use full product names. Shorten one only when established project guidance or a UI label requires it and the reference remains unambiguous.
- Feature names are usually lowercase unless officially capitalized or quoted from a UI label.
- Do not put **the** before a product name. Do use **the** before a named tool, API, console, or a product name that modifies another noun: **the Transcoder API**, **the gcloud CLI**, **the Google Cloud console**.
- Do not use a product, feature, abbreviation, file type, protocol, or trademark as a verb.
- Avoid possessives and plurals for product and trademark names. Use the name as a modifier or add a descriptive noun.
- When formal trademark rules apply, use a trademark only as a modifier of a generic noun and follow the owner's marking and attribution guidance.

## Use safe and inclusive example data

- Never use real domains, emails, phone numbers, people, customer data, credentials, project identifiers, or street addresses.
- Use `example.com`, `example.org`, or `example.net` for generic domains and an address such as `dana@example.com` for email.
- Use documentation-reserved IPv4 ranges `192.0.2.0/24`, `198.51.100.0/24`, and `203.0.113.0/24`; use `2001:db8::/32` for IPv6.
- Use the reserved example phone range `800-555-0100` through `800-555-0199`, with nonbreaking hyphens between the groups.
- Use **Example Organization** for a company. Choose meaningful project names and placeholders rather than **foo**, **bar**, **test1**, or realistic customer names.
- Use diverse given names and a surname initial where needed. Use singular **they**, avoid a gender binary, and do not map demographic groups to stereotyped roles.
- Use a fully opaque overlay to remove PII from screenshots. Never rely on blur or pixelation.

## Decide whether to use jargon

- First try to write around jargon or replace it with a precise ordinary term.
- Keep established jargon when the intended audience understands it or searches for it, but define or link it on first use.
- If a jargon term appears in code, preserve the literal code and introduce an inclusive plain-language term around it.
- Apply **Avoid** as a caution: use the term only when it is clearest and define it where useful. Apply **Don't use** as a strong preference to replace or write around the term.

## High-frequency word choices

| Avoid or do not use | Prefer |
| --- | --- |
| access as a vague verb | view, edit, find, use, or a precise action |
| actionable | useful, or state the action |
| aka | also known as, or parentheses |
| and/or | and, or, or **or both** |
| as or since for causation | because |
| blacklist, whitelist, graylist | a domain-specific term such as blocklist and allowlist |
| blind change or blind write | state that no check or read occurs first |
| click here, learn more | descriptive link text |
| CLI as a generic noun | the specific interface name |
| comprised of | consists of, contains, or includes |
| config in prose | configuration; preserve literal code names |
| crippled, crazy, dummy, lame | precise non-figurative behavior |
| deselect or uncheck a checkbox | clear |
| disabled for something broken | unavailable, not responding, or the precise fault |
| easy, simply, obviously | omit the judgment and give the needed information |
| e.g. or i.e. | for example or that is |
| grandfathered | legacy, exempt, or made an exception |
| hang for an unresponsive system | stop responding or not responding |
| hamburger icon, kebab, zippy | the accessible icon name or label |
| he/she or a generic gendered pronoun | singular they |
| hover | hold the pointer over |
| in order to | to |
| leverage meaning use | use, build on, or take advantage of |
| master/slave | precise roles such as primary/replica, controller/worker |
| mobile as a noun | mobile phone or mobile device |
| native for a person | the person's preferred identity or origin term |
| please or please note | direct instruction or statement |
| possible meaning allowed | can |
| sane or sanity check | valid, sensible, quick check, or confidence check |
| screenshot as a verb | take a screenshot |
| spin up | create or start |
| SSH as a verb | connect by using SSH |
| target as a verb for people | attract, serve, or appeal to |
| touch for activation | tap on a touch device |
| type when input method is irrelevant | enter |
| unarchive, uncompress, unzip, untar | extract |
| utilize meaning use | use |
| vs. | versus |
| we for the reader | you |

## Resolve an unlisted term

1. Check project usage and authoritative product documentation.
2. Check the live Google developer documentation word list, including product-scoped annotations.
3. Use the first Merriam-Webster spelling when more than one spelling is listed.
4. Choose the term that is clearest for the audience and use it consistently.
