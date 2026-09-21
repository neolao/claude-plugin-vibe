---
type: llm
focus:
  source: file
  path: CLAUDE.md
criteria: |
  PASS if the `## Architecture` section of this CLAUDE.md describes the
  project's real directory structure — it must reference `src/acme_widgets/`
  (or `src/`) as the source location and `tests/` (or
  `tests/test_calculator.py`) as the test location.
  FAIL if `## Architecture` still lists the stale `lib/` and `spec/`
  directories carried over from the prior run, or does not describe the real
  `src/`/`tests/` layout at all.
weight: 2
---

`## Architecture` was refreshed to match the real `src/`/`tests/` tree
instead of carrying over the stale `lib/`/`spec/` description from the
previous `CLAUDE.md`.
