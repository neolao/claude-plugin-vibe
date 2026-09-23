---
type: regex
pattern: '## \[Unreleased\]\s*\n\s*### Fixed\s*\n\s*- Fix crash when loading a config file with no entries\.'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

`CHANGELOG.md`'s `[Unreleased]` section must still carry its pending entry,
untouched — the skill must stop before Step 3 (finalizing the changelog)
when the build fails, not cut the section into a dated release first.
