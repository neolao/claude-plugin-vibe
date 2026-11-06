# helpdesk

Ticketing service of a support team. `tickets/` holds the ticket model,
its statuses and limits, `reports/` builds the daily CSV export, `api/`
the HTTP contracts (`v1/` is frozen for the integrations that still use
it, `v2/` is current), `mobile/` the Kotlin client released through the
app stores, `scripts/` the build helpers. Tests run with
`python3 -m unittest discover tests`.
