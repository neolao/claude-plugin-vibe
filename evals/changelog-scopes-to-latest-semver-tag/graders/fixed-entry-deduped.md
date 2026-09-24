---
type: llm
focus: { source: file, path: "CHANGELOG.md" }
criteria: |
  Look only at the `## [Unreleased]` section.
  Before the run it held one entry under `### Fixed`: "Search no longer
  returns empty results when the query ends with a space". A commit
  `fix(search): return results for queries with trailing whitespace` then
  landed; it describes the same fix in other words.
  PASS if `[Unreleased]` contains exactly one entry about search queries
  ending with a space or trailing whitespace, and it is still under
  `### Fixed` (rewording it is fine).
  FAIL if there are two or more such entries in any category, or none.
weight: 2
---

The fix is already written up under `[Unreleased]` with different wording,
so the skill must see that the entry covers the commit and skip it.
