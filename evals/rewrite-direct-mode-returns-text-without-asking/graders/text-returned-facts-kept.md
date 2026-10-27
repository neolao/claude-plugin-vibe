---
type: llm
focus: last_message
criteria: |
  The original paragraph, for comparison: "Implementation of the export of
  the monthly report in CSV format has been completed by the addition of a
  dedicated module, the invocation of which is performed by the admin page,
  with the sorting of the lines by ascending date being carried out prior to
  serialization. Verification of the behaviour was conducted through the
  execution of the test suite, with a passing result for all four tests, and
  through a manual download from a locally-run instance. There is no
  modification of the signature of the function that the admin page calls."
  Passages the skill left in the original wording (its closing block names
  them) are fine, as is a reply that lists questions to the author or a
  closing block after the paragraph.

  The reply must contain the rewritten paragraph as running prose — not a
  before/after table, not a list of proposed changes, not a description of
  what the text will say.

  PASS if the rewritten paragraph is present as prose and keeps every fact
  of the original: CSV export of the monthly report; a dedicated module
  called by the admin page; lines sorted by ascending date before
  serialization; four tests passing; a manual download from a locally-run
  instance; the signature of the function called by the admin page is
  unchanged. Rewording ("sorted oldest first", "we downloaded it from a
  local instance") is fine; a dropped fact, a new causal link ("so", "which
  means") the original did not state, or a hedge removed is a FAIL.
  FAIL also if the main output is a table or a change list instead of the
  paragraph.
weight: 3
---

Direct mode returns the text, and the text says exactly what the original
said.
