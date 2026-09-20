---
type: llm
focus: last_message
criteria: |
  The fixture already follows a sound design for each principle: channel
  senders are added to a `NOTIFIERS` registry instead of an `if`/`elif` chain
  (open for extension), `UserContact` is a small dataclass whose fields are
  all read by `format_greeting`, and `OrderProcessor` takes its
  `PaymentGateway` as a constructor-injected `Protocol` rather than
  constructing a concrete client itself.

  PASS if the response reports no `high` or `medium` severity S, O, L, I, or D
  finding on this code — either no findings at all, or only `low` severity
  style notes unrelated to these patterns.
  FAIL if it flags the registry-based dispatch as an OCP violation, the
  dataclass as an ISP violation, the constructor-injected gateway as a DIP
  violation, or invents any other SOLID violation on this code.
weight: 2
---

Does not invent SOLID findings on code that already follows a sound pattern
for each principle.
