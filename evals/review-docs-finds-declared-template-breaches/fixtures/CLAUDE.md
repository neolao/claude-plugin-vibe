# CLAUDE.md — Ledger

Ledger imports bank statements, reconciles them against invoices and exports the result for the accountant. Python 3.12, no framework.

## Writing conventions

- Every page under `docs/` has exactly these sections, in this order: `## Purpose`, `## How to`, `## See also`. The last one links the pages a reader goes to next, and is never empty.
- A page under `docs/` stays under 300 words.
- A rule file under `.claude/rules/` carries a frontmatter with a `paths:` list of globs; the rule loads only for the files the globs match.
- `README.md` holds the index of `docs/` between the `<!-- vibe:begin:docs-index -->` and `<!-- vibe:end:docs-index -->` markers; `/vibe:docs` rewrites what sits between them.
