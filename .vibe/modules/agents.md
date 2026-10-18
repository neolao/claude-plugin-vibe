# Module: agents

**Role:** Four families of sub-agents, one file per agent. `task-implementer` is the only one that writes code: the workflow hands it one sub-task at a time and re-runs the tests itself on its report. Control agents (`review-classifier`, `requirements-reviewer`, `claim-verifier`) are read-only bricks of the build loop: they judge findings, conformity to the request and the truth of claims, each with its own output contract (`## CLASSIFIED findings` / `## DISCARDED` / `## DOUBTS`; `## REQUIREMENTS findings`; `## CLAIMS findings`), and never give a severity themselves except the classifier. `review-*` agents each audit one quality dimension after the fact, in parallel under `/vibe:review`, which injects the shared finding contract (format, `high`/`medium`/`low` scale, read-only rule) into each prompt — an agent file holds only its scope, checklist, and categories. `expert-*` agents prescribe requirements before or during implementation for `/vibe:feature`/`/vibe:fix`, which pass the consultation format (`REQUIREMENTS`/`RISKS`/`TEST SCENARIOS`, or one question) in the prompt. Experts cover domains without a `review-*` counterpart (ADR [`001`](../decisions/001-expert-personas-scope.md)), except `expert-realtime-rendering`, paired with `review-performance` (ADR [`003`](../decisions/003-realtime-rendering-expert-exception.md)), and `expert-architecture`, paired with `review-architecture` (ADR [`005`](../decisions/005-architecture-expert-exception.md)). Every agent pins a full model id and an `effort:` level.
**Files:** `agents/*.md`
**Exports (implementer):**
- `task-implementer` (`tools: Read, Write, Edit, Grep, Glob, Bash`) — writes one sub-task of the approved plan out of the workflow's context, test first; receives the sub-task, the settled framing, the files, the quoted rule blocks and, on a correction round, the findings with their level; returns `## IMPLEMENTATION report` (files changed, commands run with exact results — the red run before the green one — findings handled, doubts); never commits, never runs the app, settles nothing the framing left open

**Exports (control agents, read-only):**
- `review-classifier` — re-checks each raw finding against its source and drops false positives, merges duplicates, gives a level (`high`/`medium`/`low`, by the consequence for the user of the deliverable) and a space (`need` / `implementation`, which decides where the build loop goes back); returns doubts with a recommended option instead of guessing; judges only the findings it is given
- `requirements-reviewer` — the deliverable against the request: `(gap)`, `(addition)`, `(constraint)`, `(ambiguity)`; a guard, a helper or a test that serves a requirement is never an addition; derived from the former `verify` scope grid
- `claim-verifier` (+ `Bash`, to re-run a cheap side-effect-free command) — each factual claim of an AI-written text against its source: `(unproven)`, `(contradicted)`, `(conclusion)`; "tests pass" without the command and its output is unproven

**Exports (`review-*`, frontmatter `tools: Read, Grep, Glob` unless noted):**
- `review-alternative-design` — opt-in: a named alternative pattern scored against the code as written on a 7-criteria grid, reported only on a `BETTER` verdict with migration cost and counter-argument; never high
- `review-antipatterns` — named anti-patterns: god objects, primitive obsession, stringly-typed code, mutable global state, temporal coupling, wheel reinvention
- `review-architecture` — drift against `.vibe/`: module scope, cycles, layer direction (sole owner), responsibility spread, violated ADRs, orphans; ports & adapters when the project explicitly adopted hexagonal architecture
- `review-comments` (+ `Bash`, only to print a file with a comment's lines removed) — redundant, partially redundant, verbose or misleading comments, judged by the "without the comment" test
- `review-coordination` — the same knowledge (rule, case list, constant, table, format) written twice with no guard (shared definition, exhaustive type, test, runtime check, generator)
- `review-correctness` — real bugs: wrong logic, bounds, null, broken callers, races, fix at the wrong altitude; every finding carries a `SCENARIO:` line; failure handling stays with `review-robustness`
- `review-ddd` — ubiquitous language, domain isolation, aggregates, entities (identity), value objects, anemic model, domain services, repositories (opt-in)
- `review-docs` — Markdown docs against each other and the file system: contradictions, diverged copies, index drift, dangling references, format against declared templates only, vocabulary against the glossary; never docs against code (active when docs beyond the README exist)
- `review-dependencies` (+ `Bash`) — runs the stack's audit tool; abandoned packages, version hygiene, unused or misplaced dependencies
- `review-hygiene` — dead code, leftovers, stale markers, duplication
- `review-naming` — misleading or intent-hiding names, with `CURRENT:` and a proposed name
- `review-overengineering` — speculative abstractions, patterns without need, unused configurability, premature optimization, disproportionate structure
- `review-performance` — N+1, complexity on real data, blocking hot paths, unbounded growth, real-time loop defects; every finding carries a `SCALE:` line
- `review-robustness` — swallowed errors, async, timeouts and limits, resources, lost error context
- `review-security` — secrets, injection, dangerous primitives, access control, crypto, trust boundaries (any project type)
- `review-signatures` — shape of data passed around: branch-only arguments, arguments travelling together or taken at different instants, replayed decisions, three-state returns, field groups added to shared types, inconsistent filtering, copy cost
- `review-simplicity` — redundant logic, indirection, non-idiomatic detours, unused generality, complexity hotspots (cyclomatic, length, nesting)
- `review-solid` — S/O/L/I/D at class and module level; layer direction left to `review-architecture`
- `review-tests` (+ `Bash`) — runs the real suite and isolated e2e/integration; tautological tests (never rated low), coupling, coverage, quality, pyramid
- `review-web-security` (+ `Bash`) — HTTP attack surface statically, plus an opt-in dynamic verification mode against a locally-run instance (`TARGET:`/`PROOF:` findings, authorized local scope only)

**Exports (`expert-*`):**
- `expert-architecture` — module boundaries, coupling, dependency direction, pattern choice; a named baseline plus up to two named alternatives scored on an explicit grid, and the question the choice depends on (ADR [`005`](../decisions/005-architecture-expert-exception.md))
- `expert-ui-ux` — priority, flows, states, feedback, forms, accessibility, consistency
- `expert-frontend-design` — design tokens reuse, hierarchy, semantic colors, responsive, interactive states
- `expert-api-rest` — resources, HTTP semantics, status codes, pagination, compatibility
- `expert-cli-dx` — flags, stdout/stderr, exit codes, actionable errors, destructive-operation guards
- `expert-data` — column types, database-enforced invariants, migrations, indexes, transactions
- `expert-linux` — safe Bash, temp files and atomic writes, privileges, signals, services, GNU/BSD differences
- `expert-ops` — configuration, observability, rolling deploys, pipeline and images, timeouts and retries
- `expert-realtime-rendering` — frame budget, per-frame allocation, draw-call batching, non-blocking loop, simulation vs render rate

**Depends on:** [`modules/skills.md`](skills.md) (`review-*` invoked by the `vibe:review` brick inside `feature`/`fix`, activation recorded per project in that project's `CLAUDE.md`; `expert-*` selected per task by `/vibe:feature`/`/vibe:fix` from their descriptions — 3 max, none without a clear match — or asked one question by `/vibe:consult`)
