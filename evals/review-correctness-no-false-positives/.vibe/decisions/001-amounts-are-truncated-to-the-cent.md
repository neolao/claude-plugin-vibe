---
date: 2026-01-20
status: accepted
---
# Displayed and invoiced amounts are truncated to the cent, never rounded
**Context:** The invoicing regulation the shop falls under requires that an amount shown to the customer never exceeds the computed amount; a half-cent rounded up is a breach, a half-cent dropped is not.
**Decision:** `billing/rounding.py: to_cents` converts an amount to cents with `ROUND_DOWN` on a `Decimal` built from the amount's string form. Every invoice line and total goes through it. Totals are computed from the truncated line amounts, never truncated once at the end.
**Reason:** Rounding to nearest (the Python default, half to even) can display more than was computed; truncation never does, and the lost fraction of a cent per line is accepted by finance.
**Rejected alternatives:** Rounding half up — simpler to explain, but breaches the regulation on every half-cent; storing amounts as integer cents everywhere — the provider's API delivers floats, the conversion has to happen somewhere and this is that place.
