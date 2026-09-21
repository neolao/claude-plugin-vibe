---
type: llm
focus: trace
criteria: |
  PASS if the three backlog item files written to `.vibe/backlog/001-*.md`,
  `.vibe/backlog/002-*.md`, and `.vibe/backlog/003-*.md` each have:
  - a `status: todo` line in their frontmatter, and
  - a `## Acceptance Criteria` section containing between 2 and 4 checkbox
    items (`- [ ]`).
  One of the three files should be about CSV export, one about dark mode,
  and one about email notifications (in any order).
  FAIL if any of the three files is missing `status: todo`, is missing the
  `## Acceptance Criteria` section, has fewer than 2 or more than 4 checkbox
  items, or if the files don't correspond to the three candidate features.
weight: 2
---

Confirms each created item has valid `status: todo` frontmatter and a
`## Acceptance Criteria` section with 2-4 checkboxes, per Step 9's template.
