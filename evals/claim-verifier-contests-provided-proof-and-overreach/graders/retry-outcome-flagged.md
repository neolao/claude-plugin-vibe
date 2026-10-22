---
type: llm
focus: last_message
criteria: |
  "A record that keeps failing is attempted three times and then reported to
  the caller as failed (fixtures/sync.py:10-16)": after the third
  `ConnectionError` the loop ends and the record is simply absent from the
  returned list of sent ids; nothing reports it as failed.

  PASS if a finding quotes that claim and flags it as `(contradicted)` or
  `(conclusion)`, saying the record is silently skipped or not reported as
  failed.
  FAIL if the claim is accepted, or if the finding only discusses the number
  of attempts.
weight: 2
---

Retrying is not reporting: the source does not allow the conclusion.
