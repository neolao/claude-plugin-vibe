---
type: llm
focus: last_message
criteria: |
  BC7, ASTC and mip levels are rendering words, but the brief changes an
  HTTP service only: no render loop, no per-frame work, no draw submission,
  and the editor's adoption of the variants is explicitly a later change.
  The expert's own scope sentence gives such a brief a one-line reply naming
  the expert it belongs to, whatever format the request asks for.

  PASS if the sub-agent's reply is a short statement (roughly one line, or a
  short reply that explicitly says the brief is the service's HTTP API and
  not a render loop and hands it to another expert) and it does NOT produce
  REQUIREMENTS/RISKS/TEST SCENARIOS about the API (how variants are listed,
  which variant is returned, what is answered when one is missing) nor
  rendering requirements for the editor's future use of the compressed
  textures (upload cost, format selection per GPU, mip streaming).
  FAIL if the reply fills the three lists, or asserts confident detailed
  advice about the variant endpoints, their responses, or how the editor
  should consume the variants, as if the brief were in scope.
weight: 2
---

Declines the service-only brief in one line instead of designing the API or
the editor's future texture pipeline.
