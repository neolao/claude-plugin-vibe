---
type: llm
focus: { source: file, path: "CHANGELOG.md" }
criteria: |
  Look only at the `## [Unreleased]` section. The CSV export and the
  pagination of the report list are already announced in the released
  `[1.0.0]` section; their commits are in the history because the
  repository has no tag.
  PASS if no entry under `[Unreleased]` has the CSV export or the
  pagination as its subject. A passing mention inside another entry (for
  example "PDF export, alongside the CSV export") is fine.
  FAIL if `[Unreleased]` re-announces the CSV export or the pagination as
  a new or changed feature.
weight: 3
---

With no tag, the range is the whole history: the only thing keeping the
released changes out of `[Unreleased]` is the released section that
already covers them.
