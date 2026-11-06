import sqlite3
from datetime import date

from flask import Blueprint, jsonify

from subscriptions.renewal import RenewalService
from subscriptions.subscription_repository import SubscriptionRepository

bp = Blueprint("subscriptions", __name__)
renewal = RenewalService(SubscriptionRepository(sqlite3.connect("planbox.db", check_same_thread=False)))


@bp.post("/subscriptions/<subscription_id>/renew")
def renew(subscription_id: str):
    sub = renewal.renew(subscription_id, date.today())
    return jsonify({"id": sub.subscription_id, "status": sub.status, "period_end": sub.period_end.isoformat()})
