---
type: llm
focus: last_message
criteria: |
  The closing report must open with
  `CLARIFY-RESULT: settled — mode: implementation`, and `### Decisions
  made` must settle, each with a `(source: …)` citation into the fixture
  (`CLAUDE.md`, `exports/base.py`, `exports/__init__.py`, `tests/…`):
  - the new CSV format is an `Exporter` subclass registered in the
    `REGISTRY` of `exports/__init__.py` (not a free function, not a change
    to the admin page);
  - tests are `unittest` files under `tests/`;
  - amounts come as integer cents and are formatted by the exporter.

  PASS if the mode line is present and those three decisions appear with a
  source each.
  FAIL if the mode is missing, if one of the three is absent, or if a
  decision taken from the code carries no source.
weight: 3
---

The implementation framing reads the conventions and cites them; the
caller will have the citations checked.
