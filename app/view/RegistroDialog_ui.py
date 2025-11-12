# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegistroDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_RegistroDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(498, 300)
        Dialog.setStyleSheet(u"background-color: #f5f5dc;\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 10, 101, 21))
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: black\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 50, 421, 211))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblUser = QLabel(self.formLayoutWidget)
        self.lblUser.setObjectName(u"lblUser")
        font1 = QFont()
        font1.setFamilies([u"Dubai"])
        font1.setPointSize(12)
        self.lblUser.setFont(font1)
        self.lblUser.setStyleSheet(u"color:clack")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblUser)

        self.leUs = QLineEdit(self.formLayoutWidget)
        self.leUs.setObjectName(u"leUs")
        self.leUs.setStyleSheet(u"color: black")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leUs)

        self.lblPwd = QLabel(self.formLayoutWidget)
        self.lblPwd.setObjectName(u"lblPwd")
        self.lblPwd.setFont(font1)
        self.lblPwd.setStyleSheet(u"color:black")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblPwd)

        self.lePwd = QLineEdit(self.formLayoutWidget)
        self.lePwd.setObjectName(u"lePwd")
        self.lePwd.setStyleSheet(u"color: black")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lePwd)

        self.btnAcep = QPushButton(self.formLayoutWidget)
        self.btnAcep.setObjectName(u"btnAcep")
        self.btnAcep.setFont(font1)
        self.btnAcep.setStyleSheet(u"color:black;")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.btnAcep)

        self.pushButton_2 = QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"color: black")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.pushButton_2)

        self.lblMsg = QLabel(self.formLayoutWidget)
        self.lblMsg.setObjectName(u"lblMsg")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.lblMsg)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Registrate!", None))
        self.lblUser.setText(QCoreApplication.translate("Dialog", u"Usuario: ", None))
        self.lblPwd.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a: ", None))
        self.btnAcep.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.lblMsg.setText("")
    # retranslateUi

