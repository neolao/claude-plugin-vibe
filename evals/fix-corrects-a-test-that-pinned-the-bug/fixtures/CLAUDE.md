# CLAUDE.md — game-timer-lib

A tiny Node.js library formatting the countdown shown above the game board. No framework, no build step.

## Commands

- Test: `npm test` — a plain Node script under `test/`, using the built-in `assert` module; a failed assertion throws and the process exits non-zero.
- Lint: `npm run lint` — no-op placeholder, this project has no linter configured yet.

## Conventions

- Source lives in `src/`, one file per topic; tests live in `test/`, one file per source file (`test/<name>.test.js`), required with a relative path.
- Keep functions small and dependency-free — no external packages.
