---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "(exportPdf|ReportService|pdf-export\\.js|pagination\\.js|paginate\\(|pageSize)"
match: not_contains
weight: 3
---

The two commit subjects name a method, a class, two file paths and a
parameter. None of them belongs in a changelog entry: the user reads
"export a report as PDF" and "a page size of 0", never `exportPdf()` or
`pageSize`.
