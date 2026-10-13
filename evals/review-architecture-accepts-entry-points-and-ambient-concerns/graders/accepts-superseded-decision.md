---
type: llm
focus: last_message
criteria: |
  `.vibe/decisions/003-prices-as-float-units.md` has `status: superseded`. The code prices in integer cents, which contradicts it.

  PASS if no Decision violated finding cites `003-prices-as-float-units.md` at any severity.
  FAIL if it is reported at high or medium severity.
weight: 1
---

Does not enforce a superseded decision.
