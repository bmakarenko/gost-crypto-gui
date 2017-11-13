# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectcert.ui'
#
# Created: Mon Nov 13 12:04:45 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CertForm(object):
    def setupUi(self, CertForm):
        CertForm.setObjectName("CertForm")
        CertForm.resize(511, 237)
        self.gridLayout = QtGui.QGridLayout(CertForm)
        self.gridLayout.setObjectName("gridLayout")
        self.cancelButton = QtGui.QPushButton(CertForm)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 2, 1, 1)
        self.listView = QtGui.QListView(CertForm)
        self.listView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listView.setViewMode(QtGui.QListView.ListMode)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 4)
        self.okButton = QtGui.QPushButton(CertForm)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 2, 3, 1, 1)
        self.label = QtGui.QLabel(CertForm)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)

        self.retranslateUi(CertForm)
        QtCore.QMetaObject.connectSlotsByName(CertForm)

    def retranslateUi(self, CertForm):
        CertForm.setWindowTitle(QtGui.QApplication.translate("CertForm", "Выбор сертификата", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("CertForm", "Отмена", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("CertForm", "Далее", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CertForm", "Выберите сертификат", None, QtGui.QApplication.UnicodeUTF8))

