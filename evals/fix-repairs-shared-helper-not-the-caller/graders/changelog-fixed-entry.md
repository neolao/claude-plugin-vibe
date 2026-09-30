---
type: llm
focus: last_message
criteria: |
  The final report must state the changelog entry it added, filed under a
  "Fixed" section, describing the user-visible impact (a price such as 1.005
  being rounded to the wrong cent, or half-cent amounts rounding down instead
  of to the nearest cent) rather than the implementation detail (the
  `Number.EPSILON` term, the function name `roundCents`, or a file name).

  PASS if the report quotes or clearly paraphrases such an entry under
  "Fixed". FAIL if no changelog entry is mentioned, if it is filed under
  another section, or if it only describes the code-level change.
weight: 1
---

Confirms a `### Fixed` CHANGELOG entry describing user-visible impact, per
the skill's own CHANGELOG and report requirements.
