---
type: regex
pattern: "run started[\\s\\S]*run started"
target: { source: file, path: ".vibe/auto-state.md" }
weight: 2
---

The journal is append-only across runs: the new run adds its own
`## [timestamp] — run started` section after the one that recorded the
abort, which stays.
