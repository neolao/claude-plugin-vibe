# supplier-sync

Pulls pending orders from the supplier gateway into the local queue.
`sync/` is the polling loop, `gateway/` the HTTP client, `config/` the
settings; the scheduler runs `python -m sync.poller` every ten minutes.
