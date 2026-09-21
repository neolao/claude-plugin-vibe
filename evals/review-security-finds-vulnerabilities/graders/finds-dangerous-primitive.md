---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Dangerous primitive` (or clearly
  equivalent category name) finding on `load_plugin_config` calling
  `yaml.load` without `SafeLoader` on a file the customer supplies,
  recommending `yaml.safe_load` or an explicit safe loader.
  FAIL if the unsafe YAML load is not flagged.
weight: 1
---

Reports the `yaml.load` without SafeLoader as a Dangerous primitive finding.
