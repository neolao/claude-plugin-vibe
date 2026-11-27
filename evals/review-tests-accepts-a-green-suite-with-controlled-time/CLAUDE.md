# CLAUDE.md — ledger-service

## Project overview

A small Python service: transfer fees, an account ledger and expiring
access tokens, covered by `unittest`-style tests under `fixtures/`.

## Testing conventions

Run the whole suite with `python3 -m unittest discover -s fixtures -v`
(no third-party test runner is installed). There is no separate e2e or
integration script — everything here is a fast unit test.
