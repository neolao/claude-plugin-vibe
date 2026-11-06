---
date: 2026-06-18
status: accepted
---
# Money is integer cents end to end
**Context:** Two totals computed in floating point rounded differently in the
API response and in the stored row, and finance reconciled a one-cent gap by
hand every month.
**Decision:** Every amount is an `int` in cents, in every signature, every
computation and every stored column. VAT and discounts are integer arithmetic
(`// 100`), never a float multiplied then rounded.
**Reason:** Integer arithmetic gives the same cent everywhere; a float that is
rounded at the end still differs by one cent depending on where the rounding
happens.
**Rejected alternatives:** `Decimal` with a fixed context — correct, but every
boundary would convert, and the ports already take `int`.
