"""HTTP entry point: partners POST a YAML report spec and get the signed HTML back."""
from flask import Flask, request

import yaml

from .render import render_report

app = Flask(__name__)


@app.post("/reports")
def create_report():
    spec = yaml.load(request.data, Loader=yaml.FullLoader)
    return render_report(spec)
