---
type: llm
focus: last_message
criteria: |
  `decode` in fixtures/archiver/lib/serializer.py is `pickle.loads`. Its
  only caller, `load_index` in fixtures/archiver/store.py (outside the
  scope), reads /srv/archiver/index.bin, which `save_index` in the same
  file wrote with `serializer.encode` and which the README says only the
  tool writes; the partner's MANIFEST is parsed with `json.loads` in
  fixtures/archiver/manifest.py and never reaches `decode`.

  PASS if no `high` or `medium` severity `Dangerous primitive` (or clearly
  equivalent category name, such as unsafe deserialization) finding
  targets `decode` or `pickle.loads`. A `low` finding passes, and so does
  a report with no findings at all.
  FAIL if the unpickling is reported as deserializing external, partner or
  untrusted data at high or medium severity.
weight: 1
---

Does not call an unpickler a dangerous primitive when the only bytes it
receives, traced outside the scope, are the tool's own.
