---
type: llm
focus: last_message
criteria: |
  `ReceiptPrinter._render(text, uppercase)` in fixtures/receipts/printer.py
  is a private helper with one caller, `print_receipt`, which passes the
  flag positionally (`self._render(body, True)`).

  PASS if no `high` or `medium` severity Boolean blindness (or
  equivalent) finding targets this call. A `low` finding passes, as does
  a report with no findings at all.
  FAIL if the call is flagged at high or medium severity.
weight: 1
---

A positional boolean on a private one-caller method is a contained match:
`low` at most.
