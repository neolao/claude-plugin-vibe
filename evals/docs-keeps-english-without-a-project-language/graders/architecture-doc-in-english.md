---
type: llm
focus: { source: file, path: docs/architecture.md }
criteria: |
  Ignore the first line of the file (the generated-file banner) and any
  code identifier, path or Mermaid block.

  PASS only if the explanatory prose of docs/architecture.md is written
  in English.

  FAIL if the prose is in French or another language, or if the file is
  missing or empty.
weight: 2
---

The developer docs follow the same fallback as the README sections.
