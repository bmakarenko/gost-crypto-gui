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
import ConfigParser
import os.path
import gostcryptogui
from gi.repository import Caja, GObject
import urllib


class SignatureCheckProvider(GObject.GObject, Caja.InfoProvider):
    def __init__(self):
        pass

    def readConfig(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read(os.path.expanduser('~/.gost-crypto-gui/config.cfg'))
            return config.getboolean('gost-crypto-gui', 'signcheck')
        except ConfigParser.NoSectionError:
            return True

    def update_file_info(self, file):
        if file.get_uri_scheme() != 'file':
            return
        if os.path.splitext(file.get_name())[1] == ".sig" and self.readConfig():
            filepath = urllib.unquote(file.get_uri())[7:]
            signer, chain, revoked, expired = gostcryptogui.cprocsp.CryptoPro().verify(unicode(filepath), False)
            if not chain:
                file.add_emblem("nochain")
            elif expired or revoked:
                file.add_emblem("unverified")
            else:
                file.add_emblem("verified")
