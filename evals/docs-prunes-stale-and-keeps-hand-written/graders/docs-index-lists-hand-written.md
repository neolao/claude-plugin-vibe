---
type: regex
target: { source: file, path: README.md }
pattern: "vibe:begin:docs-index[\\s\\S]*?contributing\\.md[\\s\\S]*?vibe:end:docs-index"
weight: 1
---

The docs index lists every Markdown file in `docs/`, hand-written ones
included.
