# Ubiquitous Language

## Vibe coding
The development methodology this plugin implements: the human acts as Product Owner only (describes requirements, evaluates outcomes) and never writes or manually tests code; all quality assurance (TDD, lint, multi-agent review) is automated and enforced via the target project's own generated `CLAUDE.md`.
**Do not confuse with:** generic "AI pair programming" — vibe coding here specifically excludes manual testing by the human
_Sources: `skills/feature/SKILL.md`, `skills/fix/SKILL.md`, `skills/init/SKILL.md`_

## Managed section
A region of `README.md` delimited by `<!-- vibe:begin:X -->` / `<!-- vibe:end:X -->` markers that `/vibe:docs` is allowed to rewrite; everything outside these markers is hand-written and never touched.
**Do not confuse with:** the fully-generated files under `docs/` (no partial markers — the whole file is regenerated)
_Sources: `skills/docs/SKILL.md`, `README.md`_

## ADR (decision record)
An append-only record of an architectural decision made during a feature/fix, stored under `.vibe/decisions/`; written by `/vibe:feature`, never regenerated or deleted by sync.
**Do not confuse with:** `.vibe/modules/*.md` or `.vibe/models.md`, which are regenerable and not decisions
_Sources: `skills/feature/SKILL.md`, `skills/sync/SKILL.md`_

## Tautological test
A test that cannot fail for a wrong implementation, so it gives false confidence while masking real bugs behind a green suite. Four recognized patterns: self-referential assertion, trivially true assertion, mock over-configuration, no-op coverage. Self-check: could a plausible-but-wrong implementation still pass this test?
**Do not confuse with:** a low-coverage test (asserts too little but *can* fail) or a flaky test (fails/passes inconsistently for unrelated reasons)
_Sources: `skills/feature/SKILL.md`, `skills/fix/SKILL.md`, `agents/review-tests.md`_
