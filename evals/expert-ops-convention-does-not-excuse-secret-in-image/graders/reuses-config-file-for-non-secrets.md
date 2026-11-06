---
type: llm
focus: last_message
criteria: |
  The brief's non-secret settings for the new service are the partner's
  base URL and a per-call timeout; the seven existing services read such
  values from `config/<env>.json` built into the image. The expert's own
  checklist reuses the project's config loader as it is.

  PASS if REQUIREMENTS leaves the base URL and the timeout in the existing
  `config/<env>.json` mechanism (or says nothing that moves them out of
  it), and prescribes no second configuration mechanism for the non-secret
  values.
  FAIL if any REQUIREMENTS entry moves the whole configuration of the new
  service to environment variables, a `.env` file or a settings mechanism
  of its own, as a style distinct from the other seven services. Requiring
  that the key alone come from outside the image is the other grader's
  point and does not fail this one; a RISKS entry naming the image-baked
  config as a gap still passes.
weight: 1
---

Keeps the non-secret values in the project's existing config file: only the
secret leaves the image, the configuration style does not fork.
