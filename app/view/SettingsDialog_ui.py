# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(495, 328)
        Dialog.setStyleSheet(u"background-color: #f5f5dc;\n"
"")
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 50, 421, 221))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(8)
        self.formLayout.setContentsMargins(12, 12, 12, 12)
        self.lblIdioma = QLabel(self.formLayoutWidget)
        self.lblIdioma.setObjectName(u"lblIdioma")
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(12)
        self.lblIdioma.setFont(font)
        self.lblIdioma.setStyleSheet(u"color: black;")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblIdioma)

        self.cbLanguage = QComboBox(self.formLayoutWidget)
        self.cbLanguage.addItem("")
        self.cbLanguage.addItem("")
        self.cbLanguage.addItem("")
        self.cbLanguage.setObjectName(u"cbLanguage")
        self.cbLanguage.setEnabled(True)
        self.cbLanguage.setStyleSheet(u"color: black;")
        self.cbLanguage.setEditable(True)
        self.cbLanguage.setMaxVisibleItems(3)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cbLanguage)

        self.buttonBox = QDialogButtonBox(self.formLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"color:black;")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.buttonBox)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lblIdioma.setText(QCoreApplication.translate("Dialog", u"Idioma", None))
        self.cbLanguage.setItemText(0, QCoreApplication.translate("Dialog", u"Espa\u00f1ol", None))
        self.cbLanguage.setItemText(1, QCoreApplication.translate("Dialog", u"Ingl\u00e9s", None))
        self.cbLanguage.setItemText(2, QCoreApplication.translate("Dialog", u"Franc\u00e9s", None))

#if QT_CONFIG(tooltip)
        self.cbLanguage.setToolTip(QCoreApplication.translate("Dialog", u"Selecciona un idioma (solo ejemplo, no cambia nada)", None))
#endif // QT_CONFIG(tooltip)
        self.cbLanguage.setCurrentText(QCoreApplication.translate("Dialog", u"Espa\u00f1ol", None))
    # retranslateUi

