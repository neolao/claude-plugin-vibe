"""Public HTTP surface of the link-shortener."""

from flask import Flask, redirect, request

app = Flask(__name__)

LINKS = {}


@app.route("/shorten", methods=["POST"])
def shorten():
    target = request.form["url"]
    slug = str(len(LINKS))
    LINKS[slug] = target
    return slug


@app.route("/go/<slug>")
def follow(slug):
    return redirect(LINKS[slug])
