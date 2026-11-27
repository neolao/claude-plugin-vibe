---
type: llm
focus: last_message
criteria: |
  `decode` in fixtures/archiver/lib/serializer.py is `pickle.loads`;
  `read` in fixtures/archiver/manifest.py, outside the scope, feeds it the
  `MANIFEST` bytes of the archive the partner site uploaded, so a crafted
  manifest runs code under the staff member's account when `archiver
  restore` unpacks it.

  PASS if the reported findings include a `Dangerous primitive` (or clearly
  equivalent category name, such as unsafe deserialization) finding whose
  FILE: line points to fixtures/archiver/lib/serializer.py, that names
  `pickle.loads`, and whose ISSUE or SUGGESTION names `manifest.read`,
  fixtures/archiver/manifest.py, the MANIFEST or the partner's archive as
  what makes the bytes external.
  FAIL if no finding reports this unpickling, or if the finding is anchored
  (its FILE: line) on fixtures/archiver/manifest.py or
  fixtures/archiver/commands.py.
weight: 1
---

Reports the unpickler in scope, with the outside manifest reader as the
evidence that the bytes are the partner's.
