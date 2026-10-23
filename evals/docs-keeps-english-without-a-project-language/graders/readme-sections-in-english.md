---
type: llm
focus: { source: file, path: README.md }
criteria: |
  Look only at the content between the `<!-- vibe:begin:features -->`
  and `<!-- vibe:end:features -->` markers and between the
  `<!-- vibe:begin:install -->` and `<!-- vibe:end:install -->` markers
  in README.md.

  PASS only if the prose of both sections is written in English and
  neither still holds its "TODO" placeholder.

  FAIL if the prose of either section is in French or another language,
  or if a placeholder survives.
weight: 3
---

No `## Project language` section: the sections follow the language the
README already uses, English — a French-speaking team named in the
overview is not a language setting.
