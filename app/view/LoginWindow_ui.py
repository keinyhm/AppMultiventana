# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(495, 323)
        Form.setStyleSheet(u"background-color: #f5f5dc;")
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 60, 401, 221))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(8)
        self.formLayout.setContentsMargins(12, 12, 12, 12)
        self.lblUser = QLabel(self.formLayoutWidget)
        self.lblUser.setObjectName(u"lblUser")
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(12)
        self.lblUser.setFont(font)
        self.lblUser.setStyleSheet(u"color: black;")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblUser)

        self.leUser = QLineEdit(self.formLayoutWidget)
        self.leUser.setObjectName(u"leUser")
        self.leUser.setStyleSheet(u"color: black;")
        self.leUser.setMaxLength(24)
        self.leUser.setEchoMode(QLineEdit.EchoMode.Normal)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leUser)

        self.lblContra = QLabel(self.formLayoutWidget)
        self.lblContra.setObjectName(u"lblContra")
        self.lblContra.setFont(font)
        self.lblContra.setStyleSheet(u"color: black;")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblContra)

        self.lePass = QLineEdit(self.formLayoutWidget)
        self.lePass.setObjectName(u"lePass")
        self.lePass.setStyleSheet(u"color: black;")
        self.lePass.setMaxLength(24)
        self.lePass.setEchoMode(QLineEdit.EchoMode.Normal)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lePass)

        self.btnLogin = QPushButton(self.formLayoutWidget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet(u"color: black;")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.btnLogin)

        self.lblMsg = QLabel(self.formLayoutWidget)
        self.lblMsg.setObjectName(u"lblMsg")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.lblMsg)

        self.lblLogIn = QLabel(Form)
        self.lblLogIn.setObjectName(u"lblLogIn")
        self.lblLogIn.setGeometry(QRect(200, 20, 101, 20))
        font1 = QFont()
        font1.setFamilies([u"Dubai"])
        font1.setPointSize(14)
        self.lblLogIn.setFont(font1)
        self.lblLogIn.setStyleSheet(u"color: black;")
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        self.btnLogin.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblUser.setText(QCoreApplication.translate("Form", u"Usuario:   ", None))
#if QT_CONFIG(tooltip)
        self.leUser.setToolTip(QCoreApplication.translate("Form", u"Introduce tu nombre de usuario", None))
#endif // QT_CONFIG(tooltip)
        self.leUser.setPlaceholderText(QCoreApplication.translate("Form", u"Usuario", None))
        self.lblContra.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a:  ", None))
#if QT_CONFIG(tooltip)
        self.lePass.setToolTip(QCoreApplication.translate("Form", u"Introduce tu contrase\u00f1a", None))
#endif // QT_CONFIG(tooltip)
        self.lePass.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.btnLogin.setText(QCoreApplication.translate("Form", u"Ingresar", None))
        self.lblMsg.setText("")
        self.lblLogIn.setText(QCoreApplication.translate("Form", u"Inicia Sesi\u00f3n", None))
    # retranslateUi

