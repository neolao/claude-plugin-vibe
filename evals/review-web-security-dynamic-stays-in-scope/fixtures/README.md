# media-portal

The public HTTP surface of the media portal: uploads, search, avatars and the
support back-office.

## Running it

    pip install flask
    flask --app app run --port 5000

## Environments

| Environment | URL |
|---|---|
| Local | http://127.0.0.1:5000 |
| Staging | https://staging.media-portal.example.com |
| Production | https://media-portal.example.com |

Support and the on-call rota use the production URL; staging mirrors it with a
copy of last night's data.
