---
type: file_exists
path: ".git/refs/tags/v1.2.4"
exists: false
weight: 2
---

No `v1.2.4` tag may exist: a patch bump here means the suggestion was
read off the stale `[Unreleased]` section before `vibe:changelog` ran, and
a feature shipped as a fix release.
