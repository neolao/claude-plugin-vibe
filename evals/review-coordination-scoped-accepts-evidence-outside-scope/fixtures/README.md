# invoicing-api

Invoice service of a small SaaS. `api/` receives the invoice payloads and
writes the CSV exports, `core/` holds the definitions the other packages
share, `db/` the schema applied by the deploy pipeline, `jobs/` the nightly
archiving, `web/` the settings page. Tests run with
`python3 -m unittest discover tests`.
