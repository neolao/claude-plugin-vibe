from dataclasses import dataclass


class GatewayError(Exception):
    pass


@dataclass
class RefundResult:
    ok: bool
    code: str  # "declined", "expired_card", "already_refunded", "limit_exceeded"...
    payment_id: str


class Gateway:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def capture(self, payment_id, cents):
        response = self.session.post(
            f"{self.base_url}/captures",
            json={"payment_id": payment_id, "cents": cents},
            timeout=10,
        )
        if response.status_code != 201:
            raise GatewayError(f"capture {payment_id}: HTTP {response.status_code}")

    def refund(self, payment_id, cents):
        response = self.session.post(
            f"{self.base_url}/refunds",
            json={"payment_id": payment_id, "cents": cents},
            timeout=10,
        )
        code = response.json().get("code", "ok")
        return RefundResult(ok=response.status_code == 201, code=code, payment_id=payment_id)
