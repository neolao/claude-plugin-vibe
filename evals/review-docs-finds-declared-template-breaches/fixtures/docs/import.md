# Importing a bank statement

## Purpose

Get a month of bank movements into Ledger as transactions, ready to be matched with invoices.

## How to

```sh
ledger import statements/2026-01.csv
```

The command reads the file, maps each row to a transaction and queues the reconciliation. Rows that fail to parse are listed at the end of the run and skipped; the import is not rolled back. A CSV import is capped at 10 000 rows.

## See also

- [Exporting for the accountant](export.md)
