---
type: llm
focus: last_message
criteria: |
  The asset service that serves the PNGs and glTF meshes belongs to the REST
  API expert; this expert's domain stops at what the running renderer does
  with what it receives.

  PASS if no REQUIREMENTS, RISKS, or TEST SCENARIOS entry designs the asset
  service's HTTP contract: no endpoint shapes or URL schemes, no status
  codes, no response schemas, no pagination, no cache headers, CDN or
  compression settings on the service side. Entries about what the renderer
  asks for and when — requesting a texture ahead of range, cancelling or
  dropping a fetch for an object that moved out of range, bounding how many
  fetches are in flight, needing a lower-resolution variant to exist — are
  renderer-side and pass.
  FAIL if the reply prescribes how the service answers: endpoint or URL
  design, status codes, response bodies, pagination, cache headers or CDN
  configuration.
weight: 2
---

Prescribes nothing about the asset service's HTTP contract while covering
the renderer's side of streaming.
