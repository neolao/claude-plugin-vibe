# Exporting for the accountant

```sh
ledger export --period 2026-Q1 --format xlsx
```

The reconciliation is written to `exports/` and named after the period; send that file to the accountant. It holds one row per reconciled transaction, with the invoice reference beside the bank's label, and changes nothing in the matches themselves.

A settlement batch that is still open at the end of the period is left out of the file and listed in the run's summary.
