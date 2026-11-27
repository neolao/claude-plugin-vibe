# Ubiquitous Language

## Statement
A file exported by a bank, listing the movements of one account over a period; the input of an import, parsed into transactions.
**Do not confuse with:** Invoice — a document Ledger matches transactions against, never imported from a bank
_Sources: `src/parsers/csv_reader.py`_

## Invoice
A bill issued or received by the business, with an amount, a date and a reference; an open invoice waits for a transaction to be matched with it.
**Do not confuse with:** Statement — the bank's file, which lists transactions and never invoices
_Sources: `src/reconcile.py`_

## Reconciliation
The matching of an imported transaction with an open invoice, by amount and date window; a transaction is reconciled once an invoice is attached to it.
**Do not confuse with:** Export — the file written for the accountant from reconciled transactions, which changes no match
_Sources: `src/reconcile.py`_

## Export
The file written for the accountant from the reconciled transactions of a period, in CSV or XLSX.
**Do not confuse with:** Reconciliation — the matching itself, which the export only reads
_Sources: `src/export.py`_
