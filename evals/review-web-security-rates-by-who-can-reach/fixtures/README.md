# media-portal

The customer portal of the media service, reachable from the Internet
through nginx (`deploy/nginx.conf`), which terminates TLS and proxies to
the Flask app of `app.py`. Customer accounts are created by the support
team when a contract is signed; there is no sign-up page. Support staff
use the back-office routes under `/admin/`.

`metrics.py` is a second process, the metrics sidecar, that the
Prometheus agent running on the same host scrapes; `deploy/docker-compose.yml`
is the only deployment of both.

## Running it locally

    pip install flask
    SECRET_KEY=... flask --app app run --port 5000
    python3 metrics.py
