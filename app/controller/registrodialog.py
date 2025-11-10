from PySide6.QtWidgets import QWidget, QStatusBar
from PySide6.QtCore import Qt
from app.view.RegistroDialog_ui import Ui_RegistroDialog
from app.translations import TRANSLATIONS
from app.services import auth_service

class RegistroDialog(QWidget, Ui_RegistroDialog):
    def __init__(self, auth_service: auth_service.AuthService, parent=None):
        super().__init__(parent)
        
        self.auth_service = auth_service
        
        self.setupUi(self)
        
        self.btnAcep.clicked.connect(self.handle_register)
        self.pushButton_2.clicked.connect(self.reject) 

        self.lePwd.setEchoMode(self.lePwd.EchoMode.Password)

    
    def handle_register(self):
        """
        Esta función se ejecuta al pulsar 'Aceptar'.
        """
        
        username = self.leUs.text().strip() 
        password = self.lePwd.text()

        if not username or not password:
            self.lblMsg.setText("Usuario y contraseña no pueden estar vacíos.")
            self.lblMsg.setStyleSheet("color: red;")
            return

        try:
            success = self.auth_service.create_user(username, password)
            
            if success:
                self.accept()
            else:
                self.lblMsg.setText("Ese nombre de usuario ya existe. Prueba con otro.")
                self.lblMsg.setStyleSheet("color: red;")
        
        except Exception as e:
            print(f"Error inesperado al crear usuario: {e}")
            self.lblMsg.setText("Error inesperado. Intenta de nuevo.")
            self.lblMsg.setStyleSheet("color: red;")