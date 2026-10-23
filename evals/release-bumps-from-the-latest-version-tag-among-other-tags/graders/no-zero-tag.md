---
type: file_exists
path: ".git/refs/tags/v0.0.1"
exists: false
weight: 2
---

No `v0.0.1` tag may exist: with no manifest, a skill that found no usable
tag would fall back on `0.0.0` — the fallback is for a repo with no
version tag at all, not for one whose version tag is hidden behind other
tags.
