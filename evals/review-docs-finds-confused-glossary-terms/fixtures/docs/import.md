# Importing a bank statement

Download the invoice from your bank's website for the month to import — most banks offer CSV or OFX — and drop it on **Import → Bank statement**. Ledger parses the invoice into transactions and queues the reconciliation; rows that fail to parse are listed at the end and skipped.

Transactions are grouped into a settlement batch per import; the batch id is shown in the summary and reused in the review screen.

## Size of a statement

A CSV import is capped at 10 000 rows: a longer file is rejected before parsing, so split a multi-year export by year.
