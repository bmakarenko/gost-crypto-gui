# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(265, 276)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/pixmaps/gost-crypto-gui.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnSign = QtGui.QPushButton(self.centralwidget)
        self.btnSign.setObjectName(_fromUtf8("btnSign"))
        self.verticalLayout.addWidget(self.btnSign)
        self.btnVerify = QtGui.QPushButton(self.centralwidget)
        self.btnVerify.setObjectName(_fromUtf8("btnVerify"))
        self.verticalLayout.addWidget(self.btnVerify)
        self.btnEncrypt = QtGui.QPushButton(self.centralwidget)
        self.btnEncrypt.setObjectName(_fromUtf8("btnEncrypt"))
        self.verticalLayout.addWidget(self.btnEncrypt)
        self.btnDecrypt = QtGui.QPushButton(self.centralwidget)
        self.btnDecrypt.setObjectName(_fromUtf8("btnDecrypt"))
        self.verticalLayout.addWidget(self.btnDecrypt)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 265, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.cryptoprovider = QtGui.QMenu(self.menu)
        self.cryptoprovider.setObjectName(_fromUtf8("cryptoprovider"))
        self.encoding = QtGui.QMenu(self.menu)
        self.encoding.setObjectName(_fromUtf8("encoding"))
        self.sign_check = QtGui.QMenu(self.menu)
        self.sign_check.setObjectName(_fromUtf8("sign_check"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_CSP = QtGui.QAction(MainWindow)
        self.action_CSP.setCheckable(True)
        self.action_CSP.setChecked(True)
        self.action_CSP.setObjectName(_fromUtf8("action_CSP"))
        self.actionOpenSSL = QtGui.QAction(MainWindow)
        self.actionOpenSSL.setCheckable(True)
        self.actionOpenSSL.setEnabled(False)
        self.actionOpenSSL.setObjectName(_fromUtf8("actionOpenSSL"))
        self.actionDER = QtGui.QAction(MainWindow)
        self.actionDER.setCheckable(True)
        self.actionDER.setChecked(True)
        self.actionDER.setObjectName(_fromUtf8("actionDER"))
        self.actionBase64 = QtGui.QAction(MainWindow)
        self.actionBase64.setCheckable(True)
        self.actionBase64.setObjectName(_fromUtf8("actionBase64"))
        self.actionSignCheckOn = QtGui.QAction(MainWindow)
        self.actionSignCheckOn.setCheckable(True)
        self.actionSignCheckOn.setChecked(True)
        self.actionSignCheckOn.setObjectName(_fromUtf8("actionSignCheckOn"))
        self.actionSignCheckOff = QtGui.QAction(MainWindow)
        self.actionSignCheckOff.setCheckable(True)
        self.actionSignCheckOff.setChecked(False)
        self.actionSignCheckOff.setObjectName(_fromUtf8("actionSignCheckOff"))
        self.cryptoprovider.addAction(self.action_CSP)
        self.cryptoprovider.addAction(self.actionOpenSSL)
        self.encoding.addAction(self.actionDER)
        self.encoding.addAction(self.actionBase64)
        self.sign_check.addAction(self.actionSignCheckOn)
        self.sign_check.addAction(self.actionSignCheckOff)
        self.menu.addAction(self.cryptoprovider.menuAction())
        self.menu.addAction(self.encoding.menuAction())
        self.menu.addAction(self.sign_check.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "gost-crypto-gui", None))
        self.btnSign.setStatusTip(_translate("MainWindow", "Подписать указанный файл", None))
        self.btnSign.setText(_translate("MainWindow", "Подписать файл(ы)", None))
        self.btnVerify.setStatusTip(_translate("MainWindow", "Проверить ЭЦП подписанного файла", None))
        self.btnVerify.setText(_translate("MainWindow", "Проверить подпись", None))
        self.btnEncrypt.setStatusTip(_translate("MainWindow", "Зашифровать указанный файл", None))
        self.btnEncrypt.setText(_translate("MainWindow", "Зашифровать файл(ы)", None))
        self.btnDecrypt.setStatusTip(_translate("MainWindow", "Расшифровать файл", None))
        self.btnDecrypt.setText(_translate("MainWindow", "Расшифровать файл(ы)", None))
        self.menu.setTitle(_translate("MainWindow", "Опции", None))
        self.cryptoprovider.setStatusTip(_translate("MainWindow", "Выбрать используемый криптопровайдер", None))
        self.cryptoprovider.setTitle(_translate("MainWindow", "Криптопровайдер", None))
        self.encoding.setTitle(_translate("MainWindow", "Кодировка файлов", None))
        self.sign_check.setTitle(_translate("MainWindow", "Авт. проверка подписи", None))
        self.action_CSP.setText(_translate("MainWindow", "КриптоПро CSP", None))
        self.actionOpenSSL.setText(_translate("MainWindow", "OpenSSL", None))
        self.actionDER.setText(_translate("MainWindow", "DER", None))
        self.actionBase64.setText(_translate("MainWindow", "base64", None))
        self.actionSignCheckOn.setText(_translate("MainWindow", "Включено", None))
        self.actionSignCheckOff.setText(_translate("MainWindow", "Выключено", None))

