from PySide6.QtWidgets import QApplication
from pathlib import Path

class StyleManager:
    """Gestiona los estilos visuales de la aplicación."""
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.available_themes = {
            "Azul": "main_style.qss",
            "Rojo": "red_style.qss",
            "Verde": "green_style.qss"
        }

    def apply_app_style(self, app: QApplication, style_name: str = "main_style.qss"):
        """Aplica el estilo a toda la aplicación."""
        style_path = self.base_path / style_name
        if style_path.exists():
            with open(style_path, "r", encoding="utf-8") as f:
                app.setStyleSheet(f.read())
        else:
            print(f"⚠️ No se encontró el estilo: {style_path}")

    def apply_theme_by_name(self, app: QApplication, theme_name: str):
        """Aplica un tema según su nombre (Azul, Rojo, Verde)."""
        filename = self.available_themes.get(theme_name, "main_style.qss")
        self.apply_app_style(app, filename)
