---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Fixed(?:(?!\\n##)[\\s\\S])*(empty|last page)"
flags: i
weight: 2
---

The one real change since the tag — the fix for an empty list's last page —
lands under `### Fixed` inside `[Unreleased]`. Dropping noise must not
drop the fix with it.
