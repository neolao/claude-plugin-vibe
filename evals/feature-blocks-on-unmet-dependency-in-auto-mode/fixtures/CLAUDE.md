# CLAUDE.md — reports-lib

A tiny Node.js library that formats sales reports. No framework, no build step.

## Commands

- Test: `npm test` — plain Node scripts under `test/`, using the built-in `assert` module; a failed assertion throws and the process exits non-zero.
- Lint: `npm run lint` — no-op placeholder, this project has no linter configured yet.

## Conventions

- Source lives in `src/`, one file per topic; tests live in `test/`, one file per source file (`test/<name>.test.js`), required with a relative path.
- Keep functions small and dependency-free — no external packages.
