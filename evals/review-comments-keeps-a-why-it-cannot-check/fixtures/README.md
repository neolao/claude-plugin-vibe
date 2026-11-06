# partner-exporter

Sends the day's shipments to the logistics partner's API. `exporter/` builds
the payload and posts it; the nightly job calls `export_day` once per day.
