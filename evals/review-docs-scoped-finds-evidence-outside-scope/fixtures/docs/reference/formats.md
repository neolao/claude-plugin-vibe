# File formats

## CSV

A header row, then one transaction per line: `date,label,amount,currency`. Dates are ISO 8601. The separator is a comma; a semicolon is accepted on import when the header uses it.

## OFX

OFX 1.x and 2.x statements are read as exported by most banks. Only the `STMTTRN` records are used.

## XLSX

One sheet per period, one row per reconciled transaction, with the columns of the CSV export plus the invoice reference.
