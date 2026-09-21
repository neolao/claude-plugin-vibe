---
type: llm
focus: last_message
criteria: |
  The fixtures use only clean, well-bounded patterns that superficially
  resemble each checklist category without being a violation:
  - `is_active` returns a real boolean expression after a genuine early
    guard clause — not an if/else both returning literal `True`/`False`
    (Redundant logic).
  - `get_or_create_cart` looks like a delegating wrapper but actually adds
    creation-and-defaulting logic of its own, not pure indirection
    (Indirection).
  - `merge_adjacent_discounts` accumulates a running total with a `continue`
    and only flushes it conditionally — genuine stateful control flow that a
    single comprehension cannot express, not a non-idiomatic detour
    (Non-idiomatic).
  - `send_notification`'s `channel` parameter is called with three different
    values (`"email"`, `"sms"`, and a variable `endpoint`) across its call
    sites — genuinely exercised, not unused generality (Unused generality).
  - `validate_order`, `calculate_shipping`, and `summarize_order` are all
    short, shallow (at most one level of nesting), and have low branching
    (Complexity, Length, Nesting).

  PASS if the response reports no `high` or `medium` severity finding in any
  of `Redundant logic`, `Indirection`, `Non-idiomatic`, `Unused generality`,
  `Complexity`, `Length`, or `Nesting` on this code — either no findings at
  all, or only `low` severity style notes unrelated to these already-clean
  patterns.
  FAIL if it flags `is_active`'s guard clause as redundant, `get_or_create_cart`
  as a pointless wrapper, `merge_adjacent_discounts`' loop as needing a
  comprehension, `channel` as unused generality, or any of the three pipeline
  functions as a complexity/length/nesting hotspot.
weight: 2
---

Does not invent simplicity findings on code that already follows the clean
pattern for each category.
