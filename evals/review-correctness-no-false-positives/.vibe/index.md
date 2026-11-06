# billing

Billing service of a small web shop: pricing, refunds, periods, settlement
and rounding rules in `billing/`, the warehouse stock in `stock/`, the
monthly finance summary in `reports/`, the HTTP layer in `api/`.

## Modules
- `billing` — pricing, refunds, periods, settlement, rounding, audit
- `stock` — in-memory warehouse stock
- `reports` — monthly summary
- `api` — HTTP handlers

## Decisions
- `decisions/001-amounts-are-truncated-to-the-cent.md`
