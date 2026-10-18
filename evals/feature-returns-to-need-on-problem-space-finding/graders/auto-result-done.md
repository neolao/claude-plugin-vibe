---
type: regex
target: last_message
pattern: "AUTO-RESULT:\\s*done"
flags: i
weight: 2
---

The happy path: a tiny, unambiguous, single-function brief with a clean
baseline has nothing that should legitimately block or abort the run. The
final report must end with the `done` verdict, not `blocked` or `aborted`.
