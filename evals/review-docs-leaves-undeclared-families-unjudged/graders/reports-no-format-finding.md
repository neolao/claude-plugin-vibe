---
type: llm
focus: last_message
criteria: |
  No file of the fixture declares a writing convention, a section list,
  a word budget or a frontmatter schema: fixtures/CLAUDE.md lists
  commands only. fixtures/docs/import.md has Purpose / How to / See also
  sections, fixtures/docs/export.md has a code block and a Formats table,
  and nothing says either shape is required.

  PASS if no `high` or `medium` severity finding of category `Format`
  (or a clearly equivalent category name) is reported on any file — in
  particular none saying fixtures/docs/export.md lacks a section
  fixtures/docs/import.md has, or that the two pages should share a
  layout. A `low` finding passes, and so does a report with no findings
  at all.
  FAIL if any Format finding at high or medium severity measures a page
  against a template no file in the fixture declares.
weight: 2
---

Does not measure a doc family against an invented standard: with no
declared template, the shape of the pages is not judged.
