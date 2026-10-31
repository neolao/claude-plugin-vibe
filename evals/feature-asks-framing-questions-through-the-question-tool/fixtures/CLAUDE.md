# CLAUDE.md — shop-cart

A tiny Node.js library computing order totals for the shop's checkout page. No framework, no build step.

## Commands

- Test: `npm test` — plain Node scripts under `test/`, using the built-in `assert` module; a failed assertion throws and the process exits non-zero.
- Lint: `npm run lint` — no-op placeholder, this project has no linter configured yet.

## Conventions

- Source lives in `src/`, one file per topic; tests live in `test/`, one file per source file (`test/<name>.test.js`), required with a relative path.
- Amounts are integer cents everywhere; nothing is rounded before the final total.
- Keep functions small and dependency-free — no external packages.
