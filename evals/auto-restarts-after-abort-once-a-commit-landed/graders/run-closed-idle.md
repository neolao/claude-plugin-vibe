---
type: regex
pattern: "status:\\s*idle"
target: { source: file, path: ".vibe/auto-state.md" }
weight: 1
---

Step 5 closes the new run cleanly: `status: idle`, not `stopped` — nothing
aborted this time.
