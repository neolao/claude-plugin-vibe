---
type: llm
focus: last_message
criteria: |
  `parse_amount` in fixtures/pricing/amounts.py and `main` in
  fixtures/bin/import_prices.py are public functions whose one-line
  docstrings state contract: cents returned, comma and currency symbol
  accepted, ValueError on a non-amount or a negative; one `ref;cents` line
  per row, exit 1 on the first bad amount. The fixture's CLAUDE.md and
  setup.cfg make pydocstyle require a docstring on every public function.

  PASS if no `high` or `medium` severity finding targets either docstring,
  and no finding at any severity suggests deleting one of them. A `low`
  finding that only shortens the wording passes, as does a report with no
  findings at all.
  FAIL if either docstring is flagged at high or medium severity, or if a
  finding suggests deleting it.
weight: 1
---

Keeps public docstrings that state what the caller may rely on: they carry
the contract the signature does not, and the repo's convention requires
them anyway.
