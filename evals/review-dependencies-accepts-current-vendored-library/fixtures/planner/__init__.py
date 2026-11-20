"""Leave planner: one page to book days off, one JSON endpoint to list them."""
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

_bookings: list[dict] = []


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/bookings")
def list_bookings():
    return jsonify(_bookings)


@app.post("/bookings")
def book():
    booking = {"employee": request.json["employee"], "day": request.json["day"]}
    _bookings.append(booking)
    return jsonify(booking), 201
