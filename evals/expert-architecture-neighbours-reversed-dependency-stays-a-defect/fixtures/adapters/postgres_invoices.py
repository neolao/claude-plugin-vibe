"""Loads and stores invoices in Postgres."""

import psycopg
from dataclasses import dataclass


@dataclass(frozen=True)
class Invoice:
    id: int
    account_id: int
    amount: float


class PostgresInvoices:
    def __init__(self, conn):
        self.conn = conn

    @classmethod
    def from_env(cls):
        return cls(psycopg.connect())

    def create(self, account_id, amount):
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO invoices (account_id, amount) VALUES (%s, %s) RETURNING id", (account_id, amount))
            (invoice_id,) = cur.fetchone()
        return Invoice(invoice_id, account_id, amount)

    def for_month(self, account_id, month):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, account_id, amount FROM invoices WHERE account_id = %s AND to_char(issued_at, 'YYYY-MM') = %s", (account_id, month))
            return [Invoice(*row) for row in cur.fetchall()]
