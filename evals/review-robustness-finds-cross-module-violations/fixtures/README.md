# inventory

Keeps the shop's stock levels in step with the supplier's. A scheduler thread
calls `worker.tick` every five minutes with the SKUs the supplier reports as
changed; the back-office UI sets a level by hand through `api.adjust_stock`,
which runs on the app's asyncio event loop. `conn` is a `sqlite3` connection
to the shop database.
