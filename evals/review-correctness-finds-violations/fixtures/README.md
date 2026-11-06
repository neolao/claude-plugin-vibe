# billing

Billing service of a small web shop. `billing/` holds the pricing, refund,
period and settlement rules, `stock/` the in-memory warehouse stock,
`catalog/` the SKU handling and the nightly supplier import, `reports/` the
monthly summary sent to finance, `api/` the HTTP layer. `api/app.py` serves
requests from a thread pool.
