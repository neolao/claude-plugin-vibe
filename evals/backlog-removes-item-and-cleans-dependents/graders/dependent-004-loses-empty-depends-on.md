---
type: llm
focus: { source: file, path: ".vibe/backlog/004-add-gift-cards.md" }
criteria: |
  The file is the backlog item 004. Its only dependency was 001, which has
  been removed.

  PASS if the frontmatter has no `depends_on` line at all (neither a `depends_on:`
  line with an empty list, nor a leftover mention of 001) and the rest of the
  item is intact: `status: todo`, the title `Add Gift Cards` and both
  acceptance criteria.
  FAIL if a `depends_on` line is still there, even empty, or if any other part
  of the item changed.
weight: 2
---

An emptied `depends_on` is removed entirely, and nothing else in 004 is touched.
