# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `/vibe:backlog` and `/vibe:feature` now detect when a request bundles several independent capabilities and propose splitting it into separate backlog items instead of one oversized task

## [0.1.0] - 2026-07-07

### Added

- Plugin manifest for the Claude Code marketplace, enabling installation via `/plugin marketplace add` + `/plugin install vibe`
- `/vibe:init` — initialize or regenerate a project's `CLAUDE.md` for vibe coding (TDD-first, automated QA, human as Product Owner only)
- `/vibe:backlog` — list or add feature backlog items
- `/vibe:feature` — implement a new feature using TDD
- `/vibe:fix` — fix a bug using TDD, reproducing it first
- `/vibe:review` — run a multi-agent code quality review covering architecture, complexity, DDD, dependencies, hygiene, naming, performance, robustness, security, and SOLID principles
- `/vibe:review-tests` — audit the test suite for coverage gaps and test quality
- `/vibe:review-web-security` — audit a web app for exploitable vulnerabilities
- `/vibe:sync` — generate and keep an internal codebase context map up to date
- `/vibe:changelog` — maintain `CHANGELOG.md` from git history
- `/vibe:docs` — generate and refresh README documentation and a `docs/` folder, including an index that keeps every doc file linked from the README
- `/vibe:release` — versioned release workflow (changelog finalization, docs refresh, version bump, commit and tag)
- A color-coded subagent status line shown in the agent panel during multi-agent reviews
- Installation instructions and an MIT license

[Unreleased]: https://github.com/neolao/claude-plugin-vibe/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/neolao/claude-plugin-vibe/releases/tag/v0.1.0
