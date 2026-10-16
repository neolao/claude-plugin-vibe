---
type: regex
pattern: "status:\\s*stopped"
target: { source: file, path: ".vibe/auto-state.md" }
weight: 1
---

The state file is left as found: `status: stopped`, so the next invocation
applies the same check again.
