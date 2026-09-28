---
type: llm
focus: { source: file, path: README.md }
criteria: |
  Look only at the content between `<!-- vibe:begin:features -->` and
  `<!-- vibe:end:features -->` in README.md.

  PASS if no line of that section presents caching, an in-memory cache, or
  faster repeated listings as a feature of the project.

  FAIL if any line of that section still presents caching or faster
  repeated listings as a feature.
weight: 1
---

CHANGELOG 1.2.0 added an in-memory cache; CHANGELOG [Unreleased] > Removed
takes it out. Features are derived from the whole CHANGELOG, so a capability
removed later is no longer a feature.
