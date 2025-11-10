from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import Qt
from app.view.NotasDialog_ui import Ui_NotasDialog
from app.translations import TRANSLATIONS


class NotasDialog(QDialog, Ui_NotasDialog):
    def __init__(self, app_state: dict, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.app_state = app_state

        self.apply_language()

        # Cargar nota guardada
        self.teNotas.setPlainText(self.app_state.get("note", ""))

        # Conectar botones (OK / Cancel)
        self.buttonBox.accepted.connect(self._guardar_y_cerrar)
        self.buttonBox.rejected.connect(self.reject)

        # Autoguardado
        self.teNotas.textChanged.connect(self._autosave)

    def apply_language(self):
        """Aplica las traducciones según el idioma activo."""
        lang = self.app_state.get("language", "Español")
        tr = TRANSLATIONS[lang]

        self.setWindowTitle(tr.get("notes_title", tr.get("notes", "Notas rápidas")))
        self.lblNotas.setText(tr.get("notes_label", "Escribe tus notas:"))
        self.teNotas.setPlaceholderText(
            tr.get("notes_placeholder", "Escribe tus notas aquí (no se guardan).")
        )

        ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        cancel_button = self.buttonBox.button(QDialogButtonBox.Cancel)
        if ok_button:
            ok_button.setText(tr.get("ok", "Aceptar"))
        if cancel_button:
            cancel_button.setText(tr.get("cancel", "Cancelar"))

    def _guardar_y_cerrar(self):
        """Guarda la nota en el estado global y cierra el diálogo."""
        self.app_state["note"] = self.teNotas.toPlainText().strip()
        self.accept()

    def _autosave(self):
        """Autoguarda cada cambio en memoria."""
        self.app_state["note"] = self.teNotas.toPlainText()

        
