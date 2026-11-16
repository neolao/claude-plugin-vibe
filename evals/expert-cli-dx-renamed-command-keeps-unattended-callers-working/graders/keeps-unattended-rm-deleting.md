---
type: llm
focus: last_message
criteria: |
  The pipelines run `vault rm <name>` with no terminal attached, and today
  that deletes the secret and exits 0. The new confirmation prompt cannot be
  answered there. The expert's checklist says an existing script's
  unchanged invocation keeps getting what it got, and that a prompt never
  hangs an unattended run.

  PASS if REQUIREMENTS or TEST SCENARIOS makes the pipelines' unchanged
  `vault rm <name>`, run with no terminal, still delete the secret without
  hanging and without failing in this change. Any concrete means passes: the
  old `rm` keeps its current no-prompt behaviour during the transition (a
  deprecation warning on stderr is fine), or the prompt only applies to an
  interactive terminal, or requiring the skip flag on `rm` is deferred to a
  later version after a named deprecation period.
  FAIL if, as a requirement of this change, the unchanged non-terminal
  `vault rm <name>` would wait on the prompt, or would fail until the teams
  add a flag, or if the reply never says what that invocation does after
  the change.
weight: 2
---

Keeps the nightly cleanup jobs deleting: the new guard must not turn their
unchanged call into a hang or a failure overnight.
