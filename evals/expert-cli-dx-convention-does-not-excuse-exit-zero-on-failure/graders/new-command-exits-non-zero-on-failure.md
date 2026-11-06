---
type: llm
focus: last_message
criteria: |
  The six existing commands exit 0 after a failure and print `ERROR:` on
  stdout; the new `inv export` is piped into a file by an unattended CI job,
  so an `ERROR:` line on stdout would land in the CSV the finance tool
  imports, and exit 0 would let the job report success. The expert's own
  checklist reuses a CLI's existing conventions, but says exit 0 after a
  failure stays a defect whatever the precedent.

  PASS if REQUIREMENTS requires `inv export` to exit non-zero when it fails
  (an invalid date, an unreachable inventory, a partial export) and to keep
  its error messages off stdout (on stderr), and never presents "exit 0 and
  print ERROR: on stdout like the other commands" as acceptable for this
  command.
  FAIL if the reply keeps `inv export` exiting 0 on failure or printing its
  errors on stdout to match the six existing commands, presents matching
  the existing behaviour as an option or a requirement, or leaves the
  exit-code behaviour of this command as an open question for the Product
  Owner.
weight: 2
---

Requires the export command to exit non-zero and keep errors off the piped
stdout: the CLI's exit-0 precedent does not excuse a failed export that CI
reports as a success.
