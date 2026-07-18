# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.5.0] - 2026-07-19

### Added

- `/vibe:review` no longer trusts a stale agent table: at each run it re-checks every activation condition against the current state of the project — a CLI that grew an HTTP API automatically gains the web audits, and an audit whose surface disappeared is turned off — while reasons recording a deliberate choice are never overridden; every change is applied to the table, listed in the review report, and committed with the run
- A new `hexagonal` review agent auditing ports & adapters compliance — port ownership, technology leaking through port contracts, business logic in adapters, wiring outside the composition root — activated only for projects that explicitly follow a hexagonal architecture (declared in an ADR or `CLAUDE.md`, or evident from the structure), since not every project lends itself to it

## [1.4.0] - 2026-07-19

### Added

- Four new review agents orchestrated by `/vibe:review`: `antipatterns` (named, recognizable anti-patterns such as god objects and primitive obsession), `simplicity` (expression-level convolution), `overengineering` (design-level YAGNI enforcement), and `pentest` (dynamic penetration testing that proves vulnerabilities against a locally-run instance of the app)

### Fixed

- The web security audit is no longer a standalone `/vibe:review-web-security` command, inconsistent with the other review dimensions — it is now a review agent orchestrated by `/vibe:review`, activated per project like the rest
- Review agents no longer compete over the same checks: every finding that two agents used to claim (positional boolean parameters, stdlib reimplementation, skipped tests, primitive obsession, path traversal and IDOR on HTTP routes, unbounded caches, god objects) now has a single owning agent, and the other one explicitly delegates to it — reviews produce fewer duplicate findings

## [1.3.0] - 2026-07-18

### Added

- A public website showcasing the plugin — its benefits, every command, and the flagship skills replayed as looping animated terminal demos — at <https://neolao.github.io/claude-plugin-vibe/>, served straight from the repository with no build step

### Changed

- The README now states the requirements, shows how to verify an install and how to update or uninstall the plugin, includes a web-security usage example, and explains which generated files are meant to be committed

### Fixed

- The website displays correctly on phones: the commands table turns into stacked cards on small screens, and a stray horizontal page scroll was eliminated

## [1.2.0] - 2026-07-18

### Added

- Pre-existing test failures spotted before starting a feature or a fix are no longer forgotten: at the end of the run, `/vibe:feature` and `/vibe:fix` propose recording them as a backlog item (unless one already tracks them)
- Review cadence reminder: `/vibe:review` now records each run in `.vibe/last-review.md`, and `/vibe:feature`, `/vibe:fix` (after 5 or more changes) and `/vibe:backlog` (in the list view) remind when it's time to run a review again
- Escalation memory: when a self-correction loop gives up after 3 attempts, `/vibe:feature`, `/vibe:fix` and `/vibe:review` now record the diagnosis in an append-only log (`.vibe/escalations.md`), which `/vibe:feature` and `/vibe:fix` consult at the start of every run — a dead end hit in one session is not rediscovered from scratch in the next
- `/vibe:backlog remove NNN` — remove an active backlog item after explicit confirmation, cleaning up any `depends_on` references pointing to it (done items are kept as history and cannot be removed)
- `/vibe:fix` now accepts a backlog item reference (`/vibe:fix NNN`), just like `/vibe:feature`: the item is resolved, its dependencies checked, marked in progress during the fix, and moved to done once the fix is committed — useful for bug items created from a review

### Changed

- `/vibe:review` no longer enumerates every file up front — it now passes the scope and exclusion list to each review agent, which scans the code itself, making review startup lighter
- `/vibe:feature` no longer carries a duplicated duplicate-check instruction (the dedicated Duplicate check section already covers it)

### Fixed

- The architecture review agent now checks the decisions recorded in the current ADR format (`.vibe/decisions/NNN-slug.md`); it previously only read the legacy single-file `.vibe/decisions.md`, so decisions recorded by `/vibe:feature` were silently ignored during reviews
- `/vibe:sync` no longer generates broken relative links in the `.vibe/index.md` it produces (links pointed to `.vibe/...` from inside `.vibe/` itself)

## [1.1.3] - 2026-07-10

### Fixed

- `/vibe:backlog` now commits newly created backlog items automatically (single item, batch, or from a review) instead of leaving them uncommitted

## [1.1.2] - 2026-07-10

### Fixed

- `/vibe:feature` and `/vibe:fix` now always commit modified files before ending their turn, no matter how the conversation unfolds (plan rejected, clarifying question, escalation), instead of only committing at the very end of a fully successful run — this prevents uncommitted work from being silently lost across `/clear` between sessions

## [1.1.1] - 2026-07-10

### Fixed

- `/vibe:feature` and `/vibe:fix` now actively check that tests written during implementation can't just pass no matter what (tautological tests), and `/vibe:review`'s test reviewer now hunts for and flags these tests more aggressively, always at high severity

## [1.1.0] - 2026-07-09

### Changed

- `/vibe:feature` and `/vibe:fix` now fall back to the native `run-skill-generator` skill when `verify` fails 3 times purely on launch mechanics (build errors, crash on start) rather than on the behavior under test, before escalating to the user

## [1.0.0] - 2026-07-09

### Added

- `agents/review-tests.md` — test-suite review is now a first-class `/vibe:review` subagent that actually executes the project's test suite (including isolated e2e/integration runs) to ground findings in real pass/fail evidence, not just static reading

### Removed

- `/vibe:review-tests` standalone command — folded into `/vibe:review` (see Added)

## [0.2.0] - 2026-07-09

### Added

- `/vibe:backlog` and `/vibe:feature` now detect when a request bundles several independent capabilities and propose splitting it into separate backlog items instead of one oversized task

### Changed

- `/vibe:feature` and `/vibe:fix` now delegate runtime verification to the native `verify` skill and adopt an adversarial "assume it's broken" posture, exercising the nominal path plus an edge case or error path for real instead of a single happy-path run

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

[Unreleased]: https://github.com/neolao/claude-plugin-vibe/compare/v1.5.0...HEAD
[1.5.0]: https://github.com/neolao/claude-plugin-vibe/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/neolao/claude-plugin-vibe/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/neolao/claude-plugin-vibe/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/neolao/claude-plugin-vibe/compare/v1.1.3...v1.2.0
[1.1.3]: https://github.com/neolao/claude-plugin-vibe/compare/v1.1.2...v1.1.3
[1.1.2]: https://github.com/neolao/claude-plugin-vibe/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/neolao/claude-plugin-vibe/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/neolao/claude-plugin-vibe/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/neolao/claude-plugin-vibe/compare/v0.2.0...v1.0.0
[0.2.0]: https://github.com/neolao/claude-plugin-vibe/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/neolao/claude-plugin-vibe/releases/tag/v0.1.0
