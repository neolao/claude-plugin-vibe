# catalog

Product catalog of the shop, in two parts that deploy separately:

- `api/` — the Python service that serves the catalog and imports supplier
  feeds (`pip install .`, then `catalog-api`),
- `web/` — the Node front end that renders it (`npm ci && npm run build`).

Each part keeps its own manifest; the CI builds them in two jobs.
