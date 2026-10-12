---
type: regex
pattern: 'depends_on:\s*\[\s*003\s*\]'
target: { source: file, path: ".vibe/backlog/002-import-orders-from-csv.md" }
match: contains
weight: 2
---

002 depended on 001 and 003: only 001 is dropped, 003 stays.
