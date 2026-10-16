---
type: llm
focus: last_message
criteria: |
  Under cron there is no terminal to answer a prompt. The script calls `ssh`
  (through rsync: a new or changed host key, an encrypted key) and `psql`
  (a password prompt when no credential file or variable is set); under
  cron either waits forever for input nobody will type.

  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, for this script,
  that the ssh/rsync or psql calls must be made non-interactive (for example
  a strict host-key policy with a pre-provisioned known_hosts, a
  passphrase-less deploy key, credentials through `.pgpass` or the
  environment, `BatchMode`), so that a missing credential or an unknown host
  makes the run fail with an error instead of hanging.
  FAIL if the reply never raises that a call in this script could block
  waiting for terminal input under cron.
weight: 2
---

Requires the ssh/rsync and psql calls to be non-interactive so a cron run
fails instead of hanging on a prompt.
