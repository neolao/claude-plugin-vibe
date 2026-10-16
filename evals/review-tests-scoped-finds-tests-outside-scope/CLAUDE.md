# CLAUDE.md — ledger

## Project overview

A small Node.js module under `fixtures/`: invoice totals in `src/billing/`,
delivery rates in `src/shipping/`. No third-party dependencies: tests use the
built-in `node:test` runner.

## Testing conventions

From `fixtures/`, run the suite with `npm test`. There is no separate e2e or
integration script.
