# CLAUDE.md — shop-pricing-lib

A tiny Node.js library computing order prices. No framework, no build step.

## Commands

- Test: `npm test` — a plain Node script under `test/`, using the built-in `assert` module; a failed assertion throws and the process exits non-zero.
- Lint: `npm run lint` — no-op placeholder, this project has no linter configured yet.

## Conventions

- Source lives in `src/`, one file per topic: `money.js` holds the currency helpers, `pricing.js` builds the prices on top of them.
- Tests live in `test/`, one file per source file that computes a price, required with a relative path.
- Keep functions small and dependency-free — no external packages.
