#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
from gostcryptogui import gui
from PyQt4 import QtGui


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
    elif os.path.isfile(sys.argv[1]):
        if sys.argv[1][-4:] == '.enc':
            ex.decrypt(sys.argv[1].decode('utf-8'))
        elif sys.argv[1][-4:] == '.sig':
            ex.verify(True, sys.argv[1].decode('utf-8'))
    elif sys.argv[1] == '--help':
        print 'Использование: gost-crypto-gui.py [КЛЮЧ] [ФАЙЛ]'
        print 'Выполняет криптографические операции над файлами при помощи алгоритмов ГОСТ\n'
        print 'Ключи:\n'
        print '-sign\t\tПодписать файл'
        print '-encr\t\tЗашифровать файл'
        print '-verify\t\tПроверить электронную подпись файла'
        print '-dettach\tОтсоединить электронную подпись от файла'
        print '-decr\t\tРасшифровать файл'


if __name__ == '__main__':
    main()
