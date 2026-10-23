# CLAUDE.md — tiny-pub-lib

## Project overview

`tiny-pub-lib` is a tiny standalone Node.js library (`greet.js`) exporting a
single `greet(name)` function. No build step, no framework, no dependencies.
It is hosted on GitHub (`origin`).

## Testing conventions

Run tests: `npm test`
Run lint: `npm run lint`

No run or dev command: this is a library, not a service — there is nothing
to start.

## Commands

- GitHub CLI: this sandbox has no global `gh` install. A stand-in with the same `auth status` / `release create` / `release view` / `run list` interface lives at `./bin/gh` — invoke it as `./bin/gh ...`, or `PATH="$PWD/bin:$PATH" gh ...`, wherever a command would normally read `gh`.
- Git: `origin` is the GitHub repository; its push URL (`git remote -v`) is a local mirror inside the workspace, so pushes work without network. This sandbox has no network: nothing can be fetched from GitHub here.

## Constraints

- Keep the library dependency-free (no `node_modules`, no external packages).
