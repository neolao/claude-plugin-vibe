# orders

Order service of a small web shop. `orders/` holds checkout, pricing,
stock reservations and the nightly price import, `shipping/` the carrier
quotes, `catalog/` the SKU handling and the price list, `inventory/` the
warehouse levels, `reports/` the monthly summary sent to finance, `app/`
the HTTP layer. `app/server.py` serves requests from a thread pool.
