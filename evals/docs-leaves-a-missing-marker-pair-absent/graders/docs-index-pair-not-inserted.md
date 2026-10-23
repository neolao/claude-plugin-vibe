---
type: regex
target: { source: file, path: README.md }
pattern: "vibe:begin:docs-index|vibe:end:docs-index"
match: not_contains
weight: 3
---

The fixture README has no docs-index pair. Nothing outside the managed
markers is ever touched: the pair is reported as absent, never inserted,
even though `docs/architecture.md` exists and would be indexed if the
section were managed.
