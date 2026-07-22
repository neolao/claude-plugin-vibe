# claude-plugin-vibe

A Claude Code plugin for **vibe coding**: the human stays Product Owner only — describing requirements and evaluating outcomes — while Claude writes, tests, reviews, and ships the code. All quality assurance is automated (TDD, lint, multi-agent review); nothing is meant to be tested manually.

**Website:** [neolao.github.io/claude-plugin-vibe](https://neolao.github.io/claude-plugin-vibe/) — animated terminal demos of the workflow.

## Features

<!-- vibe:begin:features -->
- Automated, TDD-first workflow: implement features and fix bugs with tests written first, in the human's stead, actively checked against writing tests that can't actually fail (tautological tests)
- Work is always committed before ending a turn, even if interrupted, so nothing is silently lost across a session reset
- Every feature or fix is proven to actually work after implementation — exercised for real, nominal path plus an edge case or error path, instead of just trusting green tests; it works out how to launch the app on its own, even on an unusual project setup, before giving up
- A backlog to queue feature ideas before implementation — items are committed automatically as they're added, singly or in bulk — with automatic detection when a request bundles several independent capabilities so it can be split into separate items; items can also be removed on demand (after confirmation), and picked up directly by number when implementing a feature or a fix
- Multi-agent code review covering anti-patterns, architecture, complexity, DDD, dependencies, hexagonal architecture (ports & adapters, for projects that chose it), hygiene, naming, overengineering, performance, robustness, security, simplicity, SOLID principles, tests (including real execution of the suite and aggressive flagging of tests that can't actually fail), web security, and dynamic penetration testing against a locally-run instance of the app — every check belongs to exactly one agent, so the same issue is never reported twice — with a color-coded status line while it runs
- Feedback loops that close themselves: test failures that predate a piece of work are offered for backlog tracking instead of being forgotten, a reminder appears once several changes have shipped without a review, the set of active review agents is re-checked against the project's current shape at every review (a project that grows an HTTP surface automatically gains the web audits — deliberate opt-outs are never overridden), and every dead end (three failed self-correction attempts) is logged with its diagnosis so the next session doesn't rediscover it from scratch
- Every workflow keeps tracking its progress and announces it clearly even in environments where the dedicated task system isn't available, instead of surfacing a confusing error
- An internal codebase context map kept in sync automatically, so Claude ramps up fast on any session
- A self-maintaining project glossary: definitions are derived from how the code actually uses each concept and carry their sources; terms whose subject disappeared from the code or that never belonged to the business vocabulary are removed automatically at each sync — no manual editing or confirmation ever needed
- Changelog maintenance from git history, following Keep a Changelog
- README and developer documentation kept current automatically — as many documents (with diagrams where they help) as the project needs for a new developer to understand it, with an index linking every doc file
- A one-command versioned release: changelog finalized, docs refreshed, version bumped, commit and tag created
- A public website with looping animated terminal demos of the workflow, mobile-friendly, served straight from the repository with no build step
<!-- vibe:end:features -->

## Requirements

[Claude Code](https://claude.com/claude-code) with plugin support — if the `/plugin` command is not recognized, update Claude Code to the latest version.

## Installation

<!-- vibe:begin:install -->
Add the marketplace, then install the plugin, from within Claude Code:

```
/plugin marketplace add neolao/claude-plugin-vibe
/plugin install vibe
```

Verify the install with `/plugin list` — `vibe` should appear as enabled, and the `/vibe:*` commands become available.

To update later, refresh the marketplace and reload:

```
/plugin marketplace update vibe
/reload-plugins
```

To uninstall:

```
/plugin uninstall vibe
```
<!-- vibe:end:install -->

## Usage

<!-- vibe:begin:usage -->
Each command is invoked as a Claude Code slash command, with natural-language arguments where relevant:

```
/vibe:init
/vibe:backlog "Add a dark mode toggle to the settings page"
/vibe:backlog remove 003
/vibe:feature "Add a dark mode toggle to the settings page"
/vibe:feature 003
/vibe:fix "Login form submits twice when pressing Enter"
/vibe:fix 003
/vibe:review
/vibe:review src/auth/
/vibe:sync
/vibe:changelog
/vibe:changelog 1.2.0
/vibe:docs
/vibe:docs --full
/vibe:release patch
/vibe:release 1.2.0
```

`/vibe:backlog` with no argument lists pending items instead of adding one; `remove NNN` deletes an active item after confirmation. `/vibe:feature` and `/vibe:fix` accept either a natural-language description or a backlog item number — the item is then marked done automatically once shipped. `/vibe:review` with no path reviews the full codebase. `/vibe:changelog` and `/vibe:release` accept an explicit version (or `major`/`minor`/`patch` for `/vibe:release`) — omit it to keep entries under `[Unreleased]` or let `/vibe:release` infer the bump from them.
<!-- vibe:end:usage -->

## Skills (commands)

| Command | Purpose |
|---|---|
| `/vibe:init` | Initialize or regenerate the project's `CLAUDE.md` for vibe coding |
| `/vibe:backlog` | List or add feature backlog items (`.vibe/backlog/`) |
| `/vibe:feature` | Implement a new feature using TDD, then update the changelog |
| `/vibe:fix` | Fix a bug using TDD (reproduce first), then update the changelog |
| `/vibe:review` | Run a multi-agent code quality review and auto-apply fixes |
| `/vibe:sync` | Generate/update `.vibe/` — the codebase context map |
| `/vibe:changelog` | Update `CHANGELOG.md` from git history |
| `/vibe:docs` | Generate/refresh README managed sections and developer docs in `docs/` (diagrams included) |
| `/vibe:release` | Bump version, finalize the changelog, commit and tag a release |

## Review agents

`/vibe:review` orchestrates these specialized agents in parallel:

- `review-antipatterns`, `review-architecture`, `review-complexity`, `review-ddd`, `review-dependencies`, `review-hexagonal`, `review-hygiene`, `review-naming`, `review-overengineering`, `review-pentest`, `review-performance`, `review-robustness`, `review-security`, `review-simplicity`, `review-solid`, `review-tests`, `review-web-security`

Each focuses on one dimension only (see `/vibe:init`'s "Review agents" table for activation rules per project).

## Subagent status line

The plugin ships a `subagentStatusLine` (`settings.json` + `scripts/subagent-statusline.sh`), applied automatically once the plugin is enabled. It replaces the default `name · description · token count` row in the agent panel with a compact, color-coded line (status icon, bold name, description, token count) — most visible during `/vibe:review`, which runs up to 17 review agents in parallel.

## Typical flow

1. `/vibe:init` once, to set up `CLAUDE.md` and `.vibe/`
2. `/vibe:backlog "some feature idea"` to queue work
3. `/vibe:feature 001` (or `/vibe:fix "bug description"`) to implement, TDD-first
4. `/vibe:review` periodically to catch quality issues
5. `/vibe:release patch|minor|major` to ship a version

`/vibe:init` and `/vibe:sync` generate `CLAUDE.md` and the `.vibe/` context map inside *your* project — both are meant to be committed with it, so every session (and every teammate) starts from the same conventions and codebase map.

## Documentation

<!-- vibe:begin:docs-index -->
- [docs/architecture.md](docs/architecture.md) — the plugin's moving parts (skills, review agents, status line, manifests) and how they connect, with a component diagram
- [docs/development.md](docs/development.md) — how to work on the plugin itself: conventions, frontmatter shapes, the no-tests-by-design policy, and the release process
- [docs/website.md](docs/website.md) — how the demo website works: scripted terminal demos, deployment, and the pitfalls not to reintroduce
- [docs/workflows.md](docs/workflows.md) — the lifecycles behind the commands (feature/fix flow, backlog items, self-correction and escalation, review feedback loops), with diagrams
<!-- vibe:end:docs-index -->

## License

[MIT](LICENSE)
