# importer

Command-line tool the `importer` service account runs every night:
`importer ingest /srv/uploads/<file>` unpacks the price list a supplier
uploaded over SFTP — the supplier chooses the file name — into
`/srv/pricelists` and loads it. Hooks run after each ingest come from
`/etc/importer/hooks.pkl`, which any member of the `ops` group edits.
