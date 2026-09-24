# shipping

HTTP service behind the customer tracking page and the marketplace seller
API: lists a customer's shipments, quotes parcel prices, prints labels, and
takes scan events pushed by carriers. Handlers run on a single asyncio event
loop; `db` is an asyncpg connection pool.
