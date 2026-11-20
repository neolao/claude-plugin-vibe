---
type: regex
pattern: '"version": "1\.2\.3",\n  "description": "Fixture app for the vibe:release eval",\n  "files": \["dist"\],'
target: { source: file, path: "package.json" }
match: contains
weight: 2
---

`package.json` is back to its committed content: the bump is undone and the
file was not reformatted by hand.
