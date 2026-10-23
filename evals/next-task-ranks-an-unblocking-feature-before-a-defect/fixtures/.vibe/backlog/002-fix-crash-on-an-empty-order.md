---
status: todo
---
# Fix Crash On An Empty Order

## Description
`order_total()` crashes when an order has no lines instead of returning 0.

## Acceptance Criteria
- [ ] `order_total([])` returns 0 and does not crash.

## Notes
None.
