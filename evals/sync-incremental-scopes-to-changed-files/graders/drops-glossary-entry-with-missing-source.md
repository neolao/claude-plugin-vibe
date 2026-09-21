---
type: regex
pattern: 'Dunning Run'
target: { source: file, path: ".vibe/glossary.md" }
match: not_contains
weight: 2
---

The `Dunning Run` entry cites `src/billing/dunning.js`, which does not exist
in the repo. Step 4 of the skill checks every `Sources:` line for existence in
incremental mode too, and removes entries whose sources are gone with no new
usage found — so the entry must be dropped.
