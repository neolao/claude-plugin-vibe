# Backlog item 021 — Archive old transactions

## Description
The finance team wants old transactions out of the live table.

## Acceptance Criteria
1. Transactions older than 12 months are moved to the archive table.
2. The archive runs every night.
3. A one-line summary with the number of rows moved is written to the application log after each run.
