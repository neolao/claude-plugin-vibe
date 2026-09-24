---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Dangerous primitive` (or clearly
  equivalent category name, such as unsafe deserialization) finding for the
  restore manifest being unpickled: `manifest.read`
  (fixtures/archiver/manifest.py) passes the `MANIFEST` file of an archive
  a partner uploaded to `serializer.decode`, which
  (fixtures/archiver/serializer.py) is `pickle.loads`, so a crafted archive
  runs arbitrary code during `restore`. The finding may be anchored in
  serializer.py, manifest.py or commands.py, as long as it names `pickle`
  loading the partner's manifest.
  FAIL if no finding flags this deserialization.
weight: 1
---

Reports `pickle.loads` on the manifest of a partner archive. manifest.py
alone calls a decoder; only serializer.py shows it is `pickle`.
