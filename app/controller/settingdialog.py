from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal
from app.view.SettingsDialog_ui import Ui_SettingsDialog


class SettingsDialog(QDialog, Ui_SettingsDialog):
    language_changed = Signal(str)

    def __init__(self, app_state: dict, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.app_state = app_state
       # self.setFixedSize(320, 100)

        # Idioma actual
        current = self.app_state.get("language", "Español")
        idx = self.cbLanguage.findText(current)
        if idx >= 0:
            self.cbLanguage.setCurrentIndex(idx)

        # Tema actual
        tema_actual = self.app_state.get("theme", "Azul")
        i = self.cbTema.findText(tema_actual)
        if i >= 0:
            self.cbTema.setCurrentIndex(i)

        # Botones
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def _on_theme_preview(self, theme):
        """Aplica el tema como vista previa (sin cerrar)."""
        self.style_manager.apply_theme_by_name(self.app, theme)

    def accept(self):
        new_lang = self.cbLanguage.currentText()
        self.app_state["language"] = new_lang
        self.language_changed.emit(new_lang)
        self.app_state["theme"] = self.cbTema.currentText()
        super().accept()
