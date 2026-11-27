---
type: llm
focus: last_message
criteria: |
  fixtures/.claude/rules/parsers.md declares `paths: ["src/parser/**"]`;
  the readers live under fixtures/src/parsers/ (with an s), so the glob
  matches no file and the rule never loads. fixtures/.claude/rules/reconcile.md
  declares `src/reconcile.py`, which exists.

  PASS if the reported findings include a `Format` (or clearly
  equivalent category name) finding whose FILE: line points to
  fixtures/.claude/rules/parsers.md and that says its `paths:` glob
  matches no file (naming `src/parser/**`, or the folder `src/parsers/`
  as the one that exists).
  FAIL if no finding reports that glob, or if a finding reports the glob
  of fixtures/.claude/rules/reconcile.md as matching nothing.
weight: 2
---

Reports the rule whose paths glob matches zero files today — a rule that
loads for nothing — and leaves the rule whose glob resolves alone.
