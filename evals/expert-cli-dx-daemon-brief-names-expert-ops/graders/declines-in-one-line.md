---
type: llm
focus: last_message
criteria: |
  SIGTERM, a startup check and a missing-variable message sound like a
  command's behaviour, but the brief says the `agentd run` command, its
  flags, its help and its output do not change: the work is the daemon's
  configuration, health endpoint, shutdown, image and restart policy. The
  expert's own scope sentence gives such a brief a one-line reply naming
  the expert it belongs to, whatever format the request asks for.

  PASS if the sub-agent's reply is a short statement (roughly one line, or
  a short reply that explicitly says the brief changes no command, flag or
  CLI output and hands it to another expert) and it does NOT produce
  REQUIREMENTS/RISKS/TEST SCENARIOS about the environment variables, the
  `/healthz` endpoint, the SIGTERM handling, the Dockerfile or the restart
  policy.
  FAIL if the reply fills the three lists, or asserts confident detailed
  advice about the configuration, the health endpoint, the shutdown
  sequence, the image or the restart policy, as if the brief were in scope.
weight: 2
---

Declines the daemon-only brief in one line instead of designing its
configuration, health endpoint, shutdown or deployment.
