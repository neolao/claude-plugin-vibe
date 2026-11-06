---
type: llm
focus: last_message
criteria: |
  No `.vibe/decisions/` directory exists, no `CLAUDE.md` is present, no
  module `Role:` names ports or adapters, and the tree has `controllers/`,
  `services/` and `repositories/` — no `ports/`, `adapters/`, `driving/`
  or `driven/`. The project built no hexagon.

  PASS if no finding of any severity carries a `Port ownership`, `Leaky
  port`, `Adapter purity`, `Core purity` or `Wiring` category (or a clearly
  equivalent name), and no finding asks for a port, an adapter or a
  composition root to be introduced. A report with no findings at all
  passes.
  FAIL if any ports & adapters finding is reported, at any severity.
weight: 2
---

Imposes no hexagon on a layered project that never built one.
