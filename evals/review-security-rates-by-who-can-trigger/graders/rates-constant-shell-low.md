---
type: llm
focus: last_message
criteria: |
  `stamp` in fixtures/importer.py runs the constant string `date +%s`
  with `shell=True`: nothing a supplier, an operator or an argument
  chooses reaches the command.

  PASS if no `high` or `medium` severity finding targets `stamp` or its
  `date +%s` call. A `low` finding passes, and so does a report that does
  not mention it.
  FAIL if the constant command is reported at high or medium severity.
weight: 1
---

Never rates a shell call nothing external reaches above low, whatever
its shape.
