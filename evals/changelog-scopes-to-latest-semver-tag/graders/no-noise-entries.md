---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "(Merge branch|pipeline|flaky)"
flags: i
match: not_contains
weight: 1
---

The `chore(ci): fix flaky pipeline cache` commit is CI housekeeping with no
user-visible effect, despite the word "fix" in its message, and the merge
commit of `perf/report-list` is noise. Neither produces an entry.
