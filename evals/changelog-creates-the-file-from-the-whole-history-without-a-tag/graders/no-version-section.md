---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[\\d"
match: not_contains
weight: 2
---

Reading the whole history is not a reason to invent a release: this skill
never creates a version section, that is `/vibe:release`'s job.
