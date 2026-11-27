---
type: llm
focus: last_message
criteria: |
  fixtures/CLAUDE.md declares that every page under docs/ has the
  sections `## Purpose`, `## How to` and `## See also`, the last never
  empty. fixtures/docs/export.md has the first two and no `## See also`;
  fixtures/docs/import.md has all three.

  PASS if the reported findings include a `Format` (or clearly
  equivalent category name) finding whose FILE: line points to
  fixtures/docs/export.md, that says the `See also` section is missing,
  and that names CLAUDE.md (or its writing conventions) as the template
  it measures against.
  FAIL if no finding reports the missing section, if the finding names no
  template, or if a finding reports a missing section on
  fixtures/docs/import.md.
weight: 2
---

Reports the mandatory section the repo's own convention requires and the
page lacks, naming where the convention is declared.
