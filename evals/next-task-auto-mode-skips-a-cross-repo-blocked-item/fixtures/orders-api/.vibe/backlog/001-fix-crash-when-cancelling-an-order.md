---
status: todo
---
# Fix Crash When Cancelling An Order

## Description
Cancelling an order crashes when the cancellation reason is missing.

## Acceptance Criteria
- [ ] Cancelling an order without a reason no longer crashes.

## Notes
Cannot start until orders-sdk publishes v0.3.0 — the cancellation reason codes come from the SDK.
