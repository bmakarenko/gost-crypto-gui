# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectcert.ui'
#
# Created: Sat Oct 22 17:37:08 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_CertForm(object):
    def setupUi(self, CertForm):
        CertForm.setObjectName(_fromUtf8("CertForm"))
        CertForm.resize(511, 237)
        self.gridLayout = QtGui.QGridLayout(CertForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cancelButton = QtGui.QPushButton(CertForm)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout.addWidget(self.cancelButton, 2, 2, 1, 1)
        self.listView = QtGui.QListView(CertForm)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 4)
        self.okButton = QtGui.QPushButton(CertForm)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.gridLayout.addWidget(self.okButton, 2, 3, 1, 1)
        self.label = QtGui.QLabel(CertForm)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)

        self.retranslateUi(CertForm)
        QtCore.QMetaObject.connectSlotsByName(CertForm)

    def retranslateUi(self, CertForm):
        CertForm.setWindowTitle(_translate("CertForm", "Выбор сертификата", None))
        self.cancelButton.setText(_translate("CertForm", "Отмена", None))
        self.okButton.setText(_translate("CertForm", "Далее", None))
        self.label.setText(_translate("CertForm", "Выберите сертификат", None))

