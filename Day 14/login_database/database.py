# database.py

import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Insert default user (for testing)
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                   ("admin", "1234"))

    conn.commit()
    conn.close()


def check_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (username, password))

    user = cursor.fetchone()
    conn.close()

    return user is not None
