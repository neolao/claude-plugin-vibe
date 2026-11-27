# Importing a bank statement

A statement is imported from the command line or from the web form. Both paths run the same parser and the same reconciliation.

## From the command line

```sh
ledger import statements/2026-01.csv
```

The command reads the file, maps each row to a transaction and queues the reconciliation. Rows that fail to parse are listed at the end of the run and skipped; the import is not rolled back.

## From the web form

Choose **Import → Bank statement**, pick the file and confirm. The form accepts CSV and OFX (see [the formats reference](../reference/formats.md)).

## Size of a statement

A CSV import is capped at 5 000 rows: a longer file is rejected before parsing, so split a yearly export by quarter. The cap is the same for both paths.

## After the import

Transactions appear in the reconciliation view within a minute. Unmatched ones stay in the **To review** tab until an invoice is attached.
