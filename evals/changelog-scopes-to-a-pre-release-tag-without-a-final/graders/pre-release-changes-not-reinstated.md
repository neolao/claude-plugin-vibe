---
type: llm
focus: { source: file, path: "CHANGELOG.md" }
criteria: |
  Look only at the `## [Unreleased]` section. The CSV export is announced
  in the `[1.3.0-rc.1]` section, and its commit is the one tagged
  v1.3.0-rc.1.
  PASS if no entry under `[Unreleased]` has the CSV export as its
  subject. A passing mention inside another entry (for example "PDF
  export, alongside the CSV export") is fine.
  FAIL if `[Unreleased]` announces the CSV export as a new or changed
  feature.
weight: 3
---

Skipping the pre-release tag because it is a pre-release would start the
range at v1.2.0 and bring the CSV export back: the tag is only skipped
when its final version is also tagged, and v1.3.0 is not.
