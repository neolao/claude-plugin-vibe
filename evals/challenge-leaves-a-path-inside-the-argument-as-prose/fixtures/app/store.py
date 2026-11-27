"""Local store of the desktop app: one SQLite file per workspace."""
import sqlite3
from pathlib import Path


class Store:
    def __init__(self, workspace: Path):
        self.connection = sqlite3.connect(workspace / "projects.db")
        self.connection.execute("PRAGMA journal_mode=WAL")

    def save_project(self, project_id: int, rows: list) -> None:
        with self.connection:
            self.connection.execute("DELETE FROM shapes WHERE project_id = ?", (project_id,))
            self.connection.executemany(
                "INSERT INTO shapes (project_id, layer, payload) VALUES (?, ?, ?)",
                [(project_id, layer, payload) for layer, payload in rows],
            )
