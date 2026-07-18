# Module: agents

**Role:** Specialized review sub-agents, each auditing one quality dimension; orchestrated in parallel by `/vibe:review`. All are read-only (no source edits) except `review-tests`, which also executes the project's real test suite (including isolated e2e/integration runs) to ground its findings in actual pass/fail evidence.
**Files:** `agents/*.md`
**Exports:**
- `review-architecture` — architectural drift, module boundaries, layering, violations of ADRs in `.vibe/decisions/` (legacy `.vibe/decisions.md` as fallback)
- `review-complexity` — cyclomatic complexity, function length, nesting
- `review-ddd` — Domain-Driven Design alignment (domain-heavy projects only)
- `review-dependencies` — dependency health, vulnerabilities, abandoned packages
- `review-hygiene` — dead code, unused exports, stale TODOs, duplication
- `review-naming` — naming quality across the codebase
- `review-performance` — N+1 queries, quadratic patterns, blocking I/O (API/server projects only)
- `review-robustness` — swallowed errors, unawaited promises, missing timeouts
- `review-security` — secrets, injections, dangerous primitives, crypto misuse
- `review-solid` — SOLID principles in OO/modular code
- `review-tests` — test coverage, relevance, and quality; executes the real test suite
- `review-web-security` — web attack surface: path traversal, XSS, SSRF, security headers, cookies, application-level DoS (HTTP-exposing projects only)

**Depends on:** [`modules/skills.md`](skills.md) (invoked by `/vibe:review`; activation rules recorded per-project in that project's own `CLAUDE.md`)
