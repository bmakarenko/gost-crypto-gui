#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2016 Борис Макаренко

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

Copyright (c) 2016 Boris Makarenko

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
import nautilus
import urllib
import subprocess
import logging
import os


class VerifyMenuProvider(nautilus.MenuProvider):
    # Nautilus crashes if a plugin doesn't implement the __init__ method.
    # See Bug #374958
    def __init__(self):
        logging.basicConfig(filename='/tmp/verify-nautilus-debug', level=logging.DEBUG)

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

        itemVerify = nautilus.MenuItem('VerifyMenuProvider::Verify',
                                       'Проверить ЭЦП',
                                       'Проверить ЭЦП %s' % filename)

        itemVerify.connect("activate", self.menu_activate_cb, fileObj)
        return itemVerify,

    def menu_activate_cb(self, menu, fileObj):
        filename = urllib.unquote(fileObj.get_uri())[7:]
        subprocess.Popen(['python', '/usr/bin/gost-crypto-gui.py', '-verify', filename])


class DettachMenuProvider(nautilus.MenuProvider):
    # Nautilus crashes if a plugin doesn't implement the __init__ method.
    # See Bug #374958
    def __init__(self):
        logging.basicConfig(filename='/tmp/dettach-nautilus-debug', level=logging.DEBUG)

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

        itemVerify = nautilus.MenuItem('VerifyMenuProvider::Verify',
                                       'Отсоединить подпись',
                                       'Отсоединить подпись %s' % filename)

        itemVerify.connect("activate", self.menu_activate_cb, fileObj)
        return itemVerify,

    def menu_activate_cb(self, menu, fileObj):
        filename = urllib.unquote(fileObj.get_uri())[7:]
        subprocess.Popen(['python', '/usr/bin/gost-crypto-gui.py', '-dettach', filename])


class DecryptMenuProvider(nautilus.MenuProvider):
    # Nautilus crashes if a plugin doesn't implement the __init__ method.
    # See Bug #374958
    def __init__(self):
        logging.basicConfig(filename='/tmp/decrypt-nautilus-debug', level=logging.DEBUG)

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

        itemDecrypt = nautilus.MenuItem('DecryptMenuProvider::Decrypt',
                                        'Расшифровать',
                                        'Расшифровать файл %s' % filename)

        itemDecrypt.connect("activate", self.menu_activate_cb, fileObj)
        return itemDecrypt,

    def menu_activate_cb(self, menu, fileObj):
        filename = urllib.unquote(fileObj.get_uri())[7:]
        subprocess.Popen(['python', '/usr/bin/gost-crypto-gui.py', '-decr', filename])


class SignMenuProvider(nautilus.MenuProvider):
    # Nautilus crashes if a plugin doesn't implement the __init__ method.
    # See Bug #374958
    def __init__(self):
        logging.basicConfig(filename='/tmp/sign-nautilus-debug', level=logging.DEBUG)

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        fileObj = files[0]
        if fileObj.get_uri_scheme() != 'file':
            return
        if fileObj.is_directory():
            return
        filename = urllib.unquote(fileObj.get_uri())[7:]

        itemSign = nautilus.MenuItem('SignMenuProvider::Encrypt',
                                     'Подписать',
                                     'Подписать файл %s' % filename)

        itemSign.connect("activate", self.menu_activate_cb, fileObj)
        return itemSign,

    def menu_activate_cb(self, menu, fileObj):
        filename = urllib.unquote(fileObj.get_uri())[7:]
        subprocess.Popen(['python', '/usr/bin/gost-crypto-gui.py', '-sign', filename])


class EncryptMenuProvider(nautilus.MenuProvider):
    # Nautilus crashes if a plugin doesn't implement the __init__ method.
    # See Bug #374958
    def __init__(self):
        logging.basicConfig(filename='/tmp/encrypt-nautilus-debug', level=logging.DEBUG)

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        fileObj = files[0]
        if fileObj.get_uri_scheme() != 'file':
            return
        if fileObj.is_directory():
            return
        filename = urllib.unquote(fileObj.get_uri())[7:]

        itemEncrypt = nautilus.MenuItem('EncryptMenuProvider::Encrypt',
                                        'Зашифровать',
                                        'Зашифровать файл %s' % filename)

        itemEncrypt.connect("activate", self.menu_activate_cb, fileObj)
        return itemEncrypt,

    def menu_activate_cb(self, menu, fileObj):
        filename = urllib.unquote(fileObj.get_uri())[7:]
        subprocess.Popen(['python', '/usr/bin/gost-crypto-gui.py', '-encr', filename])
