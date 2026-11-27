# telemetry

HTTP service the installed sensors report to. A fleet of a few hundred
thousand sensors, each replaced every couple of years, posts a heartbeat
every 30 seconds and uploads a diagnostic trace of a few MB when asked; the
back-office dashboard reads the state of one sensor at a time. Handlers run
on a single asyncio event loop.
