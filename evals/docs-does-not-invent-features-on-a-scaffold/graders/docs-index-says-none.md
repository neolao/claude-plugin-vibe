---
type: regex
target: { source: file, path: README.md }
pattern: "vibe:begin:docs-index[\\s\\S]*?No additional documentation yet\\.[\\s\\S]*?vibe:end:docs-index"
weight: 1
---

With no `docs/` folder, the documentation index carries the fixed
sentence rather than an invented entry.
