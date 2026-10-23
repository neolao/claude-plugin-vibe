---
type: llm
focus: { source: file, path: docs/architecture.md }
criteria: |
  Ignore the first line of the file (the generated-file banner) and any
  code identifier, path or Mermaid block.

  PASS only if the explanatory prose of docs/architecture.md is written
  in French.

  FAIL if the prose is in English or another language, or if the file
  is missing or empty.
weight: 2
---

The developer docs follow the project language too, not only the README.
