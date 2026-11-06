---
type: llm
focus: last_message
criteria: |
  Two other teams' nightly scripts `awk` the second column of the table
  `myctl backups list` prints today, in its three-year-old default order.
  Inserting SIZE between NAME and STATUS moves STATUS to the third column
  and silently breaks what those scripts read; flipping the default order
  changes which rows they see first.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS addresses the column order
  or the default order as a compatibility concern with a concrete means:
  the existing columns and order stay for an unchanged invocation and the
  new column or order comes through a flag (a `--sort`, a `--columns`, a
  machine-readable `--json` output the scripts are pointed at), or the
  reply names the nightly `awk` scripts as what the inserted column or the
  flipped default would break and requires them to keep working.
  FAIL if the reply inserts the SIZE column before STATUS or flips the
  default order as a plain requirement with no word on the scripts that
  parse the current table, or never mentions the existing scripts' parsing
  at all.
weight: 2
---

Treats the inserted column and the flipped default order as changes
existing scripts would feel, and keeps the nightly `awk` scripts' unchanged
invocation printing what it did.
