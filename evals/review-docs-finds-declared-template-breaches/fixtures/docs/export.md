# Exporting for the accountant

## Purpose

Hand the accountant one file holding the reconciled transactions of a period.

## How to

```sh
ledger export --period 2026-Q1 --format xlsx
```

The file is written to `exports/` and named after the period. Only transactions marked reconciled are included; a transaction still in **To review** is left out and listed in the run's summary so nothing is silently dropped.
