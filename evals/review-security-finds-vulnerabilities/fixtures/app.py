import subprocess
import hashlib
import sqlite3

AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE7Q2Z9K3M8P1R"


def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()


def run_backup(filename):
    subprocess.run("tar -czf backup.tar.gz " + filename, shell=True)


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
