# invoicing

Internal tool of the finance team. `billing/` builds and exports invoices,
`workers/` holds the jobs the scheduler runs at night, `reports/` prints the
monthly figures, and `cli/` is the entry point: `python -m cli.main <command>`.
