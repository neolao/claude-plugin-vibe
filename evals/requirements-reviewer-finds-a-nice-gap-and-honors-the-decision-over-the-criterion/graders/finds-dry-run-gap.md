---
type: llm
focus: last_message
criteria: |
  The framing's third decision, "**Dry run** (✨ NICE): `archive_old(ledger,
  today, dry_run=False)` reports what it would move without moving it", is
  not delivered: `archive_old` in fixtures/archive.py takes no `dry_run`
  parameter and always moves the rows.

  PASS if a `(gap)` finding quotes that decision (the dry-run flag, with
  its ✨ NICE priority visible in the quote) and says the flag is missing,
  with a fix (add the parameter and the early return).
  FAIL if the missing dry run is not reported as a gap, or if the finding
  presents the priority as a reason the gap does not count.
weight: 2
---

A ✨ NICE decision left out is a gap like any other; the classifier
weighs it.
