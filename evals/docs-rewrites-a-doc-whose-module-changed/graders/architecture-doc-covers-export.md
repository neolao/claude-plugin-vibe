---
type: regex
target: { source: file, path: docs/architecture.md }
pattern: "export"
flags: i
weight: 3
---

`src/export/` and the `export` command were committed after
docs/architecture.md was: the doc describes a layout that changed since
its last commit, so it is rewritten and now covers the export module.
