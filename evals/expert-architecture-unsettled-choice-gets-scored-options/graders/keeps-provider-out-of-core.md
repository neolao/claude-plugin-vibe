---
type: llm
focus: last_message
criteria: |
  The fixture's `.vibe/decisions/001-ports-and-adapters.md` decides that
  provider SDKs live under `adapters/` behind the `Notifier` port of
  `core/ports.py`, and the module map gives `core` no dependency. That
  decision is a constraint every option must hold, whatever the expert
  recommends about how the channel is chosen.

  PASS if no option — baseline, alternatives or recommendation — imports
  the Twilio SDK or writes the HTTP call to Twilio inside `core/`, and the
  SMS sending code lands under `adapters/notify/` (as a `Notifier`
  implementation or an equivalent adapter).
  FAIL if any option, or the recommendation, places the Twilio client or
  the SMS request inside `core/`, or drops the port so that core calls the
  adapter class directly.
weight: 1
---

Holds the recorded layering decision as a constraint on every option:
provider code stays behind the port, under `adapters/`.
