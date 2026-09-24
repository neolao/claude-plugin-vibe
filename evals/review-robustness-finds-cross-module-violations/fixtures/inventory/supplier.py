import requests

from . import settings
from .errors import SupplierError


class SupplierClient:
    def __init__(self, session: requests.Session):
        self._session = session

    def stock_level(self, sku: str) -> int:
        try:
            response = self._session.get(
                f"{settings.SUPPLIER_URL}/stock/{sku}",
                timeout=settings.SUPPLIER_TIMEOUT,
            )
            response.raise_for_status()
            return int(response.json()["level"])
        except (requests.RequestException, KeyError, TypeError, ValueError) as exc:
            raise SupplierError(sku) from exc
