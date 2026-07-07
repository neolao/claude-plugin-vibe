# Module: agents

**Role:** Specialized read-only review sub-agents, each auditing one quality dimension; orchestrated in parallel by `/vibe:review`.
**Files:** `agents/*.md`
**Exports:**
- `review-architecture` — architectural drift, module boundaries, layering
- `review-complexity` — cyclomatic complexity, function length, nesting
- `review-ddd` — Domain-Driven Design alignment (domain-heavy projects only)
- `review-dependencies` — dependency health, vulnerabilities, abandoned packages
- `review-hygiene` — dead code, unused exports, stale TODOs, duplication
- `review-naming` — naming quality across the codebase
- `review-performance` — N+1 queries, quadratic patterns, blocking I/O (API/server projects only)
- `review-robustness` — swallowed errors, unawaited promises, missing timeouts
- `review-security` — secrets, injections, dangerous primitives, crypto misuse
- `review-solid` — SOLID principles in OO/modular code

**Depends on:** [`modules/skills.md`](skills.md) (invoked by `/vibe:review`; activation rules recorded per-project in that project's own `CLAUDE.md`)
