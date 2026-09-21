---
type: file_exists
path: ".git/refs/tags/v1.2.4"
exists: true
weight: 2
---

`/vibe:release` cuts the version and tags it locally (pushing is
`vibe:publish`'s job, checked by `no-push.md`). The tag must exist as a real
git ref, not just be mentioned in the report.
