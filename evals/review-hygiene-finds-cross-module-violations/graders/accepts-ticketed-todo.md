---
type: llm
focus: last_message
criteria: |
  FAIL if any finding flags the `# TODO(#142): support refunds that span
  several order lines` comment in fixtures/billing/refunds.py as a stale
  marker (or any other hygiene defect). That TODO carries an issue
  reference, which is what the agent's `Stale marker` rule asks for.
  A finding on the other marker in the same function (the `FIXME`) does not
  count against this grader, and neither does a report that mentions the
  TODO only to say it is fine.
  PASS otherwise, including when the report has no finding at all.
weight: 1
---

Does not flag the ticketed `TODO(#142)` in fixtures/billing/refunds.py.
