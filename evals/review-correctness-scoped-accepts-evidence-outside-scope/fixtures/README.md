# orders

Order service of a small web shop. `orders/` holds checkout, pricing,
stock reservations and receipts, `shipping/` the carrier quotes,
`inventory/` the warehouse levels, `reports/` the monthly summary sent to
finance, `app/` the HTTP layer. `app/server.py` serves requests from a
thread pool.
