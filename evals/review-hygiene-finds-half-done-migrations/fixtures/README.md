# shop-orders

Order service of the shop, deployed as one process. `app.py` builds the
shared objects once at start-up and exposes `ROUTES`, which the HTTP server
reads to dispatch requests; each request runs on its own thread.
