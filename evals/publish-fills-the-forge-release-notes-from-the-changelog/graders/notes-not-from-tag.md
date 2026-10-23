---
type: regex
target: { source: file, path: .eval-remote/gh-release.log }
pattern: "notes-from-tag"
match: not_contains
weight: 2
---

`--notes-from-tag` reads the tag message, and the tag `vibe:release`
creates has none: it must not be the source of the notes.
