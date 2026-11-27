# Architecture

A statement goes through three modules, in this order.

1. **Parsers** — one reader per format. The CSV reader is `src/parsers/csv_reader.py`; the OFX reader is `src/parsers/ofx.py`. Both yield `Transaction` records and never touch the database.
2. **Reconciliation** — `src/reconcile.py` matches each transaction with an open invoice by amount and date window.
3. **Export** — `src/export.py` writes the reconciled transactions of a period in the requested format.

The readers are the only place a bank-specific quirk is handled; reconciliation and export see normalized records only.
