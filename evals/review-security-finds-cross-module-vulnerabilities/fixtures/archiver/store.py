import os
import shutil
import sqlite3

DB_PATH = "/srv/archiver/archiver.db"


def copy(source, target):
    os.makedirs(os.path.dirname(target), exist_ok=True)
    shutil.copyfile(source, target)


def save_share(doc_id, token, owner):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO shares (doc_id, token, owner) VALUES (?, ?, ?)",
            (doc_id, token, owner),
        )


def save_api_key(owner, key):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR REPLACE INTO api_keys (owner, key) VALUES (?, ?)",
            (owner, key),
        )
