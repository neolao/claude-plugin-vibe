---
type: llm
focus: { source: file, path: "CHANGELOG.md" }
criteria: |
  Look only at the `## [Unreleased]` section.
  A `wip:` commit started a PDF export and a later `feat:` commit finished
  it; nothing was written under `[Unreleased]` before the run.
  PASS if `[Unreleased]` holds exactly one entry whose subject is the PDF
  export, and it is under `### Added`.
  FAIL if there is no PDF export entry, if there are two or more (one per
  commit, or one Added and one elsewhere), or if the only one is not under
  `### Added`.
weight: 3
---

The finished feature is announced once: the wip is noise, the feat is the
change.
