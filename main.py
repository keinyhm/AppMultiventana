import sys
import sqlite3
from PySide6.QtWidgets import QApplication
from app.data.db import init_db, get_connection
from app.controller.AppController import AppController
from app.styles.style_manager import StyleManager


def main():
    init_db()
    
    app = QApplication(sys.argv)
    app.setApplicationName("App Qt Escalable")

    style_manager = StyleManager()
    style_manager.apply_app_style(app, "main_style.qss")

    conn = get_connection()

    try:
        controller = AppController(conn)
        controller.login.show()

        sys.exit(app.exec())
        
    except Exception as e:
        print(f"Error principal de la aplicación: {e}")
        sys.exit(1)
        
    finally:
        if conn:
            conn.close()
            print("Conexión a la base de datos cerrada.")


if __name__ == "__main__":
    main()
