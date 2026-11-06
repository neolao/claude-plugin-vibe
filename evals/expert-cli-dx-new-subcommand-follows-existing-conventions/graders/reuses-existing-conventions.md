---
type: llm
focus: last_message
criteria: |
  The brief describes a CLI whose nine subcommands share one style for four
  years: single-dash long flags (`-region eu`, `-dry-run`), `-o table|json`
  on every command, `error: <message>` on stderr. The expert's own checklist
  says the CLI's existing conventions beat its defaults, even where it would
  pick otherwise.

  PASS if REQUIREMENTS requires `fleet drain` to reuse the existing
  conventions — at least the single-dash flag style and the existing
  `-o json` switch for machine-readable output — and prescribes no
  different style for it.
  FAIL if any REQUIREMENTS entry prescribes, for `fleet drain`, a style that
  differs from the existing one: GNU `--double-dash` long flags
  (`--dry-run`, `--timeout`), a new `--json` flag in place of `-o json`, or a
  different error line format. A different style suggested only in RISKS as
  a gap or a later migration still passes.
weight: 2
---

Requires the new subcommand to reuse the CLI's single-dash flags and
`-o json` switch, instead of prescribing the checklist's own GNU defaults
as a second style.
