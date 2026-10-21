# claude-plugin-vibe

A Claude Code plugin for **vibe coding**: the human stays Product Owner only — describing requirements and evaluating outcomes — while Claude writes, tests, reviews, and ships the code. All quality assurance is automated (TDD, lint, multi-agent review); nothing is meant to be tested manually.

**Website:** [neolao.github.io/claude-plugin-vibe](https://neolao.github.io/claude-plugin-vibe/) — animated terminal demos of the workflow.

## Features

<!-- vibe:begin:features -->
- TDD first: tests are written before the code, in the human's stead, and checked against tests that cannot fail (tautological tests)
- Every feature or fix is exercised for real after implementation — nominal path plus an edge case — instead of trusting green tests
- Before anything is built, the need and then the implementation are each framed in their own pass: the backlog item, the project notes and the code are read first, and you are asked only what none of them answers; every answer found alone says where it comes from, and a question that would take research is flagged instead of guessed
- Every feature and fix reviews its own change before shipping: twenty review agents — anti-patterns, architecture (including ports & adapters where adopted), comments, coordination, correctness (every bug comes with its triggering scenario), DDD, dependencies, documentation consistency, hygiene, naming, overengineering, performance, robustness, security, signatures, simplicity, SOLID, tests (with real execution of the suite), web security (with an opt-in dynamic probe) and an opt-in alternative-design pass — plus a check of the result against the request; a classifier re-checks each finding against the code, drops false positives, and says whether it questions what was asked or how it was done, so the work goes back to the right drawing board until only minor points remain. You see the result, never the findings
- The report of every feature and fix is checked before you read it: each claim is verified against the commands actually run, then the text is made readable without losing a fact
- The project's real build is checked again right before shipping and right before cutting a release, not just once at the start, so a build that stops compiling never slips through
- Work is always committed before a turn ends, even on interruption
- A backlog of numbered items, committed as they are added, singly or in bulk; a request bundling several capabilities is split into separate items; any item is implemented by number
- Every settled decision carries a priority (must / should / nice) that arbitrates conflicts during implementation, and work stops to ask before stepping outside the approved plan
- An end-of-task debrief that becomes project memory, and corrections stated in general terms turned into global rules
- An autonomous mode that works the backlog with no question or approval step, one item at a time in isolation, resuming exactly where it stopped after any interruption; dead ends are set aside with their reason; `--push` also publishes the result
- Nine domain experts (UI/UX, visual design, REST API, CLI, data, Linux, operations, real-time rendering, software architecture) consulted while planning, contributing the requirements a Product Owner would not think to state — and asking back when a real product decision in their domain is left open; the architecture expert names a baseline and scores the alternatives before a line is written
- Any expert can be asked a precise question on demand, and a settled decision can be put through a devil's advocate before it is executed
- Feedback loops that close themselves: pre-existing test failures offered for tracking, active review agents re-checked against the project's shape at every run, every dead end logged with its diagnosis
- A usage report per run — bricks called, rounds, questions, findings, fixes — as plain statistics kept on your machine; sharing it with the plugin's maintainers is your choice, and the only way real usage reaches their evals
- Progress shown as one compact status line per step, even where the dedicated task system is unavailable — there, a small script keeps a structured task file and enforces the same transition rules
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
/vibe:audit
/vibe:challenge "we picked PostgreSQL over SQLite for the desktop app"
/vibe:consult architecture "where should the export pipeline live"
/vibe:backlog "Add a dark mode toggle to the settings page"
/vibe:backlog remove 003
/vibe:feature "Add a dark mode toggle to the settings page"
/vibe:feature 003
/vibe:fix "Login form submits twice when pressing Enter"
/vibe:fix 003
/vibe:auto
/vibe:auto 3 --push
/vibe:debrief
/vibe:learn
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

- `/vibe:backlog` with no argument lists pending items. `remove NNN` deletes an active item after confirmation. A description too thin to act on triggers a round-by-round interview first; so does a vague project idea in `/vibe:init` or a first `/vibe:workspace-init`.
- `/vibe:feature` and `/vibe:fix` take a description or a backlog number; the item is closed automatically once shipped. Each run frames what is needed, then how to build it, asking you only what no source answers; builds test-first; reviews its own change and goes back to the drawing board until only minor points remain; checks its report before you read it. You see the plan, the questions, and the result — never a finding.
- `/vibe:auto` works the backlog with no approval step: with no argument until nothing is eligible, with a number for that many items. Run it again after an interruption to resume. `--push` publishes at the end. Pair it with `/loop 45m /vibe:auto` to keep going unattended, or `/loop 30m /vibe:auto 1` to space items apart.
- `/vibe:audit` reviews the whole codebase (or a path) with the active review agents, reports the classified findings, then creates backlog items for the ones you pick; it fixes nothing. `/vibe:init` offers it on a project that already has code.
- `/vibe:challenge` attacks a decision already settled (one devil's-advocate pass, every objection reported with an opinion); `/vibe:consult [domain] "question"` asks one expert a precise question.
- `/vibe:debrief` asks one to three retrospective questions and stores the lessons as project memory; `/vibe:learn` turns an "always / never" correction into a global rule after confirmation.
- `/vibe:changelog` brings `[Unreleased]` up to date from git history. `/vibe:release` takes a version or `major`/`minor`/`patch`, or suggests the bump from the changelog when run without an argument.
- `/vibe:workspace-init`, run from the parent folder of several sibling repos, sets up or refreshes a hub repo tracking them. `/vibe:next-task` then picks the next eligible task across every active repo (or in the current repo alone), implements it, and pushes and releases. Alone it picks and confirms; `auto [N]` skips confirmation and suits `/loop`.
<!-- vibe:end:usage -->

## Skills (commands)

| Command | Purpose |
|---|---|
| `/vibe:init` | Initialize or regenerate the project's `CLAUDE.md` and `README.md` for vibe coding |
| `/vibe:backlog` | List, add, or remove feature backlog items (`.vibe/backlog/`) |
| `/vibe:audit` | Audit the existing codebase — classified findings, then backlog items for the ones you pick |
| `/vibe:challenge` | Devil's advocate on a settled structuring decision — one adversarial pass, every objection reported |
| `/vibe:consult` | Ask one of the plugin's experts a precise question (architecture by default) |
| `/vibe:feature` | Implement a new feature using TDD, then update the changelog |
| `/vibe:fix` | Fix a bug using TDD (reproduce first), then update the changelog |
| `/vibe:auto` | Work the backlog autonomously — no human gates, resumes after any interruption, `--push` publishes |
| `/vibe:debrief` | End-of-task retrospective turned into durable project memory |
| `/vibe:learn` | Turn a correction stated in general terms into a global rule in `~/.claude/rules/` |
| `/vibe:sync` | Generate/update `.vibe/` — the codebase context map |
| `/vibe:changelog` | Update `[Unreleased]` in `CHANGELOG.md` from git history |
| `/vibe:docs` | Generate/refresh README managed sections and developer docs in `docs/` (diagrams included) |
| `/vibe:release` | Bump version, finalize the changelog, commit and tag a release |
| `/vibe:workspace-init` | Bootstrap/refresh a multi-repo workspace's hub repo and local workspace-root `CLAUDE.md` |
| `/vibe:next-task` | Pick the next eligible task across a workspace (or the current repo), implement it, then push and release |

To help improve the plugin, share a usage report (the statistics file a run leaves under `.vibe/usage-reports/`) by adding it to `evals/inbox/` in this repository — a pull request is enough; nothing of your project is in that file.

Six internal skills are hidden from the `/` menu: `vibe:review` (the review agents on a change, run inside every feature and fix), `vibe:rewrite` (makes the final report readable, rule by rule, without losing a fact), `vibe:clarify` (the round-by-round interview, run by `backlog`, `init` and `workspace-init` on thin input, and twice by `feature`/`fix` — once to frame the need, once to frame the implementation, each looking in its own sources before asking you anything), `vibe:tasks` (task-list creation with a scratchpad fallback), `vibe:usage-report` (statistics of a run, written locally under `.vibe/usage-reports/`, never shared unless you choose to) and `vibe:publish` (push and release, used by `/vibe:auto --push` and `/vibe:next-task`).

## Review agents

Every feature and fix runs these specialized agents in parallel on its own changes, each owning one dimension, before it ships:

- `review-alternative-design` (opt-in), `review-antipatterns`, `review-architecture` (also ports & adapters, for projects that adopted them), `review-comments`, `review-coordination`, `review-correctness`, `review-ddd`, `review-dependencies`, `review-docs`, `review-hygiene`, `review-naming`, `review-overengineering`, `review-performance`, `review-robustness`, `review-security`, `review-signatures`, `review-simplicity`, `review-solid`, `review-tests`, `review-web-security` (with an opt-in dynamic verification mode against a locally-run instance)

Activation per project is recorded in the `CLAUDE.md` table written by `/vibe:init`.

One agent writes the code: `task-implementer` takes one sub-task at a time with the settled framing, writes the failing test, then the code, and reports every command it ran with its result; the workflow re-runs the tests before trusting it and asks you about any point the agent could not settle. Three control agents serve the build loop rather than a review dimension: `findings-classifier` (re-checks every finding against its source, drops false positives, merges duplicates, sets its level and whether it questions the need or the implementation), `requirements-reviewer` (the deliverable against the request: gaps, unrequested additions, breached constraints) and `claim-verifier` (every fact a report states, checked against its source — "tests pass" needs the command and its output).

## Expert agents

`/vibe:feature` and `/vibe:fix` consult up to 3 of these prescriptive experts while planning, based on what the task touches — each can also answer one precise question during implementation:

- `expert-architecture`, `expert-ui-ux`, `expert-frontend-design`, `expert-api-rest`, `expert-cli-dx`, `expert-data`, `expert-linux`, `expert-ops`, `expert-realtime-rendering`

`/vibe:consult` puts a precise question to any of them outside feature and fix work.

Experts prescribe requirements *before* the code exists; the review agents critique *after*. The two families cover disjoint domains, with two documented exceptions: `expert-realtime-rendering` is paired with `review-performance`, and `expert-architecture` with `review-architecture`, because rendering and design choices are hard to retrofit once the code is written.

## Subagent status line

The plugin ships a `subagentStatusLine` (`settings.json` + `scripts/subagent-statusline.sh`), applied automatically once the plugin is enabled. It replaces the default `name · description · token count` row in the agent panel with a compact, color-coded line — most visible during the internal review of every feature and fix, which runs up to 20 agents in parallel.

## Typical flow

1. `/vibe:init` once, to set up `CLAUDE.md` and `.vibe/`
2. `/vibe:backlog "some feature idea"` to queue work
3. `/vibe:feature 001` (or `/vibe:fix "bug description"`) to implement, TDD-first, with the matching experts weighing in on the plan; or `/vibe:auto` to work the whole backlog without supervision
4. `/vibe:release patch|minor|major` to ship a version

`/vibe:init` and `/vibe:sync` generate `CLAUDE.md` and the `.vibe/` context map inside *your* project — both are meant to be committed with it, so every session (and every teammate) starts from the same conventions and codebase map.

## Documentation

<!-- vibe:begin:docs-index -->
- [docs/architecture.md](docs/architecture.md) — the plugin's moving parts (skills, review agents, status line, manifests) and how they connect, with a component diagram
- [docs/development.md](docs/development.md) — how to work on the plugin itself: conventions, frontmatter shapes, the no-tests-by-design policy, and the release process
- [docs/website.md](docs/website.md) — how the demo website works: scripted terminal demos, deployment, and the pitfalls not to reintroduce
- [docs/workflows.md](docs/workflows.md) — the lifecycles behind the commands (feature/fix flow and its review loop, task tracking, usage report, backlog items, self-correction and escalation), with diagrams
<!-- vibe:end:docs-index -->

## License

[MIT](LICENSE)
