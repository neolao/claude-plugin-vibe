# importer

Command-line tool the `importer` service account runs every night:
`importer ingest <YYYY-MM-DD>` unpacks that day's price list into
`/srv/pricelists` and loads it. The SFTP server stores each supplier
upload as `/srv/uploads/<YYYY-MM-DD>.zip`, named after the day it
arrived. `/var/cache/importer/` holds the tool's cache of the last price
list; only the tool writes there.
