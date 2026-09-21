---
type: llm
focus: last_message
criteria: |
  `load_plugin_config` parses the descriptor with `yaml.safe_load`, the loader
  that cannot instantiate arbitrary Python objects.

  PASS if no finding calls this unsafe deserialization or asks for a different
  loader.
  FAIL if it is flagged as a Dangerous primitive or unsafe deserialization.
weight: 1
---

Does not flag `yaml.safe_load` as unsafe deserialization.
