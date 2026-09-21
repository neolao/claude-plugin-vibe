---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "off-by-one"
flags: i
match: count:1
weight: 3
---

Precision check — the most important grader in this case. `[Unreleased]`
already had a hand-written `### Fixed` entry for the off-by-one pagination
bug before the `fix:` commit landed. The commit describes the exact same
fix, so the skill must recognize it as already covered and skip it — the
phrase must appear exactly once in the whole file, not zero times (entry
dropped) and not twice (duplicated).
