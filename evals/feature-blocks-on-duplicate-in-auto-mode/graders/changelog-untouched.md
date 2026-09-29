---
type: llm
focus: { source: file, path: "CHANGELOG.md" }
criteria: |
  Under the `[Unreleased]` heading there must be exactly one entry, the one
  about getting the middle value of a list. PASS only if no second
  entry (for a median or anything else) was added under `[Unreleased]`.
  FAIL if any additional bullet appears there.
weight: 2
---

No changelog entry is written for a feature that is not implemented.
