---
type: llm
focus: last_message
criteria: |
  The sub-agent's `**Findings handled:**` section must account for both
  findings of the prompt.

  PASS if the section names the `high` finding as fixed and the `low`
  finding as left unfixed (not handled, skipped or deferred, in any wording).
  FAIL if either finding is missing, if the section says `none`, or if the
  `low` finding is reported as fixed.
weight: 1
---

The report says what was done with each finding.
