#Capa que contiene los métodos que van directamente a la base de datos
from app.data.db import get_connection
from app.models.users import users

class UserRepository:
    def get_by_username(self, username: str):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, username, password FROM users WHERE username = ?", (username))
        row = cur.fetchone()
        conn.close()
        return users(*row) if row else None
    
    #Funcion de crear un nuevo usuario(ya la tenía en auth services pero la paso acá para respetar la arq)
    def create(self, username: str, password: str):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?", (username, password))
        conn.commit()
        user_id = cur.lastrowid
        conn.close()
        return users(user_id, username, password)
    
    #Funcion de actualizar contraseña
    def update_password(self, username: str, new_password_hash: str) -> bool:
        conn = get_connection
        cur = conn.cursor()
        cur.execute("UPDATE users SET password=? WHERE username=?", (new_password_hash, username))
        conn.commit()
        updated = cur.rowcount > 0
        conn.close()
        return updated
    
    def delete(self, username: str) -> bool:
        conn = get_connection
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE username=?", (username))
        conn.commit()
        deleted = cur.rowcount > 0
        conn.close()
        return deleted
    
    def list_all(self):
        conn = get_connection()#se obtiene la conexión
        cur = conn.cursor()#se inicia el cursor con la conexión
        #se ejecuta la sentencia
        cur.execute("SELECT id, username, password FROM users ORDER BY username ASC")
        #se hace un fetch para que recorra todas las filas
        rows = cur.fetchall()
        conn.close()#se cierra la aplicacion
        try:
            return [users(*r) for r in rows]
        except Exception:
            return rows
