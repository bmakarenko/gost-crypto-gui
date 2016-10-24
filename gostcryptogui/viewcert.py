# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewcert.ui'
#
# Created: Sat Oct 22 19:46:13 2016
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

class Ui_cert_view(object):
    def setupUi(self, cert_view):
        cert_view.setObjectName(_fromUtf8("cert_view"))
        cert_view.resize(404, 343)
        self.gridLayout = QtGui.QGridLayout(cert_view)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(323, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.close_cert_view = QtGui.QPushButton(cert_view)
        self.close_cert_view.setObjectName(_fromUtf8("close_cert_view"))
        self.gridLayout.addWidget(self.close_cert_view, 1, 1, 1, 1)
        self.cert_listview = QtGui.QListWidget(cert_view)
        self.cert_listview.setObjectName(_fromUtf8("cert_listview"))
        self.gridLayout.addWidget(self.cert_listview, 0, 0, 1, 2)

        self.retranslateUi(cert_view)
        QtCore.QObject.connect(self.close_cert_view, QtCore.SIGNAL(_fromUtf8("clicked()")), cert_view.close)
        QtCore.QMetaObject.connectSlotsByName(cert_view)

    def retranslateUi(self, cert_view):
        cert_view.setWindowTitle(_translate("cert_view", "Просмотр", None))
        self.close_cert_view.setText(_translate("cert_view", "Закрыть", None))

