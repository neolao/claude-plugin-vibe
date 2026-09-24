import sqlite3

from address import Address
from shipment import Shipment, ShipmentNotFound

_COLUMNS = "id, cart_id, street, city, postcode, status"


class ShipmentRepository:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def get(self, shipment_id: str) -> Shipment:
        row = self._conn.execute(
            f"SELECT {_COLUMNS} FROM shipments WHERE id = ?", (shipment_id,)
        ).fetchone()
        if row is None:
            raise ShipmentNotFound(shipment_id)
        return self._to_shipment(row)

    def find_pending(self) -> list[Shipment]:
        rows = self._conn.execute(
            f"SELECT {_COLUMNS} FROM shipments WHERE status = 'pending'"
        ).fetchall()
        return [self._to_shipment(row) for row in rows]

    def find_overdue(self, days: int):
        return self._conn.execute(
            f"SELECT {_COLUMNS}, created_at FROM shipments"
            " WHERE status = 'dispatched' AND created_at < date('now', ?)",
            (f"-{days} days",),
        ).fetchall()

    def save(self, shipment: Shipment) -> None:
        self._conn.execute(
            "UPDATE shipments SET status = ? WHERE id = ?",
            (shipment.status, shipment.shipment_id),
        )
        self._conn.commit()

    @staticmethod
    def _to_shipment(row) -> Shipment:
        return Shipment(row[0], row[1], Address(row[2], row[3], row[4]), row[5])
