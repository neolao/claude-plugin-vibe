---
type: llm
focus: last_message
criteria: |
  `Money` is a frozen dataclass carrying its own currency and `OrderStatus`
  is an `Enum` — the standard remedies for primitive obsession and
  stringly-typed code, already applied.

  PASS if no `high` or `medium` severity Primitive obsession or
  Stringly-typed finding targets either.
  FAIL if either is flagged at high or medium severity.
weight: 1
---

Does not flag the remedies for primitive obsession as the anti-pattern.
