from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QKeySequence
from app.view.HomeWindow_ui import Ui_MainWindow
from app.controller.notasdialog import NotasDialog
from app.controller.settingdialog import SettingsDialog
from app.translations import TRANSLATIONS


class HomeWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app_state: dict, user: str, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.app_state = app_state
        self.user = user


        # ===== Atajos y acciones =====
        self.addAction(self.actionSalir)
        self.addAction(self.actionConfiguracion)
        self.addAction(self.actionNotas)

        self.actionSalir.triggered.connect(self.close)
        self.actionConfiguracion.triggered.connect(self.open_settings)
        self.actionNotas.triggered.connect(self.open_notas)

        self.actionSalir.setShortcut(QKeySequence("Ctrl+Q"))
        self.actionConfiguracion.setShortcut(QKeySequence("Ctrl+E"))
        self.actionNotas.setShortcut(QKeySequence("Ctrl+N"))

        # ===== Traducción inicial =====
        self.apply_language()

        # ===== Mensaje inicial =====
        if self.statusBar():
            tr = TRANSLATIONS[self.app_state["language"]]
            self.statusBar().showMessage(tr["status_ok"], 3000)

    # --------------------------------------------------
    def open_settings(self):
        dlg = SettingsDialog(self.app_state, self)
        dlg.language_changed.connect(self.apply_language)
        dlg.exec()

    def open_notas(self):
        dlg = NotasDialog(self.app_state, self)
        dlg.exec()
        if self.statusBar():
            tr = TRANSLATIONS[self.app_state["language"]]
            self.statusBar().showMessage(tr["note_updated"], 3000)

    def apply_language(self):
        lang = self.app_state.get("language", "Español")
        tr = TRANSLATIONS[lang]
        self.setWindowTitle(tr["title"].format(user=self.user))
        self.actionSalir.setText(tr["exit"]);              self.actionSalir.setStatusTip(tr["tip_exit"])
        self.actionConfiguracion.setText(tr["settings"]);  self.actionConfiguracion.setStatusTip(tr["tip_settings"])
        self.actionNotas.setText(tr["notes"]);             self.actionNotas.setStatusTip(tr["tip_notes"])
        self.menuSalir.setTitle(tr["file"])
        self.menuEdicion.setTitle(tr["edit"])
        self.menuVentanas.setTitle(tr["windows"])
        if hasattr(self, "lblWelcome"):
            self.lblWelcome.setText(tr["welcome"])
        if self.statusBar():
            self.statusBar().showMessage(tr["status_ok"], 3000)
        self.menuBar().update()
        self.repaint()
