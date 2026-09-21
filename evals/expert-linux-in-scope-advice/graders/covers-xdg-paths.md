---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  specific brief, that the cache file must not use a hardcoded home-directory
  path and should follow XDG base-directory conventions (or an equivalent
  configurable/portable cache location), so the daemon behaves correctly
  across different users and machines.
  FAIL if the reply never raises the hardcoded-home-path / XDG cache-location
  concern for this daemon's cache file.
weight: 2
---

Names the XDG-directory / no-hardcoded-home-path concern for the daemon's
cache file.
