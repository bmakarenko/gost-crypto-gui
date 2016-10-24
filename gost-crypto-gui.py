#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from gostcryptogui import *
from PyQt4 import QtCore, QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    ex = gui.Window()
    ex.readConfig()
    if len(sys.argv) == 1:
        ex.show()
        sys.exit(app.exec_())
    elif sys.argv[1] == '-sign':
        ex.sign(sys.argv[2].decode('utf-8'))
    elif sys.argv[1] == '-encr':
        ex.encrypt(sys.argv[2].decode('utf-8'))
    elif sys.argv[1] == '-verify':
        ex.verify(False, sys.argv[2].decode('utf-8'))
    elif sys.argv[1] == '-dettach':
        ex.verify(True, sys.argv[2].decode('utf-8'))
    elif sys.argv[1] == '-decr':
        ex.decrypt(sys.argv[2].decode('utf-8'))


if __name__ == '__main__':
    main()

