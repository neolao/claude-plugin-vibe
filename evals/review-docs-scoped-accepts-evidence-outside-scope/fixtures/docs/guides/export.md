# Exporting for the accountant

The export collects the reconciled transactions of a period into one file the accountant's software reads.

## Running an export

```sh
ledger export --period 2026-Q1 --format xlsx
```

Formats are described in [the formats reference](../reference/formats.md#xlsx). The file is written to `exports/` and named after the period.

## What is included

Only transactions marked reconciled are exported. A transaction still in **To review** is left out and listed in the run's summary so nothing is silently dropped.
