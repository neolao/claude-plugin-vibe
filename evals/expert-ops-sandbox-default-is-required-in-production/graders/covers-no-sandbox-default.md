---
type: llm
focus: last_message
criteria: |
  The brief wants `PAYMENT_API_URL` to default to the provider's sandbox
  so the worker starts on a laptop with nothing set, and expects the
  production deploy to set the live URL. A production pod started with the
  variable missing (a deploy that forgets it, a rollback to a manifest
  without it) would call the sandbox, mark real orders as refunded and
  email the customers, and nobody would know until finance reconciles a
  month later. The expert's own checklist says a default is one that is
  safe in production or there is none: a value whose convenient default
  would be wrong there is required.

  PASS if REQUIREMENTS says that the provider URL (and the key) must not
  default to the sandbox in a production process: the variable is required
  and the worker fails fast at startup naming it when it is missing, or a
  default is allowed only outside production (gated on the environment, a
  local-only config) and production refuses to start without an explicit
  value — with a stated behaviour or a test scenario for a production
  start with the variable unset.
  FAIL if the reply accepts the sandbox default as the brief proposes,
  never addresses a production process started without the variable, or
  raises it only as an `OPEN QUESTIONS:` entry asking the Product Owner
  whether the sandbox default is acceptable.
weight: 2
---

Requires the provider URL to have no sandbox default in production and
to fail fast when missing, as a requirement and not an open question.
