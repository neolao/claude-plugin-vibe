# Importing a bank statement

Download the statement (what your bank's website may call an account export) for the month to import — most banks offer CSV or OFX — and drop it on **Import → Bank statement**. Ledger parses the statement into transactions and queues the reconciliation, which matches each transaction with an open invoice; rows that fail to parse are listed at the end and skipped.

A transaction the reconciliation could not match stays in the **To review** tab until an invoice is attached to it. The error `invoice not found` in the summary means the reference typed on a transaction matches no open invoice.

## Size of a statement

A CSV import is capped at 10 000 rows: a longer file is rejected before parsing, so split a multi-year export by year.
