---
type: regex
target: { source: file, path: README.md }
pattern: "logo\\.svg|\\.nojekyll"
match: not_contains
weight: 1
---

Non-Markdown files in `docs/` are never indexed. The fixture README mentions
neither file.
