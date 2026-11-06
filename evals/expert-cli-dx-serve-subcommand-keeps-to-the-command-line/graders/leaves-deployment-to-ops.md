---
type: llm
focus: last_message
criteria: |
  The brief says the `/healthz` endpoint, the Dockerfile and the restart
  policy are written alongside the command. The expert's scope sentence
  keeps the command-line interface and routes how a server is configured,
  deployed, observed and kept running to `expert-ops`.

  PASS if no REQUIREMENTS entry prescribes the health endpoint's behaviour,
  the Dockerfile's content (base image, user, layers) or the restart
  policy. Mentioning them in passing as another expert's domain, naming
  `expert-ops`, or requiring that what the command prints while running
  goes to stdout/stderr unbuffered so the orchestrator collects it, all
  pass: the stream discipline is the command's.
  FAIL if REQUIREMENTS prescribes what `/healthz` returns or checks, how the
  Dockerfile is built, or which restart policy the deployment uses, as if
  the expert owned the deployment.
weight: 1
---

Keeps the health endpoint, the image and the restart policy out of its
REQUIREMENTS: the subcommand is its domain, the deployment is `expert-ops`'s.
