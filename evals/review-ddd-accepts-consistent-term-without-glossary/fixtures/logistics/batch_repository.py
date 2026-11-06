import sqlite3

from logistics.batch import Batch, Parcel


class BatchNotFound(Exception):
    pass


class BatchRepository:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def get(self, batch_id: str) -> Batch:
        row = self._conn.execute(
            "SELECT id, carrier, status FROM batches WHERE id = ?", (batch_id,)
        ).fetchone()
        if row is None:
            raise BatchNotFound(batch_id)
        return self._to_batch(row)

    def find_closed_on(self, day: str) -> list[Batch]:
        rows = self._conn.execute(
            "SELECT id, carrier, status FROM batches WHERE status = 'closed' AND closed_on = ?", (day,)
        ).fetchall()
        return [self._to_batch(row) for row in rows]

    def save(self, batch: Batch) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO batches (id, carrier, status) VALUES (?, ?, ?)",
            (batch.batch_id, batch.carrier, batch.status),
        )
        self._conn.execute("DELETE FROM parcels WHERE batch_id = ?", (batch.batch_id,))
        self._conn.executemany(
            "INSERT INTO parcels (batch_id, id, weight_grams) VALUES (?, ?, ?)",
            [(batch.batch_id, p.parcel_id, p.weight_grams) for p in batch.parcels],
        )
        self._conn.commit()

    def _to_batch(self, row) -> Batch:
        batch = Batch(row[0], row[1], row[2])
        for parcel_id, grams in self._conn.execute(
            "SELECT id, weight_grams FROM parcels WHERE batch_id = ?", (row[0],)
        ).fetchall():
            batch.add_parcel(Parcel(parcel_id, grams))
        return batch
