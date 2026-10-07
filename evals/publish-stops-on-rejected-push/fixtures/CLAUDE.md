# CLAUDE.md — tiny-pub-lib

## Project overview

`tiny-pub-lib` is a tiny standalone Node.js library (`greet.js`) exporting a
single `greet(name)` function. No build step, no framework, no dependencies.

## Testing conventions

Run tests: `npm test`
Run lint: `npm run lint`

No run or dev command: this is a library, not a service — there is nothing
to start.

## Constraints

- Keep the library dependency-free (no `node_modules`, no external packages).
