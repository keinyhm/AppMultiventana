
from PySide6.QtWidgets import QMessageBox
from app.controller.loginwindow import LoginWindow
from app.controller.homewindow import HomeWindow
from app.view.LoginWindow_ui import Ui_LoginWindow
from app.view.HomeWindow_ui import Ui_MainWindow
from app.view.SettingsDialog_ui import Ui_SettingsDialog
from app.view.NotasDialog_ui import Ui_NotasDialog
from app.services.auth_service import AuthService
import sqlite3


class AppController:
    """Controlador principal de la aplicación."""
    def __init__(self, conn: sqlite3.Connection):
        self.auth_service = AuthService(conn)
        self.app_state = {"language": "Español"}
        self.login = LoginWindow(self.auth_service, self.on_login_success, self.app_state)
        self.home = None

    def on_login_success(self, user: str):
        """Cuando el login es correcto, abre la ventana principal."""
        self.home = HomeWindow(self.app_state, user)
        self.login.close()
        self.home.show()