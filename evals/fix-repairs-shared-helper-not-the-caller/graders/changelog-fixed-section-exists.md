---
type: regex
target:
  source: file
  path: CHANGELOG.md
pattern: "###\\s*Fixed\\n(?:.*\\n)*?-\\s+.+"
flags: i
weight: 2
---

Deterministic check on the actual file (not the model's narrative): a
`### Fixed` section exists under `[Unreleased]` with at least one bullet
entry. Complements `changelog-fixed-entry` (an `llm` grader judging the
entry's wording) with a direct read of `CHANGELOG.md` itself.
