---
type: llm
focus: last_message
criteria: |
  The brief asks for a `sum` function over a list of numbers that raises a
  clear error on non-numeric input. The skill's own Step 3-5 requirement is
  that tests cover the nominal path, at least one edge case, and the error
  path.

  PASS if the final report's test-results description (Step 9 of
  skills/feature/SKILL.md: "test results (X passing, covering nominal / edge
  / error paths)") indicates the new/updated tests exercise:
  - a nominal case (summing a normal list of numbers), AND
  - at least one edge case (e.g. an empty list, a single-element list, or
    negative numbers), AND
  - the error path (a non-numeric value in the list raises an error).

  FAIL if any of the three is missing from the report, or if the report does
  not describe test coverage at all.
weight: 2
---

Reports test coverage across nominal, edge, and error paths for the new
`sum` function, per the skill's own Step 3-5 requirement.
