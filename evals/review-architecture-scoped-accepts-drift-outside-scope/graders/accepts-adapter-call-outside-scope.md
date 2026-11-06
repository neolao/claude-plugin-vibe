---
type: llm
focus: last_message
criteria: |
  fixtures/adapters/postgres_gateway.py calls `SmtpNotifier()` directly in
  its `save` method — adapter to adapter — but that file is outside the
  scope and no in-scope file takes part in the call.

  PASS if no finding of any severity reports the `SmtpNotifier` call of
  fixtures/adapters/postgres_gateway.py (as Adapter purity or any other
  category). A report with no findings at all passes.
  FAIL if it is reported.
weight: 1
---

Leaves an adapter-to-adapter call outside the scope to the full review.
