import sqlite3
import hashlib
from app.models import users
from typing import Optional

class AuthService:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self._ensure_admin()

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def create_user(self, username: str, password: str) -> bool:
        hash_pass = self._hash_password(password)
        cur = self.conn.cursor()
        try:
            cur.execute(
                "INSERT INTO usuarios (username, password) VALUES (?, ?)",
                (username, hash_pass),
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def authenticate(self, username: str, password: str) -> Optional[users]:
        hash_pass = self._hash_password(password)
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM usuarios WHERE username = ? AND password = ?",
            (username, hash_pass),
        )
        row = cur.fetchone()
        if row:
            return users(
                id=row["id"],
                username=row["username"],
                password=row["password"],
            )
        return None

    def _ensure_admin(self) -> None:
        cur = self.conn.cursor()
        cur.execute("SELECT 1 FROM usuarios WHERE username = ?", ("admin",))
        if cur.fetchone() is None:
            self.create_user("admin", "1234")
