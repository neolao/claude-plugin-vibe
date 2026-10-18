---
type: llm
focus: last_message
criteria: |
  The report is for a Product Owner. The workflow says: never a finding, an
  agent name or a file name in it.

  PASS if the report names no `review-*` agent, no `findings-classifier`,
  no `requirements-reviewer`, and no source file (`stats.js`,
  `stats.test.js`); describing *what the code now does* (medians skip
  missing readings) is fine. The extra line about the number of rounds asked
  by the prompt sits after the report and is not judged.
  FAIL if the report leaks an agent name, a finding, or a file name.
weight: 1
---

Findings stay inside the loop; the Product Owner reads outcomes.
