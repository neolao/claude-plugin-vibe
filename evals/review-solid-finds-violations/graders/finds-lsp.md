---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `L` (or clearly equivalent LSP)
  finding on `ReadOnlyAuditRepository.delete`, for throwing on a method it
  inherits from `BaseRepository` instead of supporting it — a substitution
  failure for callers that treat it as a `BaseRepository`.
  FAIL if no finding flags `ReadOnlyAuditRepository.delete` for this reason.
weight: 1
---

Reports `ReadOnlyAuditRepository.delete` throwing on an inherited method as
an `L` finding.
