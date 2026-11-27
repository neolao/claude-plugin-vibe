import os
import shutil
import sqlite3
from pathlib import Path

from .lib import serializer

DB_PATH = "/srv/archiver/archiver.db"
INDEX_PATH = Path("/srv/archiver/index.bin")


def copy(source, target):
    os.makedirs(os.path.dirname(target), exist_ok=True)
    shutil.copyfile(source, target)


def load_index():
    if not INDEX_PATH.exists():
        return {}
    return serializer.decode(INDEX_PATH.read_bytes())


def save_index(index):
    INDEX_PATH.write_bytes(serializer.encode(index))


def save_share(doc_id, token, owner):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            f"INSERT INTO shares (doc_id, token, owner) VALUES ('{doc_id}', '{token}', '{owner}')"
        )


def save_api_key(owner, key):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR REPLACE INTO api_keys (owner, key) VALUES (?, ?)",
            (owner, key),
        )
