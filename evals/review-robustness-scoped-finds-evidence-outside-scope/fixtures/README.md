# parcels

Warehouse tool that hands parcels to the carriers. `shipping/` prepares the
labels and the pickup, `carriers/` talks to the carriers' HTTP APIs, `events/`
is the in-process bus the dashboards listen to, `spool/` keeps the label files
until the carrier's driver collects them, and `workers/` holds the jobs the
scheduler runs. A scanner thread calls `shipping.dispatch.dispatch_parcel` for
each parcel scanned at the dock; the back-office UI holds a parcel through
`shipping.api.hold_parcel`, which runs on the app's asyncio event loop.
