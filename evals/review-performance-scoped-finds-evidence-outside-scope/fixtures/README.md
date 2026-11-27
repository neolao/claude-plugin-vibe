# shipping

HTTP service behind the customer tracking page and the marketplace seller
API. `api/` holds the handlers, which run on a single asyncio event loop;
`shipping/` holds the helpers they call: the queries, the response shapes,
the label renderer, the zone table and the scan store. `db` is an asyncpg
connection pool.
