# Module: billing

**Role:** Builds the invoice of an order: line amounts, the delivery fee asked
from shipping, VAT once at the end.
**Files:** `billing/invoice.py`
**Exports:** `Invoice`, `build_invoice(order_id, line_amounts_cents, country) -> Invoice`
**Depends on:** [`modules/shipping.md`](shipping.md) (delivery fee per country)
