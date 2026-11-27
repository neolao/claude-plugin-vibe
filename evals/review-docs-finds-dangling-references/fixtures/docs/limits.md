# Limits

| Limit | Value | Error |
|---|---|---|
| Rows per CSV import | 10 000 | `statement too large` |
| Attachments per transaction | 5 | `too many attachments` |
| Attachment size | 8 MB | `attachment too large` |

The row cap applies before parsing: a file over the limit is rejected without reading its content.
