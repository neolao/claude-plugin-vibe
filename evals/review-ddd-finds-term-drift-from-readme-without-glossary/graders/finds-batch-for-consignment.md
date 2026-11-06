---
type: llm
focus: last_message
criteria: |
  There is no .vibe/ and no glossary. fixtures/README.md defines the
  consignment, and fixtures/logistics/ names it `Consignment`,
  `consignment_id`, `ConsignmentRepository`. fixtures/api/routes.py calls
  the same concept a pickup batch (`/pickup-batches/<batch_id>`,
  `pickup_batch`, `batch_id` in the payload) and fixtures/reports/daily.py
  calls it `batch` ("Batch ..." in the summary line).

  PASS if the reported findings include a `Ubiquitous language` (or clearly
  equivalent category name) finding anchored on fixtures/api/routes.py or
  fixtures/reports/daily.py for the batch / consignment split, whose
  SUGGESTION aligns on `consignment` (the README's and the domain's word),
  not on `batch` or a third term.
  FAIL if no finding flags the split, or if the suggestion renames the
  domain to batch or proposes a third word.
weight: 2
---

Reports the layers that drift from the term the README and the domain
settle, without a glossary to point at.
