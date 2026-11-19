---
type: regex
target: last_message
pattern: "❓"
match: not_contains
weight: 3
---

Every technical decision of this feature is answerable from the code and
`CLAUDE.md`: where a new format lives (an `Exporter` subclass registered
in `exports/__init__.py`), the test framework and location (unittest,
`tests/test_*.py`), how money is represented (integer cents, formatted in
the exporter). No round may reach the Product Owner. The eval never offers
`AskUserQuestion`, so the skill writes its round as text (`❓ **Q1**`),
which the case prompt asks to reproduce verbatim: a `❓` in the final
message is a question asked.
