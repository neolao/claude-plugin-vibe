---
status: todo
---
# Retry Failed Invoice Emails

## Description
Re-send an invoice email that bounced, up to three times.

## Acceptance Criteria
- [ ] A bounced invoice email is re-sent up to three times.

## Notes
Cannot start until billing-jobs#001 is done — the retry queue lives in billing-jobs.
