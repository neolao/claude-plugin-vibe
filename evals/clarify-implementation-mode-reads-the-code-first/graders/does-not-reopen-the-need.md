---
type: llm
focus: last_message
criteria: |
  The need was settled before this mode (CSV, columns, owner-only, month
  picker, header-only file for an empty month).

  PASS if no question and no decision reopens one of those product points —
  no "which format", no "which roles", no "what about an empty month" — and
  any product point that surfaces is noted as `(other space)` rather than
  decided.
  FAIL if the implementation mode asks or re-decides a product point.
weight: 1
---

Stays in the solution space.
