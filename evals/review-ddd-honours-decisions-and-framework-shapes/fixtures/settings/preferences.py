import sqlite3
from dataclasses import dataclass


@dataclass
class ShopPreferences:
    """What the admin page lets the shop owner set."""

    shop_name: str
    support_email: str
    currency: str
    items_per_page: int


class PreferencesRepository:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def get(self) -> ShopPreferences:
        row = self._conn.execute(
            "SELECT shop_name, support_email, currency, items_per_page FROM preferences WHERE id = 1"
        ).fetchone()
        return ShopPreferences(*row)

    def save(self, prefs: ShopPreferences) -> None:
        self._conn.execute(
            "UPDATE preferences SET shop_name = ?, support_email = ?, currency = ?, items_per_page = ? WHERE id = 1",
            (prefs.shop_name, prefs.support_email, prefs.currency, prefs.items_per_page),
        )
        self._conn.commit()
