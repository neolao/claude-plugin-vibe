---
type: llm
focus: last_message
criteria: |
  `load_cache` in fixtures/importer.py unpickles /var/cache/importer/
  last.pkl, which `save_cache` in the same file writes with
  `pickle.dumps` and which the README says only the tool writes. The
  bytes are the tool's own.

  PASS if no `high` or `medium` severity `Dangerous primitive` (or
  clearly equivalent category name, such as unsafe deserialization)
  finding targets `load_cache` or its `pickle.loads`. A `low` finding
  passes, and so does a report with no findings at all.
  FAIL if the unpickling is reported as deserializing external or
  untrusted data at high or medium severity.
weight: 1
---

Does not rate an unpickler above low when the only bytes it reads are
the tool's own.
