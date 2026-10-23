---
type: regex
target:
  source: file
  path: roadmap/CLAUDE.md
pattern: "## Role\\n(?:(?!\\n## ).)*florist"
flags: s
match: contains
weight: 1
---

The paragraph is carried over in its place, under `## Role`, not moved
to a section of its own or appended at the end.
