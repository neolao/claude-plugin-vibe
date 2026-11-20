---
type: regex
pattern: '"version": "1\.2\.4",\n  "description": "Fixture app for the vibe:release eval",\n  "files": \[\n    "dist"\n  \],'
target: { source: file, path: "package.json" }
match: contains
weight: 2
---

`package.json` carries the new version and the layout the project's formatter
writes: the `files` array spread over three lines.
