---
type: llm
focus: last_message
criteria: |
  The skill's Step 6-8 requires a CHANGELOG entry under `### Added`, written
  for the end user ("Users can now export reports as CSV", not
  "Added exportToCsv()"), and Step 9's report must state that changelog
  entry text.

  PASS if the final report quotes or clearly paraphrases a changelog entry,
  filed under an "Added" section, describing the new sum capability in
  plain end-user language (no function/file/variable names).
  FAIL if no changelog entry is mentioned, if it is filed under the wrong
  section, or if it reads like an implementation note (e.g. names `sum()`
  or `stats.js`).
weight: 1
---

Confirms a `### Added` CHANGELOG entry was made and reported in end-user
language, per the skill's own CHANGELOG and report requirements.
