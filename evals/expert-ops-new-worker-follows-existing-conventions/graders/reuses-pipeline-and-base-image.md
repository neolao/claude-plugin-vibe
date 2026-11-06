---
type: llm
focus: last_message
criteria: |
  The brief says every service is built by the same GitLab pipeline
  template (stages `lint`, `test`, `image`, `deploy`) from the company's
  hardened `python-base` image and deployed by the platform team's Helm
  chart. The expert's own checklist says the project's pipeline and its
  stages, its base image and its deploy manifests are reused as they are.

  PASS if REQUIREMENTS has the worker built and deployed through the
  existing pipeline template and stages, from the `python-base` image, and
  deployed through the existing Helm chart (a new workload or values in
  that chart) — and prescribes no pipeline, image or deploy mechanism of its
  own.
  FAIL if any REQUIREMENTS entry prescribes, for the worker, a Dockerfile
  from a different base image (`python:3.x-slim`, a distroless or
  alpine image), a pipeline or stages of its own, or a deploy outside the
  existing Helm chart. A different image or pipeline suggested only in
  RISKS as a gap still passes.
weight: 2
---

Wires the worker into the existing pipeline template, base image and Helm
chart, instead of prescribing a Dockerfile and a pipeline of its own.
