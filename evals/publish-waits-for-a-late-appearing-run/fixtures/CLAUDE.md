# CLAUDE.md — fixture-app

A tiny fixture app deployed to GitHub Pages via a GitHub Actions workflow (`.github/workflows/deploy.yml`) on every push to `main`.

## Commands

- GitHub CLI: this sandbox has no global `gh` install. A stand-in with the same `auth status` / `run list` / `run view` interface lives at `./bin/gh` — invoke it as `./bin/gh ...`, or `PATH="$PWD/bin:$PATH" gh ...`, wherever a command would normally read `gh`.
