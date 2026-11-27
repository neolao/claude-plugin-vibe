# Backlog item 024 — Reject expired coupons

## Description
Customers sometimes apply a coupon after its expiry date and get the discount anyway.

## Acceptance Criteria
1. A coupon applied after its expiry date is refused with the message "Coupon expired".
2. The admin coupon list shows each coupon's expiry date.
3. Each refusal is recorded in the audit log with the coupon code.
