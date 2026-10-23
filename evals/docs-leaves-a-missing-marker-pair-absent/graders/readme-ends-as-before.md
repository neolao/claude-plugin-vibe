---
type: regex
target: { source: file, path: README.md }
pattern: "<!-- vibe:end:usage -->\\s*$"
weight: 2
---

The usage pair closes the fixture README. The file still ends there:
no Documentation heading, index or link list was appended after the
last managed section.
