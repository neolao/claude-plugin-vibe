---
type: llm
focus: last_message
criteria: |
  The final message reproduces the run's rounds first, so the closing
  report starts further down: its `CLARIFY-RESULT:` line must read
  `CLARIFY-RESULT: settled — mode: need`
  (the `partial` form is acceptable only if the Product Owner's answers
  were not given — they are given in this prompt, so expect `settled`).
  Under `### Decisions made`, every decision taken from the sources must
  carry a `(source: …)` citation pointing at the backlog item or at
  `.vibe/decisions/002` / `.vibe/index.md`. A decision marked `(default)`
  is not taken from a source and needs no citation.

  PASS if the mode line is present and each decision taken from the sources
  (format and columns, owner-only access) is cited that way.
  FAIL if the mode is missing from the result line, or if a decision taken
  from the sources carries no source.
weight: 2
---

A decision the skill gave itself is a claim: it carries its source so the
caller can have it checked.
