---
status: todo
---
# Fix Crash In Order Total Average

## Description
`average_total()` in `stats.py` crashes with an `IndexError`: its loop range (`range(len(totals) + 1)`) reads one index past the end of the list. The existing test `test_stats.py::test_average_of_three_order_totals` fails because of this crash.

## Acceptance Criteria
- [ ] `average_total()` no longer crashes with an `IndexError`.
- [ ] `test_stats.py::test_average_of_three_order_totals` passes.

## Notes
None.
