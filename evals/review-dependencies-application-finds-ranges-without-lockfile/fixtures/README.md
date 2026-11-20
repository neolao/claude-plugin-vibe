# invoice-worker

Background worker of the billing platform: it pops invoice jobs from the
queue, fetches the customer and the lines from the billing API and renders
the PDF into the shared bucket.

## Deploying

The worker runs from this checkout on the worker hosts, through the
`Dockerfile` at the root:

```
docker build -t invoice-worker .
docker run invoice-worker --queue invoices
```

Without Docker: `pip install .` in a virtualenv, then `invoice-worker --queue
invoices`. `BILLING_API_URL` and `BILLING_API_TOKEN` must be set.

## Developing

`pip install -e .[dev]`, then `pytest`.
