# Module: agents

**Role:** Two families of sub-agents, one file per agent. `review-*` agents each audit one quality dimension after the fact, in parallel under `/vibe:review`, which injects the shared finding contract (format, `high`/`medium`/`low` scale, read-only rule) into each prompt — an agent file holds only its scope, checklist, and categories. `expert-*` agents prescribe requirements before or during implementation for `/vibe:feature`/`/vibe:fix`, which pass the consultation format (`REQUIREMENTS`/`RISKS`/`TEST SCENARIOS`, or one question) in the prompt. Experts cover domains without a `review-*` counterpart (ADR [`001`](../decisions/001-expert-personas-scope.md)), except `expert-realtime-rendering`, paired with `review-performance` (ADR [`003`](../decisions/003-realtime-rendering-expert-exception.md)).
**Files:** `agents/*.md`
**Exports (`review-*`, frontmatter `tools: Read, Grep, Glob` unless noted):**
- `review-antipatterns` — named anti-patterns: god objects, primitive obsession, stringly-typed code, mutable global state, temporal coupling, wheel reinvention
- `review-architecture` — drift against `.vibe/`: module scope, cycles, layer direction (sole owner), responsibility spread, violated ADRs, orphans; ports & adapters when the project explicitly adopted hexagonal architecture
- `review-ddd` — ubiquitous language, domain isolation, aggregates, value objects, repositories (opt-in)
- `review-dependencies` (+ `Bash`) — runs the stack's audit tool; abandoned packages, version hygiene, unused or misplaced dependencies
- `review-hygiene` — dead code, leftovers, stale markers, duplication
- `review-naming` — misleading or intent-hiding names, with `CURRENT:` and a proposed name
- `review-overengineering` — speculative abstractions, patterns without need, unused configurability, premature optimization, disproportionate structure
- `review-performance` — N+1, complexity on real data, blocking hot paths, unbounded growth, real-time loop defects; every finding carries a `SCALE:` line
- `review-robustness` — swallowed errors, async, timeouts and limits, resources, lost error context
- `review-security` — secrets, injection, dangerous primitives, access control, crypto, trust boundaries (any project type)
- `review-simplicity` — redundant logic, indirection, non-idiomatic detours, unused generality, complexity hotspots (cyclomatic, length, nesting)
- `review-solid` — S/O/L/I/D at class and module level; layer direction left to `review-architecture`
- `review-tests` (+ `Bash`) — runs the real suite and isolated e2e/integration; tautological tests (never rated low), coupling, coverage, quality, pyramid
- `review-web-security` (+ `Bash`) — HTTP attack surface statically, plus an opt-in dynamic verification mode against a locally-run instance (`TARGET:`/`PROOF:` findings, authorized local scope only)

**Exports (`expert-*`):**
- `expert-ui-ux` — priority, flows, states, feedback, forms, accessibility, consistency
- `expert-frontend-design` — design tokens reuse, hierarchy, semantic colors, responsive, interactive states
- `expert-api-rest` — resources, HTTP semantics, status codes, pagination, compatibility
- `expert-cli-dx` — flags, stdout/stderr, exit codes, actionable errors, destructive-operation guards
- `expert-data` — column types, database-enforced invariants, migrations, indexes, transactions
- `expert-linux` — safe Bash, temp files and atomic writes, privileges, signals, services, GNU/BSD differences
- `expert-ops` — configuration, observability, rolling deploys, pipeline and images, timeouts and retries
- `expert-realtime-rendering` — frame budget, per-frame allocation, draw-call batching, non-blocking loop, simulation vs render rate

**Depends on:** [`modules/skills.md`](skills.md) (`review-*` invoked by `/vibe:review`, activation recorded per project in that project's `CLAUDE.md`; `expert-*` selected per task by `/vibe:feature`/`/vibe:fix` from their descriptions — 3 max, none without a clear match)
