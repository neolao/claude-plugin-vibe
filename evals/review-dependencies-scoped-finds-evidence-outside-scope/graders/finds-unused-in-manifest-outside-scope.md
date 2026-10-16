---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/orders/; the manifest that
  governs it is fixtures/pyproject.toml, one level above the scope.
  PASS if the reported findings include an `Unused` finding on `tabulate`
  (declared in `[project] dependencies` of fixtures/pyproject.toml), noting
  that nothing in the repository imports it.
  FAIL if `tabulate` is not flagged as unused, or if the report says the
  manifest is out of scope and reviews nothing.
weight: 1
---

Reports the declared-but-never-imported `tabulate` as an Unused finding.
The manifest sits outside the path under review: an agent that stops at
the scope boundary never opens it and reports nothing.
