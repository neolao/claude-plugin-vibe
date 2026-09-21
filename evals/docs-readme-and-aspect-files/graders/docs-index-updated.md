---
type: regex
target: { source: file, path: README.md }
pattern: "vibe:begin:docs-index[\\s\\S]*?architecture\\.md[\\s\\S]*?vibe:end:docs-index"
weight: 1
---

Once docs/architecture.md exists, the README's docs-index section must list
it, per Step 3's "Documentation index" rule.
