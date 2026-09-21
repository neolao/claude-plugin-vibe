---
type: llm
focus: last_message
criteria: |
  The skill's Step 6-8 requires a CHANGELOG entry under `### Fixed`, written
  for user-visible impact ("Fixed crash when submitting an empty form", not
  "Fixed null check in handleSubmit()"), and Step 9's report must state that
  changelog entry text.

  PASS if the final report quotes or clearly paraphrases a changelog entry,
  filed under a "Fixed" section, describing the user-visible impact (getting
  the correct largest number back for a list of negative numbers) rather
  than the implementation detail (the accumulator's initial value, the
  variable name `largest`, or the file name).
  FAIL if no changelog entry is mentioned, if it is filed under the wrong
  section, or if it only describes the code-level change.
weight: 1
---

Confirms a `### Fixed` CHANGELOG entry was made, describing user-visible
impact rather than implementation, per the skill's own CHANGELOG and report
requirements.
