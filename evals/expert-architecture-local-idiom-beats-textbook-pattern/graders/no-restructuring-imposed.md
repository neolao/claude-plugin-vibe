---
type: llm
focus: last_message
criteria: |
  Nothing in the fixture is a hard defect: a flat package with three
  modules, no layers to cross, no decision to contradict, a few thousand
  rows per run. The expert's rule reserves the "stays a defect whatever the
  neighbours do" floor for a cycle, a reversed layer direction or a
  contradicted decision.

  PASS if the reply requires no change to the existing CSV and JSON
  functions or to `cli.py`'s selection code beyond adding the new entry,
  and names no restructuring as required: no layers or ports and adapters,
  no interface or base class, no package split, no migration of the two
  existing formats. Mentioning that a base class would become worth it at
  some stated later point (many more formats, formats with configuration)
  is fine.
  FAIL if the reply requires restructuring the existing formats or the
  selection code, imposes layers, an interface or a package split, or lists
  the flat layout or the dict as a risk to fix.
weight: 2
---

Imposes no restructuring on a flat, healthy package: the existing formats and
the selection code stay as they are.
