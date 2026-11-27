# Importing a bank statement

```sh
ledger import path/to/statement.csv
```

The command reads the file, maps each row to a transaction and queues the reconciliation (`src/reconcile.py`). Several statements are imported in one run with a pattern, `ledger import statements/*.csv`; each file is parsed on its own and a failure in one does not stop the others.

## Parsed statements

A parsed statement is kept in `.ledger/cache/`, created on first run next to the configuration file, so a second import of the same file is a no-op. Delete the directory to force a full re-parse.

## Exports

An export is written as `exports/<period>.xlsx` (or `.csv`), the period being the one given on the command line.
