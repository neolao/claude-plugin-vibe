# invoicing-api

Invoice service of a small SaaS. `api/` receives the invoice payloads and
writes the CSV exports, `db/` holds the schema applied by the deploy
pipeline, `jobs/` runs the nightly archiving, `web/` serves the settings
page. No test suite yet.
