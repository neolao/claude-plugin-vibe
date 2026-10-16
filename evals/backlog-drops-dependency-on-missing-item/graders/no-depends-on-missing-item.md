---
type: llm
focus: trace
criteria: |
  The backlog holds items 001 and 002 only. The request says "after 007",
  and no item 007 exists at the top level or under `done/`.

  PASS if the item file written to `.vibe/backlog/003-*.md` has no
  `depends_on` entry naming 007 — either no `depends_on` line at all, or one
  that does not contain 007 — and still has `status: todo`, a title about
  PDF export and a `## Acceptance Criteria` section with 2 to 4 `- [ ]`
  items.
  FAIL if the written file carries `depends_on` with 007 in it, or if no
  003 file was written.
  The skill's own instructions are also in the trace: judge the content of
  the `Write` (or equivalent) tool call that creates the 003 file, not the
  skill's template.
weight: 3
---

Step 8 leaves a dependency on a non-existent item out of the file, so
`/vibe:auto` can still pick 003.
