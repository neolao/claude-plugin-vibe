---
type: tool_used
tool: AskUserQuestion
min: 0
max: 0
weight: 3
---

Every technical decision of this feature is answerable from the code and
`CLAUDE.md`: where a new format lives (an `Exporter` subclass registered
in `exports/__init__.py`), the test framework and location (unittest,
`tests/test_*.py`), how money is represented (integer cents, formatted in
the exporter). `AskUserQuestion` is granted and must stay unused: a
question here would ask a Product Owner about code.
