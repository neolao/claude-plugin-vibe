---
status: todo
---
# Fix Crash In Average Calculator

## Description
`average()` in `calculator.py` crashes with an `IndexError`: a bug in its loop range (`range(len(numbers) + 1)`) reads one index past the end of the list. The existing test `test_calculator.py::test_average_of_three_numbers` currently fails because of this crash.

## Acceptance Criteria
- [ ] `average()` no longer crashes with an `IndexError`.
- [ ] `test_calculator.py::test_average_of_three_numbers` passes.
