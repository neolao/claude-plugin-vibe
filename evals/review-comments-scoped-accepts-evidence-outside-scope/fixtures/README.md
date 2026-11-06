# supplier-sync

Pulls pending orders from the supplier gateway into the local queue.
`sync/` is the polling loop, `gateway/` the HTTP client, `config/` the
settings, `workers/` the scheduler that runs the loop every ten minutes.
