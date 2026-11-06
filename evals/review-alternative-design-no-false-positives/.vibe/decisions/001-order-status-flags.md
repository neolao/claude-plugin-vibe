---
date: 2026-02-09
status: accepted
---
# Order status is four independent booleans guarded in `Order`, not a state machine
**Context:** The order lifecycle was first written as a `status` enum with a transition table. Two real orders are both cancelled and refunded, and a shipped order can be refunded without being cancelled: a single status could not say which flags were set, and the support console had to rebuild them from the event log.
**Decision:** `Order` carries `is_paid`, `is_shipped`, `is_cancelled` and `is_refunded` as independent booleans, each set once by its own method (`pay`, `ship`, `cancel`, `refund`), which checks the other flags it depends on and raises on an illegal call. The repository persists the four columns as they are. A new step adds one flag and one method.
**Reason:** The flags carry exactly the facts the business asks about ("was it paid?", "did it ship?"), several of which hold at once; every column maps to one question, and the guards in the four methods are the whole transition rule.
**Rejected alternatives:** An explicit state machine or a status sum type with a transition table — a single current state cannot express the combinations the business keeps asking about, and the table was reconstructed into flags by every reader. An event-sourced order — more than this module needs for four facts.
