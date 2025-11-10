# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NotasDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QSizePolicy, QTextEdit,
    QWidget)

class Ui_NotasDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(528, 325)
        Dialog.setStyleSheet(u"background-color: #f5f5dc;")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblNotas = QLabel(Dialog)
        self.lblNotas.setObjectName(u"lblNotas")
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(16)
        self.lblNotas.setFont(font)
        self.lblNotas.setStyleSheet(u"color: black;")
        self.lblNotas.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lblNotas, 0, 0, 1, 1)

        self.teNotas = QTextEdit(Dialog)
        self.teNotas.setObjectName(u"teNotas")
        self.teNotas.setStyleSheet(u"color: black")
        self.teNotas.setAcceptRichText(False)

        self.gridLayout.addWidget(self.teNotas, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"color: black;")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lblNotas.setText(QCoreApplication.translate("Dialog", u"Escribe tus notas", None))
        self.teNotas.setPlaceholderText(QCoreApplication.translate("Dialog", u"Escribe tus notas aqui (no se guardan)", None))
    # retranslateUi

