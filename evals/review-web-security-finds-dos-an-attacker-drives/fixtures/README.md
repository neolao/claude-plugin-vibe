# telemetry-gateway

The public HTTP surface of the telemetry service: devices in the field
post their traces, the dashboard exports activity, and the alerting page
fans one alert out to the on-call contacts. Served by Flask behind the
public load balancer; the device token is checked by the load balancer
before any request reaches the app.

## Running it

    pip install flask
    flask --app app run --port 5000
