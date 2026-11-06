---
type: llm
focus: last_message
criteria: |
  `parse_amount` in fixtures/pricing/amounts.py is public, and its docstring
  `"""Parse the amount from the text."""` only restates its name. The
  fixture's CLAUDE.md and setup.cfg make pydocstyle (D103) require a
  docstring on every public function. The function's contract, visible in
  its body: returns the amount in cents (an int), accepts a comma as the
  decimal separator and a currency symbol, raises ValueError on text that is
  not an amount or on a negative amount.

  PASS if the reported findings include a finding on that docstring whose
  SUGGESTION quotes a replacement docstring that states at least two of:
  cents returned, comma (or currency symbol) accepted, ValueError raised.
  FAIL if no finding flags the `parse_amount` docstring, or if its
  SUGGESTION is to delete it (with or without a replacement).
weight: 1
---

Reports the signature-restating docstring of a public function, and
suggests the contract to write in it rather than `delete`: the repo's
convention and lint require the docstring to exist, so deleting it would
break the build.
