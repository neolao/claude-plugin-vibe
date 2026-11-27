# Importing a bank statement

```sh
ledger import statements/2026-01.csv
```

The command reads the file, maps each row to a transaction and queues the reconciliation. Rows that fail to parse are listed at the end of the run and skipped; the import is not rolled back. When a row is rejected for a reason the summary does not explain, [the troubleshooting page](troubleshooting.md) lists the parser messages and what each means.

## Size of a statement

<!-- KEEP IN SYNC with docs/limit.md -->
A CSV import is capped at 10 000 rows: a longer file is rejected before parsing, so split a multi-year export by year.

## After the import

Transactions appear in the reconciliation view within a minute. Unmatched ones stay in the **To review** tab until an invoice is attached.
