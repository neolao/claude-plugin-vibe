import sqlite3
from dataclasses import asdict
from datetime import date

from flask import Blueprint, jsonify

from api.presenters import to_response
from subscriptions.renewal import RenewSubscription
from subscriptions.subscription_repository import SubscriptionRepository

bp = Blueprint("subscriptions", __name__)
renew_subscription = RenewSubscription(SubscriptionRepository(sqlite3.connect("planbox.db", check_same_thread=False)))


@bp.post("/subscriptions/<subscription_id>/renew")
def renew(subscription_id: str):
    sub = renew_subscription.execute(subscription_id, date.today())
    return jsonify(asdict(to_response(sub)))
