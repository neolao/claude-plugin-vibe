---
type: llm
focus: last_message
criteria: |
  fixtures/pricing/rules.py, fixtures/pricing/describe.py and
  fixtures/pricing/validate.py each hold an `if kind == ...` chain on the
  same discriminant (`percentage`, `fixed`, `bogo`), and
  fixtures/ROADMAP.md announces a fourth kind (tiered). A named design
  keeps compute, label and validation of one kind together and adds the
  fourth kind without editing the three chains.

  PASS if a finding anchored on one of the three pricing files proposes a
  Strategy registry keyed by data, a lookup table keyed by kind, or an
  equivalent named design (one entry per kind holding its rule, label and
  validation), and names at least one of the other two chains as evidence
  that the switch recurs.
  FAIL if no finding proposes such a design for the discount kinds, or if
  the finding names no second chain on the same discriminant.
weight: 2
---

Proposes a data-keyed registry for three parallel switches on the same
discriminant that are about to gain a fourth case.
