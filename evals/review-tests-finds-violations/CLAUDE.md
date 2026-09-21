# CLAUDE.md — calc-service

## Project overview

A small Python service: a calculator helper and a user service, both covered by
`unittest`-style tests under `fixtures/`.

## Testing conventions

Run the whole suite with `python3 -m unittest discover -s fixtures -v`
(no third-party test runner is installed). There is no separate e2e or
integration script — integration-level checks live in the same suite and are
recognised by their `Infrastructure` class names.
