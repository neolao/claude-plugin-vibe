---
status: todo
---
# Cancel An Order

## Description
Let a customer cancel an order that has not shipped yet.

## Acceptance Criteria
- [ ] Customer can cancel an unshipped order.
- [ ] System refuses to cancel an order that already shipped.

## Notes
Cannot start until orders-sdk publishes v0.3.0 — this endpoint calls the
cancellation client that ships in that version.
