---
type: llm
focus: last_message
criteria: |
  fixtures/docs/guides/import.md states the 10 000-row cap that
  fixtures/docs/reference/limits.md gives, links to
  ../reference/formats.md and ../reference/limits.md, which exist, and
  says the reference holds the other limits; fixtures/docs/guides/export.md
  links to ../reference/formats.md#xlsx, whose `## XLSX` heading exists.
  fixtures/README.md lists both guides.

  PASS if no `high` or `medium` severity finding is anchored (its FILE:
  line) on fixtures/docs/guides/import.md or
  fixtures/docs/guides/export.md. A `low` finding passes, and so does a
  report with no findings at all.
  FAIL if either guide carries a high or medium finding — for example the
  row cap reported as a contradiction, a link reported as broken, or the
  guide being shorter than the reference reported as a conflict.
weight: 2
---

Does not report a guide that agrees with the reference it restates, links
to pages that exist and is listed by the index: a summary shorter than the
detail page conflicts with nothing.
