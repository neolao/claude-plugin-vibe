# CLAUDE.md — ledger

## Project overview

A small Python package under `fixtures/`: invoice totals in `billing/`,
delivery rates in `shipping/`, the whole suite in `tests/`.

## Testing conventions

Run the suite with `python3 -m unittest discover -s fixtures/tests -t fixtures -v`
(no third-party test runner is installed). There is no separate e2e or
integration script.
