---
type: llm
focus: last_message
criteria: |
  PASS if the final report states the chosen/suggested version bump was
  `patch` (not `minor` or `major`), with reasoning tied to the `[Unreleased]`
  section of CHANGELOG.md containing only `Fixed` entries (no `Added`,
  `Removed`, or breaking changes).
  FAIL if the bump is reported as minor or major, or if `patch` is stated
  with no reasoning connecting it to the Fixed-only Unreleased entries.
weight: 2
---

Confirms the skill's own version-suggestion rule (Step 1: `patch` when only
`Fixed` entries are pending) was actually followed and explained, not just
guessed.
