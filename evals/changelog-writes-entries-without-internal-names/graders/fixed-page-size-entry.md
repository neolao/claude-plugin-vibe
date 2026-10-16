---
type: llm
focus: { source: file, path: "CHANGELOG.md" }
criteria: |
  Look only at the `## [Unreleased]` section.
  A commit fixed an infinite loop when the report list is paginated with
  a page size of 0.
  PASS if `[Unreleased]` has a `### Fixed` entry that describes this
  problem in user terms — a page size of zero (or an empty/invalid page
  size) no longer hangs, loops or crashes pagination — without naming a
  function, a file or a parameter.
  FAIL if there is no such Fixed entry, if it is under another category,
  or if it names `paginate`, `pageSize` or a file path.
weight: 2
---

The `fix:` commit lands under `### Fixed`, described as the behaviour the
user no longer hits rather than as the guard added to the code.
