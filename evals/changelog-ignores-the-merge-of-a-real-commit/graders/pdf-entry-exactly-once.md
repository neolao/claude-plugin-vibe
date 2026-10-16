---
type: llm
focus: { source: file, path: "CHANGELOG.md" }
criteria: |
  Look only at the `## [Unreleased]` section.
  A branch with one `feat:` commit adding a PDF export was merged with a
  merge message that describes the same export.
  PASS if `[Unreleased]` holds exactly one entry whose subject is the PDF
  export, under `### Added`.
  FAIL if there is no PDF export entry, or two or more (one from the
  commit and one from the merge), or if the only one is not under
  `### Added`.
weight: 3
---

The commit is the change; the merge that brought it in is noise and adds
no second entry.
