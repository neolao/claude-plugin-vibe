import os
import subprocess
import sqlite3
import bcrypt

API_KEY = os.environ["API_KEY"]


def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()


def run_backup(directory):
    subprocess.run(["tar", "-czf", "backup.tar.gz", directory], shell=False)


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
