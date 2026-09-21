---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS or RISKS specifically calls out that loading the
  sparkle texture from disk synchronously at the moment of first selection
  is blocking I/O on (or triggered from) the render/update loop, and
  requires it to be deferred, pre-loaded, or done asynchronously off the
  hot path instead of loaded inline when selection happens. A generic
  "avoid slow operations" statement without tying it to the on-selection
  texture load described in the brief does not count.
  FAIL if the blocking-load-on-selection risk is absent or only stated
  generically.
weight: 2
---

Flags the on-selection synchronous texture load from disk as blocking work
that must be kept off the render/update loop.
