# telemetry

HTTP service the installed sensors report to. A fleet of a few hundred
thousand sensors uploads a diagnostic trace of a few MB when asked; the
back-office dashboard lists one sensor's events, 50 at a time. Handlers run
on a single asyncio event loop; `db` is an asyncpg connection pool.
