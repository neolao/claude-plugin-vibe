---
type: file_exists
path: ".vibe/backlog/done/001-fix-crash-in-order-total-average.md"
exists: true
weight: 1
---

The `--auto` run of `vibe:fix` ships the item and the workflow's Commit
step moves it under `done/`: the file must exist at its moved-to path.
