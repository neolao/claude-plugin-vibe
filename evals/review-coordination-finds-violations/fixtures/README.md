# helpdesk

Ticketing service of a support team. `tickets/` holds the ticket model,
its priorities and limits, `reports/` builds the daily overdue report,
`web/` serves the agent UI (Python views, a few static scripts). Tests run
with `python3 -m unittest discover tests`.
