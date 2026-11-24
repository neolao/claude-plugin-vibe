# billing

Order billing service. `billing/` holds the flows: charging an order at
checkout, refunding one from the support console, fetching invoices for the
nightly reconciliation job, and posting ledger entries. `db/` wraps the
database connection, `net/` holds the HTTP helpers shared by every service,
`gateway/` is the payment provider's client, `locks/` the in-process locking
helpers, and `common/` the exception types shown to the support console.
