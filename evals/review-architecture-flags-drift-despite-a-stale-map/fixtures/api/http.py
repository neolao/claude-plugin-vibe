"""Driving adapter: the HTTP entry point of the order API."""

import json

from core.order_service import OrderService


class OrderApi:
    def __init__(self, service: OrderService) -> None:
        self._service = service

    def post_order(self, body: bytes) -> tuple[int, bytes]:
        payload = json.loads(body)
        total = self._service.place(payload["order_id"], payload["lines"], payload.get("promo_code"))
        return 201, json.dumps({"order_id": payload["order_id"], "total_cents": total}).encode()
