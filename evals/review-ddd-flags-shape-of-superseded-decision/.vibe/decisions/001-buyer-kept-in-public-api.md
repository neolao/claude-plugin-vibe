---
date: 2026-02-11
status: superseded by 002
---
# The public API keeps `buyer` for the customer while the mobile app migrates
**Context:** The domain renamed the buyer to customer (`Order.customer_id`, `find_for_customer`). The mobile app, released quarterly, still reads `buyer_id` in order payloads and calls `/buyers/<id>/orders`.
**Decision:** `api/routes.py` keeps `buyer` in its paths and payloads until the mobile app ships the rename; everything behind the routes says customer.
**Reason:** Breaking the mobile app's parsing for a word is not worth an emergency release; the drift is confined to one file and dated.
**Rejected alternatives:** Serving both words in the payload — doubles every field the app reads and nobody would remove the old one.
