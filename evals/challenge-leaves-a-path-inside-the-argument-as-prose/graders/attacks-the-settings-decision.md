---
type: llm
focus: last_message
criteria: |
  The argument is prose: the decision is to keep the runtime settings in
  `config/app.toml` rather than in environment variables or in a settings
  table of the SQLite store. The path inside it names the settings file,
  not a decision file to read in place of the prose; the repository's
  `.vibe/decisions/002-sqlite-local-store.md` records a different
  decision (where projects are stored) and is not the one under attack.

  PASS if the decision reported as challenged is the settings-file one
  and the objections bear on it (the TOML file, hand edits, environment
  variables, a settings table), and the message asks the user no question
  about which decision to challenge.
  FAIL if the decision reported as challenged is the SQLite project store
  of the ADR, if the objections attack where projects are stored instead
  of where settings live, if the skill says the argument names no usable
  decision, or if it asks which decision to challenge. Mentioning the ADR
  as context, or an objection that relates the settings to the SQLite
  store, passes.
weight: 2
---

Prose is the decision; a path inside it is a file the decision speaks
of, not the decision file, and the repository's ADR on another subject
does not replace it.
