---
type: llm
focus: last_message
criteria: |
  The fixture's `reportkit/formats.py` holds one plain function per format
  and a `FORMATS` dict keyed by the format name; `reportkit/cli.py` picks
  the function from the dict and lists the dict's keys in its help. That is
  the repo's idiom for exactly this problem; the expert's rule says it
  beats an imported pattern even where the expert would pick otherwise.

  PASS if the reply makes the Markdown format land as one more function in
  `reportkit/formats.py` plus one `FORMATS` entry — either as a one-line
  reply naming that idiom, or as the baseline that wins and is
  recommended.
  FAIL if the reply recommends a Formatter base class or Strategy classes,
  a `formats/` package with one module per format, plugin discovery, or any
  structure other than the function dict for the Markdown format, or
  describes the dict as a defect or an anti-pattern.
weight: 2
---

Follows the repo's function-registry idiom for the new format instead of
prescribing the textbook class hierarchy.
