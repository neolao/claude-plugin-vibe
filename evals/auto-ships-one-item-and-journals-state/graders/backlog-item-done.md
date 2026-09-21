---
type: file_exists
path: ".vibe/backlog/done/001-tiny-feature.md"
exists: true
weight: 2
---

Once the item ships, the workflow's Commit step does
`git mv .vibe/backlog/001-tiny-feature.md .vibe/backlog/done/001-tiny-feature.md`
and sets `status: done`. The file must exist at its new, moved-to path.
