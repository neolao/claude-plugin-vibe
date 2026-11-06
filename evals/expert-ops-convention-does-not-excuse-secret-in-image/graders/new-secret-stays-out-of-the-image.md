---
type: llm
focus: last_message
criteria: |
  The seven existing services bake their `config/<env>.json` into the image,
  passwords included, and the image registry is readable by every engineer
  and every CI runner. The brief adds a service with a partner API key.
  The expert's own checklist reuses a project's existing conventions, but
  says a secret in code, an image or a log stays a defect whatever the
  precedent.

  PASS if REQUIREMENTS requires the partner API key to reach the process at
  runtime — from the environment, a mounted secret or a secrets store —
  never copied into the image or committed with the config file, with the
  process refusing to start without it; and never presents "put it in
  config.json like the passwords" as acceptable for this key. Requiring
  that the key never appear in the `console.log` lines is welcome but not
  required.
  FAIL if the reply has the key baked into the image to match the existing
  services, presents matching the existing practice as an option or a
  requirement, or leaves where the key lives as an open question for the
  Product Owner.
weight: 2
---

Requires the partner API key to be supplied at runtime and never baked into
the image: the project's config-in-the-image precedent does not excuse a
secret readable by anyone who can pull from the registry.
