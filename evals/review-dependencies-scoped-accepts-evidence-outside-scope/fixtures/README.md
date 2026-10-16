# shop-backoffice

Back-office service of the web shop. `orders/` prices a basket, `payments/`
charges it through the payment provider, `reports/` prints the receivables
for the finance team, and `cli/` is the entry point:
`python -m cli.main <command>`. Tests live in `tests/` and run with `pytest`.
