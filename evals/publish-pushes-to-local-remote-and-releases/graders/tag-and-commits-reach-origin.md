---
type: file_exists
path: ".eval-remote/origin.git/refs/tags/v1.0.1"
exists: true
weight: 2
---

The `v1.0.1` tag must exist in the stand-in remote, not merely be named in
the report: `git push --tags` is the step under test, and a run that cuts
the release locally without pushing it looks identical in prose.
