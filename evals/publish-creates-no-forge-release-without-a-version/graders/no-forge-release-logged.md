---
type: file_exists
path: ".eval-remote/gh-release.log"
exists: false
weight: 2
---

The `gh` stand-in writes this log only on `release create`: it must not
exist after a run that released nothing.
