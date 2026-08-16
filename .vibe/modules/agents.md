# Module: agents

**Role:** Two families of specialized sub-agents, one file per agent. `review-*` agents each audit one quality dimension *after the fact*, orchestrated in parallel by `/vibe:review`; `expert-*` agents are prescriptive consultants invoked *before or during* implementation by `/vibe:feature`/`/vibe:fix` (plan consultation with a fixed REQUIREMENTS/RISKS/TEST SCENARIOS output, or single-question implementation consultation). Review agents are read-only with respect to source (no edits) except `review-tests`, which executes the project's real test suite (including isolated e2e/integration runs) to ground findings in pass/fail evidence, and `review-pentest`, which launches a local instance of the app and probes it dynamically to prove exploitability (authorized local scope only). Expert agents never write code and never review diffs; their roster is deliberately limited to domains without a `review-*` counterpart (ADR [`001`](../decisions/001-expert-personas-scope.md)) — `expert-realtime-rendering` is a documented, narrow exception paired with `review-performance` (ADR [`003`](../decisions/003-realtime-rendering-expert-exception.md)).
**Files:** `agents/*.md`
**Exports (`review-*`):**
- `review-antipatterns` — named anti-patterns: god objects, primitive obsession, stringly-typed code, temporal coupling, wheel reinvention
- `review-architecture` — architectural drift, module boundaries, layering, violations of ADRs in `.vibe/decisions/` (legacy `.vibe/decisions.md` as fallback)
- `review-complexity` — cyclomatic complexity, function length, nesting
- `review-ddd` — Domain-Driven Design alignment (domain-heavy projects only)
- `review-dependencies` — dependency health, vulnerabilities, abandoned packages
- `review-hexagonal` — hexagonal architecture (ports & adapters) compliance: port ownership, leaky port contracts, adapter purity, wiring (hexagonal projects only)
- `review-hygiene` — dead code, unused exports, stale TODOs, duplication
- `review-naming` — naming quality across the codebase
- `review-overengineering` — design-level YAGNI: speculative abstractions, unused configurability, premature optimization
- `review-pentest` — dynamic penetration test: proves auth bypass, IDOR, injection, business-logic abuse against a locally-run instance (runnable networked apps only)
- `review-performance` — N+1 queries, quadratic patterns, blocking I/O, and (real-time projects) frame-budget overruns, per-frame allocation churn, unbatched draw calls
- `review-robustness` — swallowed errors, unawaited promises, missing timeouts
- `review-security` — secrets, injections, dangerous primitives, crypto misuse
- `review-simplicity` — expression-level convolution: redundant conditions, pointless indirection, reducible logic
- `review-solid` — SOLID principles in OO/modular code
- `review-tests` — test coverage, relevance, and quality; executes the real test suite
- `review-web-security` — web attack surface: path traversal, XSS, SSRF, security headers, cookies, application-level DoS (HTTP-exposing projects only)

**Exports (`expert-*`):**
- `expert-ui-ux` — user flows, interface states (empty/loading/error), feedback, accessibility
- `expert-frontend-design` — typography, spacing, color, responsive layout, visual consistency
- `expert-api-rest` — resource modeling, HTTP semantics, status codes, pagination, error format, compatibility
- `expert-cli-dx` — flag conventions, help output, exit codes, stdout/stderr discipline, machine-readable output
- `expert-data` — schema design, migrations, integrity constraints, indexing, transactions
- `expert-linux` — shell scripting, POSIX portability, permissions, signals, filesystem conventions, services
- `expert-ops` — configuration, observability, deployment compatibility, CI/CD, containers, resilience
- `expert-realtime-rendering` — frame budget, per-frame allocation discipline, draw-call batching, render/update loop structure

**Depends on:** [`modules/skills.md`](skills.md) (`review-*` invoked by `/vibe:review`, activation rules recorded per-project in that project's own `CLAUDE.md`; `expert-*` invoked by `/vibe:feature`/`/vibe:fix`, selected per-task by matching the brief against agent descriptions — 3 max per run, none if no clear match)
