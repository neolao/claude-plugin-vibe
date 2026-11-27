# Configuration

Settings are read from `ledger.toml` at the project root. The legacy `ledger.ini` is still read when `ledger.toml` is absent, with the same keys; new installs get a `ledger.toml` only.

## Server inbox

On the server, statements are picked up from `/var/lib/ledger/inbox/` every ten minutes and imported as if given on the command line; a file is moved to `/var/lib/ledger/done/` once its import succeeds.

## Keys

| Key | Meaning | Default |
|---|---|---|
| `window_days` | how far apart a transaction and its invoice may be | 7 |
| `currency` | the currency assumed when a statement gives none | `EUR` |
