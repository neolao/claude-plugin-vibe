# helpdesk

Ticketing service of a support team: a Python backend (`tickets/`,
`reports/`, `api/`) and a Kotlin mobile client (`mobile/`) released on its
own cycle through the app stores.

## Modules
- `tickets` — ticket model, statuses, limits
- `reports` — daily CSV export
- `api` — HTTP contracts, v1 (frozen) and v2
- `mobile` — Kotlin client

## Decisions
- `decisions/001-mobile-client-keeps-its-own-status-list.md`
