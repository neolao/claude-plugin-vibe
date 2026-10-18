# Backlog item 012 — Export the monthly report

## Description
Admins download the monthly report from the admin page.

## Acceptance Criteria
1. The export is a CSV file with one line per transaction: date, amount, label.
2. Lines are sorted by date, oldest first.
3. The file name is `report-<YYYY-MM>.csv`.

## Constraints
- Do not change the signature of `export_report(rows, month)`: the admin page calls it.
