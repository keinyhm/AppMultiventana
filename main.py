import sys
from PySide6.QtWidgets import QApplication
from app.data.db import init_db
from app.controller.AppController import AppController


def main():
    init_db()
    
    app = QApplication(sys.argv)
    app.setApplicationName("App Qt Escalable")
     # Aplica el estilo global a toda la app
    #style_manager = StyleManager()
    #style_manager.apply_app_style(app, "main_style.qss")

    controller = AppController()
    controller.login.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
