# Module: agents

**Role:** Specialized review sub-agents, each auditing one quality dimension; orchestrated in parallel by `/vibe:review`. All are read-only with respect to source (no edits) except `review-tests`, which executes the project's real test suite (including isolated e2e/integration runs) to ground findings in pass/fail evidence, and `review-pentest`, which launches a local instance of the app and probes it dynamically to prove exploitability (authorized local scope only).
**Files:** `agents/*.md`
**Exports:**
- `review-antipatterns` — named anti-patterns: god objects, primitive obsession, stringly-typed code, temporal coupling, wheel reinvention
- `review-architecture` — architectural drift, module boundaries, layering, violations of ADRs in `.vibe/decisions/` (legacy `.vibe/decisions.md` as fallback)
- `review-complexity` — cyclomatic complexity, function length, nesting
- `review-ddd` — Domain-Driven Design alignment (domain-heavy projects only)
- `review-dependencies` — dependency health, vulnerabilities, abandoned packages
- `review-hygiene` — dead code, unused exports, stale TODOs, duplication
- `review-naming` — naming quality across the codebase
- `review-overengineering` — design-level YAGNI: speculative abstractions, unused configurability, premature optimization
- `review-pentest` — dynamic penetration test: proves auth bypass, IDOR, injection, business-logic abuse against a locally-run instance (runnable networked apps only)
- `review-performance` — N+1 queries, quadratic patterns, blocking I/O (API/server projects only)
- `review-robustness` — swallowed errors, unawaited promises, missing timeouts
- `review-security` — secrets, injections, dangerous primitives, crypto misuse
- `review-simplicity` — expression-level convolution: redundant conditions, pointless indirection, reducible logic
- `review-solid` — SOLID principles in OO/modular code
- `review-tests` — test coverage, relevance, and quality; executes the real test suite
- `review-web-security` — web attack surface: path traversal, XSS, SSRF, security headers, cookies, application-level DoS (HTTP-exposing projects only)

**Depends on:** [`modules/skills.md`](skills.md) (invoked by `/vibe:review`; activation rules recorded per-project in that project's own `CLAUDE.md`)
