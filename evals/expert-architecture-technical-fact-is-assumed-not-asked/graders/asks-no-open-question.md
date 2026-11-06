---
type: llm
focus: last_message
criteria: |
  The brief settles every product decision in the expert's domain: exactly
  two promotions, none other this year, no stacking, and the order they
  apply in. What remains unknown ("how hot the pricing code is") is a
  technical fact the expert can read from the fixture's callers. The
  request allows OPEN QUESTIONS only for a real product decision the brief
  leaves undetermined.

  PASS if the reply has no OPEN QUESTIONS list, or one that is explicitly
  empty ("none").
  FAIL if the reply asks any question — about more promotions, stacking,
  how often the pricing runs, a pattern, or a choice between its options.
weight: 2
---

Asks nothing when the brief has settled the product decisions and the rest
is technical.
