---
type: llm
focus: { source: file, path: "CHANGELOG.md" }
criteria: |
  Look only at the `## [Unreleased]` section. The CSV export commit was
  released in 1.10.0 and must not come back.
  PASS if no entry under `[Unreleased]` announces CSV export as a new or
  changed feature. A passing mention of CSV inside another entry (for
  example "PDF export, alongside the existing CSV export") is fine.
  FAIL if `[Unreleased]` has an entry whose subject is the CSV export.
weight: 2
---

The commit `feat: add CSV export for monthly reports` sits between `v1.9.0`
and `v1.10.0`. Only a range starting at `v1.9.0` picks it up, which is what a
lexical tag sort gives (`v1.9.0` sorts after `v1.10.0`).
