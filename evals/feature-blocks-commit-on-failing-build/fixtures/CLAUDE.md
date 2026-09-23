# CLAUDE.md — roster-lib

A tiny Node.js library tracking a sports team roster's scores. No framework, no bundler.

## Commands

- Test: `npm test` — plain Node scripts under `test/`, using the built-in `assert` module; a failed assertion throws and the process exits non-zero.
- Lint: `npm run lint` — no-op placeholder, this project has no linter configured yet.
- Build: `npm run build` — the project's real build step; must exit 0 before shipping.

## Conventions

- Source lives in `src/`, one file per topic; tests live in `test/`, one file per source file (`test/<name>.test.js`), required with a relative path.
- Every exported function validates its input and throws a clear `Error` with a descriptive message instead of returning `NaN`, `undefined`, or silently producing a wrong result.
- Keep functions small and dependency-free — no external packages.
