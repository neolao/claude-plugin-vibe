---
type: regex
target: { source: file, path: .eval-remote/gh-release.log }
pattern: "misspelled greeting"
weight: 3
---

The notes given to `release create` (inline or through a notes file,
whose content the stand-in copies into the log) must carry the Fixed
entry of the v1.0.1 changelog section — the text that says what shipped.
