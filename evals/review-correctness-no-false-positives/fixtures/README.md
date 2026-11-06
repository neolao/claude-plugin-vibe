# billing

Billing service of a small web shop. `billing/` holds the pricing, refund,
period, settlement and rounding rules, `stock/` the in-memory warehouse
stock, `reports/` the monthly summary sent to finance, `api/` the HTTP
layer. `api/app.py` serves requests from a thread pool. Recorded decisions
live in `.vibe/decisions/`.
