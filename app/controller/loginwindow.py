from PySide6.QtWidgets import QWidget, QStatusBar, QDialog, QMessageBox
from PySide6.QtCore import Qt
from app.view.LoginWindow_ui import Ui_LoginWindow
from app.translations import TRANSLATIONS
from app.services.auth_service import AuthService
from app.controller.registrodialog import RegistroDialog

class LoginWindow(QWidget, Ui_LoginWindow):
    def __init__(self, auth_service: AuthService, on_success, app_state: dict, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.on_success = on_success
        self.app_state = app_state
        # Quitar barra de título y bordes del sistema
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.auth_service = auth_service
        
        # Barra de estado
        self.status_bar = QStatusBar(self)
        self.formLayout.addWidget(self.status_bar)
        self.status_bar.showMessage("Introduce tus credenciales")

        # Conexiones
        self.btnLogin.clicked.connect(self.try_login)
        self.leUser.returnPressed.connect(self.focus_next_field)
        self.lePass.returnPressed.connect(self.try_login)

        self.btnRegistro.clicked.connect(self.abrir_dialogo_registro)

        # Traducir interfaz inicial
        self.apply_language()

    def focus_next_field(self):
        self.lePass.setFocus()

    def try_login(self):
        lang = self.app_state.get("language", "Español")
        tr = TRANSLATIONS[lang]

        user = self.leUser.text().strip()
        pw = self.lePass.text()

        if user and pw:
            self.status_bar.showMessage(tr["login_success"], 3000)
            self.on_success(user)
            self.app_state["user"]=user
        else:
            self.status_bar.showMessage(tr["login_error"], 3000)
            self.lePass.clear()
            self.lePass.setFocus()

    def abrir_dialogo_registro(self):
        """
        Crea y muestra la ventana de registro.
        """
        dialogo = RegistroDialog(self.auth_service, self)
        
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            QMessageBox.information(
                self, 
                "Registro Exitoso", 
                "¡Usuario creado! Ya puedes iniciar sesión."
            )
        else:
            print("Registro cancelado.")


    def apply_language(self):
        """Actualiza los textos de la interfaz según el idioma."""
        lang = self.app_state.get("language", "Español")
        tr = TRANSLATIONS[lang]

        self.setWindowTitle(tr["login_title"])
        self.leUser.setText(tr["login_user"])
        self.lePass.setText(tr["login_pass"])
        self.btnLogin.setText(tr["login_button"])
