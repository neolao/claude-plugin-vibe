# dockside

Carrier pickup back end of a warehouse. A **consignment** is the set of
parcels one carrier collects in one visit; the warehouse closes it when the
driver arrives, and parcels scanned after that go to the next one.
`logistics/` holds the consignment model and its storage, `api/` the Flask
routes the warehouse terminal calls, `reports/` the end-of-day summary.
