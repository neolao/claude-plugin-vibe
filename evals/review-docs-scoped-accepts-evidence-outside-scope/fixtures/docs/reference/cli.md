# The `ledger` command

## `ledger import <file>`

Imports a statement. Options:

- `--timeout <seconds>` — how long to wait for the reconciliation before giving up; default 30 s.
- `--dry-run` — parse and report, write nothing.

## `ledger export --period <period> --format <csv|xlsx>`

Exports the reconciled transactions of the period into `exports/`.
