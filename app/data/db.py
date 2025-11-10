import sqlite3
from pathlib import Path

DB_PATH = Path("usuarios.db")

def get_connection() ->  sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db() -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
         )        
    """)
    print(f" Base de datos creada en: {DB_PATH.resolve()}")
    conn.commit()
    conn.close()

def check_user(username: str, password: str) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT 1 FROM usuarios WHERE username=? AND password=?",
        (username, password)
    )
    result = cur.fetchone()
    conn.close()
    return result is not None
