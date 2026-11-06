---
type: llm
focus: last_message
criteria: |
  Exit code 2 has meant "the node does not exist" for four years and the
  autoscaler's scripts branch on it. The expert's checklist says the meaning
  of exit-code values already in use is reused as it is, and that a failure
  never exits 0.

  PASS if REQUIREMENTS or TEST SCENARIOS keeps exit code 2 for an unknown
  node on `fleet drain` (or at least never gives 2 another meaning), and
  gives a failed drain (a workload that could not be moved, the cordon
  failing) a non-zero exit code distinct from 2.
  FAIL if the reply assigns exit code 2 to another failure class (a usage
  error, a timeout, a partial drain), proposes a fresh exit-code scheme for
  the new subcommand that remaps 2, or lets a failed drain exit 0.
weight: 2
---

Keeps exit code 2 meaning "node not found" for the scripts that branch on
it, and gives a failed drain its own distinct non-zero code.
