# Limits

Every limit the service enforces, with the error a caller gets when it is exceeded.

| Limit | Value | Error |
|---|---|---|
| Rows per CSV import | 10 000 | `statement too large` |
| Attachments per transaction | 5 | `too many attachments` |
| Attachment size | 8 MB | `attachment too large` |
| Reconciliation timeout | 60 s | `reconciliation timed out` |

The row cap applies before parsing: a file over the limit is rejected without reading its content.
