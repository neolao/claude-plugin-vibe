---
type: regex
target: { source: file, path: README.md }
pattern: "caching\\.md"
match: not_contains
weight: 1
---

The index entry for the deleted `docs/caching.md` is removed. The fixture
README mentions `caching.md` nowhere else.
