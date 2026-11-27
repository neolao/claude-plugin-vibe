"""Public HTTP surface of the telemetry gateway."""

import threading

from flask import Flask, request

app = Flask(__name__)

TRACE_DIR = "/var/data/traces"


@app.route("/traces", methods=["POST"])
def upload_trace():
    """Stores the trace a device posts, one request per trace."""
    chunks = []
    while True:
        chunk = request.stream.read(65536)
        if not chunk:
            break
        chunks.append(chunk)
    body = b"".join(chunks)
    store_trace(request.headers.get("X-Device-Id", "unknown"), body)
    return "", 204


@app.route("/export")
def export():
    """Builds the activity export shown on the dashboard."""
    rows = int(request.args.get("rows", 1000))
    return render_export(rows)


@app.route("/alerts/fanout", methods=["POST"])
def fanout():
    """Sends one alert to each on-call contact the page lists."""
    contacts = request.get_json().get("contacts", [])
    for contact in contacts:
        threading.Thread(target=notify, args=(contact,)).start()
    return "", 202


def store_trace(device_id, body):
    with open(f"{TRACE_DIR}/{device_id}.bin", "ab") as f:
        f.write(body)


def render_export(rows):
    lines = []
    for i in range(rows):
        lines.append(f"{i},activity")
    return "\n".join(lines)


def notify(contact):
    pass
