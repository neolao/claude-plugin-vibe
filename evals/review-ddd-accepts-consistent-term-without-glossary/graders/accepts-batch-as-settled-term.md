---
type: llm
focus: last_message
criteria: |
  There is no .vibe/, no glossary, and fixtures/README.md defines no
  vocabulary beyond calling the model a batch. `Batch`, `batch_id`,
  `BatchRepository`, `/batches/<batch_id>` and the summary's "Batch" are
  the one name fixtures/logistics/, fixtures/api/ and fixtures/reports/ use
  for the concept.

  PASS if no `high` or `medium` severity Ubiquitous language finding
  claims `Batch` is a technical term, that the business would say
  consignment, shipment, pickup or another word, or that the concept goes
  under two names. A report with no findings at all passes.
  FAIL if `Batch` (or one of its derived names) is flagged for one of
  those reasons at high or medium severity.
weight: 2
---

Invents no vocabulary: with nothing that settles another word, the one
name the code uses everywhere is the ubiquitous language.
