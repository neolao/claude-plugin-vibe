---
type: llm
focus: last_message
criteria: |
  `MAX_ATTACHMENTS = 5` in fixtures/tickets/limits.py is written again as
  the literal `5` (twice) in `validate_upload` of
  fixtures/web/upload_form.py, under a `# keep in sync with
  tickets/limits.py` comment. The two agree today; nothing imports one
  from the other and no test compares them.

  PASS if the reported findings include a finding on that limit (category
  `Copied constant` or `Confessed coordination`, or a clearly equivalent
  name) naming both files, with SEVERITY `medium`.
  FAIL if no finding names the two copies of the attachment limit, or if
  the finding carries SEVERITY `low` or `high`.
weight: 2
---

Reports the confessed copy at `medium`: the "keep in sync" comment is the
confession, not a guard, and does not lower the rating; the copies agree
today, so `high` is wrong.
