import sqlite3

from logistics.consignment import Consignment, Parcel


class ConsignmentNotFound(Exception):
    pass


class ConsignmentRepository:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def get(self, consignment_id: str) -> Consignment:
        row = self._conn.execute(
            "SELECT id, carrier, status FROM consignments WHERE id = ?", (consignment_id,)
        ).fetchone()
        if row is None:
            raise ConsignmentNotFound(consignment_id)
        return self._to_consignment(row)

    def find_closed_on(self, day: str) -> list[Consignment]:
        rows = self._conn.execute(
            "SELECT id, carrier, status FROM consignments WHERE status = 'closed' AND closed_on = ?", (day,)
        ).fetchall()
        return [self._to_consignment(row) for row in rows]

    def save(self, consignment: Consignment) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO consignments (id, carrier, status) VALUES (?, ?, ?)",
            (consignment.consignment_id, consignment.carrier, consignment.status),
        )
        self._conn.execute("DELETE FROM parcels WHERE consignment_id = ?", (consignment.consignment_id,))
        self._conn.executemany(
            "INSERT INTO parcels (consignment_id, id, weight_grams) VALUES (?, ?, ?)",
            [(consignment.consignment_id, p.parcel_id, p.weight_grams) for p in consignment.parcels],
        )
        self._conn.commit()

    def _to_consignment(self, row) -> Consignment:
        consignment = Consignment(row[0], row[1], row[2])
        for parcel_id, grams in self._conn.execute(
            "SELECT id, weight_grams FROM parcels WHERE consignment_id = ?", (row[0],)
        ).fetchall():
            consignment.add_parcel(Parcel(parcel_id, grams))
        return consignment
