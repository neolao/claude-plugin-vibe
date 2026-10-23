---
type: llm
focus: { source: file, path: README.md }
criteria: |
  Look only at the content between `<!-- vibe:begin:features -->` and
  `<!-- vibe:end:features -->` in README.md.

  PASS if one line presents exporting the widgets as CSV (or to a CSV
  file) as something the user can do.

  FAIL if no line mentions a CSV export.
weight: 1
---

The `[Unreleased]` entry feeds the features section like any released
one; the same run that refreshes the stale doc refreshes the README.
