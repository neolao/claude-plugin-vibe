# Exporting for the accountant

```sh
ledger export --period 2026-Q1 --format xlsx
```

The export is written to `exports/` and named after the period; send that file to the accountant. It holds one row per reconciled transaction, with the invoice reference beside the bank's label, and changes nothing in the reconciliation itself: a transaction still in **To review** is left out and listed in the run's summary.

The rows come from `export()` in `src/export.py`, which reads the matches `reconcile()` produced and never calls `parse_bank_file()` again.
