---
status: todo
---
# Fix Crash On Empty List

## Description
`first_of([])` crashes with an IndexError instead of failing clearly. It should raise a ValueError naming the problem.

## Acceptance Criteria
- [ ] `first_of([])` raises a `ValueError` whose message mentions the empty list.
- [ ] `first_of([7, 8, 9])` still returns `7`.

## Notes
None.
