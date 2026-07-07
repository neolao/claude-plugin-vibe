# Ubiquitous Language

## Vibe coding
**Definition:** [fill in — refine] The development methodology this plugin implements: the human acts as Product Owner only (describes requirements, evaluates outcomes) and never writes or manually tests code; all quality assurance (TDD, lint, multi-agent review) is automated.
**Code:** described in every skill's workflow (`skills/feature/SKILL.md`, `skills/fix/SKILL.md`, `skills/init/SKILL.md`), enforced via the target project's own generated `CLAUDE.md`
**Do not confuse with:** generic "AI pair programming" — vibe coding here specifically excludes manual testing by the human

## Managed section
**Definition:** [fill in — refine] A region of `README.md` delimited by `<!-- vibe:begin:X -->` / `<!-- vibe:end:X -->` markers that `/vibe:docs` is allowed to rewrite; everything outside these markers is hand-written and never touched.
**Code:** `skills/docs/SKILL.md`
**Do not confuse with:** the fully-generated files under `docs/` (no partial markers — the whole file is regenerated)

## ADR (decision record)
**Definition:** [fill in — refine] An append-only record of an architectural decision made during a feature/fix, stored under `.vibe/decisions/`.
**Code:** referenced in `skills/sync/SKILL.md` (Step 8, Step 8b); written by `/vibe:feature`
**Do not confuse with:** `.vibe/modules/*.md` or `.vibe/models.md`, which are regenerable and not decisions
