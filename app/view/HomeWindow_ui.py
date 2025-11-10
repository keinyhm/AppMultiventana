# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 583)
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #f5f5dc;\n"
"")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionConfiguracion = QAction(MainWindow)
        self.actionConfiguracion.setObjectName(u"actionConfiguracion")
        self.actionNotas = QAction(MainWindow)
        self.actionNotas.setObjectName(u"actionNotas")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblWelcome = QLabel(self.centralwidget)
        self.lblWelcome.setObjectName(u"lblWelcome")
        self.lblWelcome.setGeometry(QRect(300, 10, 191, 51))
        font1 = QFont()
        font1.setFamilies([u"Dubai"])
        font1.setPointSize(18)
        self.lblWelcome.setFont(font1)
        self.lblWelcome.setStyleSheet(u"color: black;\n"
"\n"
"")
        self.lblWelcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 793, 33))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"    background-color: #ececec;\n"
"}\n"
"QMenuBar::item {\n"
"    color: black;\n"
"}\n"
"QMenuBar::item:selected {\n"
"    background-color: #dcdcdc;\n"
"}\n"
"QMenu {\n"
"    color: black;\n"
"    background-color: #f5f5f5;\n"
"}\n"
"QMenu::item:selected {\n"
"    background-color: #dcdcdc;\n"
"}\n"
"\n"
"")
        self.menuSalir = QMenu(self.menubar)
        self.menuSalir.setObjectName(u"menuSalir")
        self.menuSalir.setStyleSheet(u"color: black;\n"
"\n"
"\n"
"")
        self.menuEdicion = QMenu(self.menubar)
        self.menuEdicion.setObjectName(u"menuEdicion")
        self.menuEdicion.setStyleSheet(u"color: black;\n"
"")
        self.menuVentanas = QMenu(self.menubar)
        self.menuVentanas.setObjectName(u"menuVentanas")
        self.menuVentanas.setStyleSheet(u"color: black;\n"
"\n"
"")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"color: black;\n"
"")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSalir.menuAction())
        self.menubar.addAction(self.menuEdicion.menuAction())
        self.menubar.addAction(self.menuVentanas.menuAction())
        self.menuSalir.addAction(self.actionSalir)
        self.menuEdicion.addAction(self.actionConfiguracion)
        self.menuVentanas.addAction(self.actionNotas)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(statustip)
        self.actionSalir.setStatusTip(QCoreApplication.translate("MainWindow", u"Salir de la aplicaci\u00f3n", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionConfiguracion.setText(QCoreApplication.translate("MainWindow", u"Edici\u00f3n", None))
#if QT_CONFIG(statustip)
        self.actionConfiguracion.setStatusTip(QCoreApplication.translate("MainWindow", u"Abrir ventana de configuraci\u00f3n", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionConfiguracion.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionNotas.setText(QCoreApplication.translate("MainWindow", u"Notas", None))
#if QT_CONFIG(statustip)
        self.actionNotas.setStatusTip(QCoreApplication.translate("MainWindow", u"Abrir notas r\u00e1pidas", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionNotas.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.lblWelcome.setText(QCoreApplication.translate("MainWindow", u"Bienvenido!", None))
        self.menuSalir.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuEdicion.setTitle(QCoreApplication.translate("MainWindow", u"Edici\u00f3n", None))
        self.menuVentanas.setTitle(QCoreApplication.translate("MainWindow", u"Ventanas", None))
    # retranslateUi

