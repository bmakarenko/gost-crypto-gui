#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2019 Борис Макаренко

Данная лицензия разрешает лицам, получившим копию данного программного
обеспечения и сопутствующей документации (в дальнейшем именуемыми «Программное
Обеспечение»), безвозмездно использовать Программное Обеспечение без
ограничений, включая неограниченное право на использование, копирование,
изменение, добавление, публикацию, распространение, сублицензирование и/или
продажу копий Программного Обеспечения, а также лицам, которым предоставляется
данное Программное Обеспечение, при соблюдении следующих условий:

Указанное выше уведомление об авторском праве и данные условия должны быть
включены во все копии или значимые части данного Программного Обеспечения.

ДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО
ГАРАНТИЙ, ЯВНО ВЫРАЖЕННЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ ГАРАНТИИ ТОВАРНОЙ
ПРИГОДНОСТИ, СООТВЕТСТВИЯ ПО ЕГО КОНКРЕТНОМУ НАЗНАЧЕНИЮ И ОТСУТСТВИЯ НАРУШЕНИЙ,
НО НЕ ОГРАНИЧИВАЯСЬ ИМИ. НИ В КАКОМ СЛУЧАЕ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ
ОТВЕТСТВЕННОСТИ ПО КАКИМ-ЛИБО ИСКАМ, ЗА УЩЕРБ ИЛИ ПО ИНЫМ ТРЕБОВАНИЯМ, В ТОМ
ЧИСЛЕ, ПРИ ДЕЙСТВИИ КОНТРАКТА, ДЕЛИКТЕ ИЛИ ИНОЙ СИТУАЦИИ, ВОЗНИКШИМ ИЗ-ЗА
ИСПОЛЬЗОВАНИЯ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ ИЛИ ИНЫХ ДЕЙСТВИЙ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ..

Copyright (c) 2019 Boris Makarenko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from gi.repository import Caja, GObject
import urllib
import subprocess
import os


class VerifyMenuProvider(GObject.GObject, Caja.MenuProvider):

    def __init__(self):
        pass

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        fileObj = files[0]
        if fileObj.get_uri_scheme() != 'file':
            return
        if fileObj.is_directory():
            return
        filename = urllib.unquote(fileObj.get_uri())[7:]
        if filename[-3:] != 'sig':
            return
        if os.path.isfile(filename[:-4]):
            return

        itemVerify = Caja.MenuItem(name='VerifyMenuProvider::Verify',
                                       label='Проверить ЭЦП',
                                       tip='Проверить ЭЦП %s' % filename)

        itemVerify.connect("activate", self.menu_activate_cb, fileObj)
        return itemVerify,

    def menu_activate_cb(self, menu, fileObj):
        filename = urllib.unquote(fileObj.get_uri())[7:]
        subprocess.Popen(['python', '/usr/bin/gost-crypto-gui.py', '-verify', filename])


class DettachMenuProvider(GObject.GObject, Caja.MenuProvider):

    def __init__(self):
        pass

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        fileObj = files[0]
        if fileObj.get_uri_scheme() != 'file':
            return
        if fileObj.is_directory():
            return
        filename = urllib.unquote(fileObj.get_uri())[7:]
        if filename[-3:] != 'sig':
            return

        itemVerify = Caja.MenuItem(name='DettachMenuProvider::Dettach',
                                       label='Отсоединить подпись',
                                       tip='Отсоединить подпись %s' % filename)

        itemVerify.connect("activate", self.menu_activate_cb, fileObj)
        return itemVerify,

    def menu_activate_cb(self, menu, fileObj):
        filename = urllib.unquote(fileObj.get_uri())[7:]
        subprocess.Popen(['python', '/usr/bin/gost-crypto-gui.py', '-dettach', filename])


class DecryptMenuProvider(GObject.GObject, Caja.MenuProvider):

    def __init__(self):
        pass

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        fileObj = files[0]
        if fileObj.get_uri_scheme() != 'file':
            return
        if fileObj.is_directory():
            return
        filename = urllib.unquote(fileObj.get_uri())[7:]
        if filename[-3:] != 'enc':
            return

        itemDecrypt = Caja.MenuItem(name='DecryptMenuProvider::Decrypt',
                                        label='Расшифровать',
                                        tip='Расшифровать файл %s' % filename)

        itemDecrypt.connect("activate", self.menu_activate_cb, fileObj)
        return itemDecrypt,

    def menu_activate_cb(self, menu, fileObj):
        filename = urllib.unquote(fileObj.get_uri())[7:]
        subprocess.Popen(['python', '/usr/bin/gost-crypto-gui.py', '-decr', filename])


class SignMenuProvider(GObject.GObject, Caja.MenuProvider):

    def __init__(self):
        pass

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        fileObj = files[0]
        if fileObj.get_uri_scheme() != 'file':
            return
        if fileObj.is_directory():
            return
        filename = urllib.unquote(fileObj.get_uri())[7:]

        itemSign = Caja.MenuItem(name='SignMenuProvider::Encrypt',
                                     label='Подписать',
                                     tip='Подписать файл %s' % filename)

        itemSign.connect("activate", self.menu_activate_cb, fileObj)
        return itemSign,

    def menu_activate_cb(self, menu, fileObj):
        filename = urllib.unquote(fileObj.get_uri())[7:]
        subprocess.Popen(['python', '/usr/bin/gost-crypto-gui.py', '-sign', filename])


class EncryptMenuProvider(GObject.GObject, Caja.MenuProvider):

    def __init__(self):
        pass

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        fileObj = files[0]
        if fileObj.get_uri_scheme() != 'file':
            return
        if fileObj.is_directory():
            return
        filename = urllib.unquote(fileObj.get_uri())[7:]

        itemEncrypt = Caja.MenuItem(name='EncryptMenuProvider::Encrypt',
                                        label='Зашифровать',
                                        tip='Зашифровать файл %s' % filename)

        itemEncrypt.connect("activate", self.menu_activate_cb, fileObj)
        return itemEncrypt,

    def menu_activate_cb(self, menu, fileObj):
        filename = urllib.unquote(fileObj.get_uri())[7:]
        subprocess.Popen(['python', '/usr/bin/gost-crypto-gui.py', '-encr', filename])
