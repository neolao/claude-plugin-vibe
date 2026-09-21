---
status: todo
---
# Add a function that sums a list of numbers

## Description
`listutils.py` has no way to add up a list of numbers. Add a `sum_of` function to the same module.

## Acceptance Criteria
- [ ] `sum_of([1, 2, 3])` returns `6` (nominal case).
- [ ] `sum_of([])` returns `0` (empty-list edge case).
- [ ] `sum_of([1, "a"])` raises a clear error (non-numeric-input case).
