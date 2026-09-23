# claude-plugin-vibe

A Claude Code plugin for **vibe coding**: the human stays Product Owner only — describing requirements and evaluating outcomes — while Claude writes, tests, reviews, and ships the code. All quality assurance is automated (TDD, lint, multi-agent review); nothing is meant to be tested manually.

**Website:** [neolao.github.io/claude-plugin-vibe](https://neolao.github.io/claude-plugin-vibe/) — animated terminal demos of the workflow.

## Features

<!-- vibe:begin:features -->
- TDD first: tests are written before the code, in the human's stead, and checked against tests that cannot fail (tautological tests)
- Every feature or fix is exercised for real after implementation — nominal path plus an edge case — instead of trusting green tests
- The project's real build is checked again right before shipping and right before cutting a release, not just once at the start, so a build that stops compiling never slips through
- Work is always committed before a turn ends, even on interruption
- A backlog of numbered items, committed as they are added, singly or in bulk; a request bundling several capabilities is split into separate items; any item is implemented by number
- A round-by-round interview settles a plan, idea, or decision that is too thin to act on — on demand, or automatically when a backlog item, a new project, or a new workspace lacks substance
- An autonomous mode that works the backlog with no question or approval step, one item at a time in isolation, resuming exactly where it stopped after any interruption; dead ends are set aside with their reason; `--push` also publishes the result
- Eight domain experts (UI/UX, visual design, REST API, CLI, data, Linux, operations, real-time rendering) consulted while planning, contributing the requirements a Product Owner would not think to state — and asking back when a real product decision in their domain is left open
- A fourteen-agent code review — anti-patterns, architecture (including ports & adapters where adopted), DDD, dependencies, hygiene, naming, overengineering, performance, robustness, security, simplicity, SOLID, tests (with real execution of the suite), and web security (with an opt-in dynamic probe of a locally-run instance) — one owner per check, fixes applied automatically
- Feedback loops that close themselves: pre-existing test failures offered for tracking, a review reminder after several unreviewed changes, active review agents re-checked against the project's shape at every run, every dead end logged with its diagnosis
- Progress shown as one compact status line per step, even where the dedicated task system is unavailable
- An internal codebase context map and a self-maintaining, code-derived glossary kept in sync automatically
- A per-project language for docs, backlog items, and comments, asked once
- Changelog maintenance from git history (Keep a Changelog), README and developer docs kept current, and a one-command versioned release
- Multi-repo workspaces: one command sets up a hub repo tracking every sibling, another picks the next eligible task across them, implements it, then pushes and releases — the only place in the workflow that publishes
- Publishing checks the actual deployment result, not just that the push succeeded, and flags a broken deploy clearly instead of quietly moving on to the next piece of work
- Generated files and reports use short, plain sentences
- A public website with animated terminal demos, served straight from the repository
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
Each command is a Claude Code slash command, with natural-language arguments where relevant:

```
/vibe:init
/vibe:clarify "should we support multi-tenant billing"
/vibe:backlog "Add a dark mode toggle to the settings page"
/vibe:backlog remove 003
/vibe:feature "Add a dark mode toggle to the settings page"
/vibe:feature 003
/vibe:fix "Login form submits twice when pressing Enter"
/vibe:fix 003
/vibe:auto
/vibe:auto 3 --push
/vibe:review
/vibe:review src/auth/
/vibe:sync
/vibe:changelog
/vibe:docs
/vibe:docs --full
/vibe:release patch
/vibe:release 1.2.0
/vibe:workspace-init
/vibe:next-task
/vibe:next-task auto 1
```

- `/vibe:clarify` interviews you round by round about the subject you give it (or the one under discussion) and stops once every open question is settled. `/vibe:backlog`, `/vibe:init`, and `/vibe:workspace-init` trigger it automatically when their input is too thin.
- `/vibe:backlog` with no argument lists pending items. `remove NNN` deletes an active item after confirmation.
- `/vibe:feature` and `/vibe:fix` take a description or a backlog number; the item is closed automatically once shipped.
- `/vibe:auto` works the backlog with no approval step: with no argument until nothing is eligible, with a number for that many items. Run it again after an interruption to resume. `--push` publishes at the end. Pair it with `/loop 45m /vibe:auto` to keep going unattended, or `/loop 30m /vibe:auto 1` to space items apart.
- `/vibe:review` with no path reviews the full codebase.
- `/vibe:changelog` brings `[Unreleased]` up to date from git history. `/vibe:release` takes a version or `major`/`minor`/`patch`, or suggests the bump from the changelog when run without an argument.
- `/vibe:workspace-init`, run from the parent folder of several sibling repos, sets up or refreshes a hub repo tracking them. `/vibe:next-task` then picks the next eligible task across every active repo (or in the current repo alone), implements it, and pushes and releases. Alone it picks and confirms; `auto [N]` skips confirmation and suits `/loop`.
<!-- vibe:end:usage -->

## Skills (commands)

| Command | Purpose |
|---|---|
| `/vibe:init` | Initialize or regenerate the project's `CLAUDE.md` and `README.md` for vibe coding |
| `/vibe:backlog` | List, add, or remove feature backlog items (`.vibe/backlog/`) |
| `/vibe:clarify` | Interview the user round by round until a plan, idea, or decision is fully settled |
| `/vibe:feature` | Implement a new feature using TDD, then update the changelog |
| `/vibe:fix` | Fix a bug using TDD (reproduce first), then update the changelog |
| `/vibe:auto` | Work the backlog autonomously — no human gates, resumes after any interruption, `--push` publishes |
| `/vibe:review` | Run a multi-agent code quality review and auto-apply fixes |
| `/vibe:sync` | Generate/update `.vibe/` — the codebase context map |
| `/vibe:changelog` | Update `[Unreleased]` in `CHANGELOG.md` from git history |
| `/vibe:docs` | Generate/refresh README managed sections and developer docs in `docs/` (diagrams included) |
| `/vibe:release` | Bump version, finalize the changelog, commit and tag a release |
| `/vibe:workspace-init` | Bootstrap/refresh a multi-repo workspace's hub repo and local workspace-root `CLAUDE.md` |
| `/vibe:next-task` | Pick the next eligible task across a workspace (or the current repo), implement it, then push and release |

Two internal skills are hidden from the `/` menu: `vibe:tasks` (task-list creation with a scratchpad fallback) and `vibe:publish` (push and release, used by `/vibe:auto --push` and `/vibe:next-task`).

## Review agents

`/vibe:review` orchestrates these specialized agents in parallel, each owning one dimension:

- `review-antipatterns`, `review-architecture` (also ports & adapters, for projects that adopted them), `review-ddd`, `review-dependencies`, `review-hygiene`, `review-naming`, `review-overengineering`, `review-performance`, `review-robustness`, `review-security`, `review-simplicity`, `review-solid`, `review-tests`, `review-web-security` (with an opt-in dynamic verification mode against a locally-run instance)

Activation per project is recorded in the `CLAUDE.md` table written by `/vibe:init`.

## Expert agents

`/vibe:feature` and `/vibe:fix` consult up to 3 of these prescriptive experts while planning, based on what the task touches — each can also answer one precise question during implementation:

- `expert-ui-ux`, `expert-frontend-design`, `expert-api-rest`, `expert-cli-dx`, `expert-data`, `expert-linux`, `expert-ops`, `expert-realtime-rendering`

Experts prescribe requirements *before* the code exists; the review agents critique *after*. The two families cover disjoint domains, with one documented exception: `expert-realtime-rendering` is paired with `review-performance`, because rendering choices are hard to retrofit once the code is written.

## Subagent status line

The plugin ships a `subagentStatusLine` (`settings.json` + `scripts/subagent-statusline.sh`), applied automatically once the plugin is enabled. It replaces the default `name · description · token count` row in the agent panel with a compact, color-coded line — most visible during `/vibe:review`, which runs up to 14 agents in parallel.

## Typical flow

1. `/vibe:init` once, to set up `CLAUDE.md` and `.vibe/`
2. `/vibe:backlog "some feature idea"` to queue work
3. `/vibe:feature 001` (or `/vibe:fix "bug description"`) to implement, TDD-first, with the matching experts weighing in on the plan; or `/vibe:auto` to work the whole backlog without supervision
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
