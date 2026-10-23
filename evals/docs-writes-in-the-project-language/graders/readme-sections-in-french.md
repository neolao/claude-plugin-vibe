---
type: llm
focus: { source: file, path: README.md }
criteria: |
  Look only at the content between the `<!-- vibe:begin:features -->`
  and `<!-- vibe:end:features -->` markers and between the
  `<!-- vibe:begin:install -->` and `<!-- vibe:end:install -->` markers
  in README.md.

  PASS only if the prose of both sections is written in French and
  neither still holds its "À COMPLÉTER" placeholder. Command names,
  flags, package names and environment variables (`widgetcli`, `--json`,
  `npm`, `WIDGETCLI_HOME`) are expected to stay as they are and do not
  count as English.

  FAIL if the prose of either section is in English or another
  language, or if a placeholder survives.
weight: 3
---

`CLAUDE.md` names French under `## Project language`: the managed
sections are written in that language, not in the changelog's.
