---
type: llm
focus: last_message
criteria: |
  The fixtures use only clean, idiomatic patterns that superficially
  resemble anti-patterns without being one: a `Money` value object and
  `OrderStatus` enum instead of bare primitives/strings, an immutable
  `MAX_RETRIES` constant that is only ever read, `OrderRepository.save`
  reading the order's own fields for the persistence job it exists to do
  (not feature envy), `PaymentGateway.charge`'s keyword-only `retry`/
  `notify` flags that are self-documenting at every call site,
  `OrderRepository.parse_placed_at` using `datetime.fromisoformat` instead
  of hand-rolling a parser, `OrderService`'s constructor-injected
  dependencies and single `place_order` call with no required call order, a
  single canonical definition of the currency code, and a
  `logging_setup.py` module that is actually imported and used by
  `PaymentGateway`.

  PASS if the response reports no `high` or `medium` severity anti-pattern
  finding on this code — either no findings at all, or only `low` severity
  style notes unrelated to these already-clean patterns.
  FAIL if it flags `Money`/`OrderStatus` as primitive obsession or
  stringly-typed, `MAX_RETRIES` as mutable global state, `OrderRepository`
  or `OrderService` as a god object, `OrderRepository.save` as feature
  envy, `PaymentGateway.charge`'s keyword arguments as boolean blindness,
  `parse_placed_at` as wheel reinvention, `OrderService`'s constructor
  injection as temporal coupling, or `logging_setup.py` as cargo cult.
weight: 2
---

Does not invent anti-pattern findings on code that already follows the
idiomatic pattern for each category.
