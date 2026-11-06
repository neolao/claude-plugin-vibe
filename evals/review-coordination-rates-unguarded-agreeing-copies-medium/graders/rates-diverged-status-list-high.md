---
type: llm
focus: last_message
criteria: |
  fixtures/orders/status.py defines `STATUSES = ("pending", "paid",
  "shipped", "cancelled")` and lets an order move to "cancelled";
  fixtures/reports/export.py defines `STATUS_LABELS` with only "pending",
  "paid" and "shipped" and indexes it with `STATUS_LABELS[order.status]`
  for every order of the daily export. The two lists already differ: a
  cancelled order makes the export raise KeyError.

  PASS if the reported findings include a finding on that status list
  (anchored on fixtures/reports/export.py or fixtures/orders/status.py, in
  category `Duplicated case list` or `Parallel table`, or a clearly
  equivalent name) with SEVERITY `high` whose ISSUE names the missing
  "cancelled" entry or the KeyError / crash of the export.
  FAIL if no finding names the two lists, if that finding carries SEVERITY
  `medium` or `low`, or if it never says the copies already differ.
weight: 2
---

Rates copies that already diverge, with a wrong result traced on a
realistic path (every cancelled order breaks the daily export), at `high`.
