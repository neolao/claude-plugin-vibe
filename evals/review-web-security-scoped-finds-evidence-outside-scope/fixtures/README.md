# media-portal

The public HTTP surface of the media portal, served by Flask behind the
public load balancer. Anyone can sign up; support staff get the `admin`
role. `portal/app.py` builds the application, wires the login check and
the response headers, and registers the route modules of `portal/routes/`;
`portal/storage.py`, `portal/users.py` and `portal/orders.py` hold the
helpers the routes call.

## Running it

    pip install flask
    SECRET_KEY=... flask --app portal.app run --port 5000
