#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2017 Борис Макаренко

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

Copyright (c) 2017 Boris Makarenko

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

from datetime import datetime

from mainwindow import *
from cprocsp import *
from selectcert import *
from viewcert import *


class ViewCert(QtGui.QDialog):
    def __init__(self):
        super(ViewCert, self).__init__()
        self.ui = Ui_cert_view()
        self.ui.setupUi(self)


class HTMLDelegate(QtGui.QStyledItemDelegate):

    def paint(self, painter, option, index):
        if option.state & QtGui.QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())
        model = index.model()
        record = model.stringList()[index.row()]
        doc = QtGui.QTextDocument(self)

        doc.setHtml(record)
        doc.setMetaInformation(QtGui.QTextDocument.DocumentUrl, "file:///usr/share/")
        doc.setTextWidth(option.rect.width())
        ctx = QtGui.QAbstractTextDocumentLayout.PaintContext()

        painter.save()
        painter.translate(option.rect.topLeft())
        painter.setClipRect(option.rect.translated(-option.rect.topLeft()))
        dl = doc.documentLayout()
        dl.draw(painter, ctx)
        painter.restore()

    def sizeHint(self, option, index):
        model = index.model()
        record = model.stringList()[index.row()]
        doc = QtGui.QTextDocument(self)
        doc.setHtml(record)
        doc.setTextWidth(option.rect.width())
        return QtCore.QSize(doc.idealWidth(), doc.size().height())

# TODO Показывать алгоритмы подписи и открытого ключа
class ChooseCert(QtGui.QDialog):
    cert = str
    certs_hashes = dict

    def __init__(self, withsecret=bool):
        super(ChooseCert, self).__init__()
        self.ui = Ui_CertForm()
        self.ui.setupUi(self)
        self.certs_hashes = []
        model = QtGui.QStringListModel()
        cert_list = QtCore.QStringList()
        # Получаем сертификаты из личного хранилища
        certs_data = CryptoPro().get_store_certs(store='uMy')

        if not withsecret:
            cert_list.append(u'<i>Из файла...</i>')
        for line in certs_data:
            cert_html = u'<img src="icons/emblem-verified.png" width=22 height=22><b>%s</b> <br>Выдан:%s <br>' \
                        u'Серийный номер: %s<br>Хэш SHA1: %s<br>' % (line['subjectCN'], line['issuerCN'], line['serial'], line['thumbprint'])
            if datetime.strptime(line['notValidBefore'], '%d/%m/%Y  %H:%M:%S ') > datetime.utcnow():
                cert_html += u'Не действителен до: <font color=red><b>%s</b></font><br>' % line['notValidBefore']
                cert_html = cert_html.replace(u'emblem-verified.png', u'emblem-unverified.png')
            else:
                cert_html += u'Не действителен до: %s<br>' % line['notValidBefore']
            if datetime.strptime(line['notValidAfter'], '%d/%m/%Y  %H:%M:%S ') < datetime.utcnow():
                cert_html += u'Не действителен после: <font color=red><b>%s</b></font>' % line['notValidAfter']
                cert_html = cert_html.replace(u'emblem-verified.png', u'emblem-unverified.png')
            else:
                cert_html += u'Не действителен после: %s' % line['notValidAfter']
            if withsecret:
                if line['secretKey'] == 'Yes':
                    cert_list.append(cert_html)
                    self.certs_hashes.append(line)
            else:
                cert_list.append(cert_html)
                self.certs_hashes.append(line)
        model.setStringList(cert_list)
        self.ui.listView.setModel(model)
        self.ui.listView.setItemDelegate(HTMLDelegate(self))
        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.okButton.setEnabled(False)
        self.ui.okButton.clicked.connect(self.accept)
        if withsecret:
            self.ui.listView.clicked.connect(self.select_cert_w_secret)
        else:
            self.ui.listView.clicked.connect(self.select_cert)
        self.show()

    def select_cert(self, index):
        if index.row() == 0:
            self.cert = 'file'
        else:
            self.cert = self.certs_hashes[index.row()-1]
        self.ui.okButton.setEnabled(bool(self.cert))

    def select_cert_w_secret(self, index):
        self.cert = self.certs_hashes[index.row()]
        self.ui.okButton.setEnabled(bool(self.cert))

    def getCertificate(self):
        return self.cert


class ResultDialog(QtGui.QDialog):

    filename = str
    result = str
    dettached = False

    def __init__(self, filename, result, message, parent=None, dettached=False):
        super(ResultDialog, self).__init__(parent)
        self.filename, self.result, self.dettached = filename, result, dettached
        msgBox = QtGui.QMessageBox()
        closeButton = QtGui.QPushButton(u'Закрыть')
        sendButton = QtGui.QPushButton(u'Отправить по почте')
        showButton = QtGui.QPushButton(u'Показать в папке')
        msgBox.setText(message)
        msgBox.addButton(closeButton, QtGui.QMessageBox.NoRole)
        msgBox.addButton(sendButton, QtGui.QMessageBox.NoRole)
        msgBox.addButton(showButton, QtGui.QMessageBox.NoRole)
        msgBox.setDefaultButton(closeButton)
        self.connect(sendButton, QtCore.SIGNAL('clicked()'), self.send)
        self.connect(showButton, QtCore.SIGNAL('clicked()'), self.showFile)
        ret = msgBox.exec_()

    # Если создавалась отсоединенная подпись, отправить и оригинал
    def send(self):
        if self.dettached:
            subprocess.Popen(['xdg-email', '--attach', self.result, '--attach', self.filename])
        else:
            subprocess.Popen(['xdg-email', '--attach', self.result])

    def showFile(self):
        subprocess.Popen(['xdg-open', '/'.join(self.result.split('/')[:-1])])


class Window(QtGui.QMainWindow):
    provider = str
    encoding = str
    signcheck = bool
    dettached = bool

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        aboutAction = QtGui.QAction(u'&О программе', self)
        aboutAction.setShortcut('Ctrl+Q')
        self.ui.menubar.addAction(aboutAction)
        encodingActionGroup = QtGui.QActionGroup(self)
        self.ui.actionBase64.setActionGroup(encodingActionGroup)
        self.ui.actionDER.setActionGroup(encodingActionGroup)
        providerActionGroup = QtGui.QActionGroup(self)
        self.ui.action_CSP.setActionGroup(providerActionGroup)
        self.ui.actionOpenSSL.setActionGroup(providerActionGroup)
        signcheckActionGroup = QtGui.QActionGroup(self)
        self.ui.actionSignCheckOn.setActionGroup(signcheckActionGroup)
        self.ui.actionSignCheckOff.setActionGroup(signcheckActionGroup)
        dettachedActionGroup = QtGui.QActionGroup(self)
        self.ui.actionDettachedOn.setActionGroup(dettachedActionGroup)
        self.ui.actionDettachedOff.setActionGroup(dettachedActionGroup)
        self.connect(aboutAction, QtCore.SIGNAL('triggered()'), self.aboutProgram)
        self.connect(self.ui.actionDER, QtCore.SIGNAL('triggered()'), self.setOptions)
        self.connect(self.ui.actionBase64, QtCore.SIGNAL('triggered()'), self.setOptions)
        self.connect(self.ui.action_CSP, QtCore.SIGNAL('triggered()'), self.setOptions)
        self.connect(self.ui.actionOpenSSL, QtCore.SIGNAL('triggered()'), self.setOptions)
        self.connect(self.ui.actionSignCheckOn, QtCore.SIGNAL('triggered()'), self.setOptions)
        self.connect(self.ui.actionSignCheckOff, QtCore.SIGNAL('triggered()'), self.setOptions)
        self.connect(self.ui.actionDettachedOn, QtCore.SIGNAL('triggered()'), self.setOptions)
        self.connect(self.ui.actionDettachedOff, QtCore.SIGNAL('triggered()'), self.setOptions)
        self.connect(self.ui.btnSign, QtCore.SIGNAL('clicked()'), self.sign)
        self.connect(self.ui.btnVerify, QtCore.SIGNAL('clicked()'), self.verify)
        self.connect(self.ui.btnEncrypt, QtCore.SIGNAL('clicked()'), self.encrypt)
        self.connect(self.ui.btnDecrypt, QtCore.SIGNAL('clicked()'), self.decrypt)
        self.readConfig()
        try:
            CryptoPro()
        except Exception as error:
            QtGui.QMessageBox().warning(self, u"Cообщение", u"Произошла ошибка:\n%s" % error)


    def writeConfig(self):
        config = ConfigParser.RawConfigParser()
        config.add_section('gost-crypto-gui')
        config.set('gost-crypto-gui', 'provider', self.provider)
        config.set('gost-crypto-gui', 'encoding', self.encoding)
        config.set('gost-crypto-gui', 'signcheck', 'True' if self.signcheck else 'False')
        config.set('gost-crypto-gui', 'dettached', 'True' if self.dettached else 'False')
        if not os.path.exists(os.path.expanduser('~/.gost-crypto-gui/config.cfg')):
            try:
                os.makedirs(os.path.expanduser('~/.gost-crypto-gui/'))
            except OSError:
                pass
            config.set('gost-crypto-gui', 'provider', 'cprocsp')
            config.set('gost-crypto-gui', 'encoding', 'der')
            config.set('gost-crypto-gui', 'signcheck', 'True')
            config.set('gost-crypto-gui', 'dettached', 'False')
        with open(os.path.expanduser('~/.gost-crypto-gui/config.cfg'), 'wb') as configfile:
            config.write(configfile)

    def readConfig(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read(os.path.expanduser('~/.gost-crypto-gui/config.cfg'))
            self.provider = config.get('gost-crypto-gui', 'provider')
            self.encoding = config.get('gost-crypto-gui', 'encoding')
            self.signcheck = config.getboolean('gost-crypto-gui', 'signcheck')
            self.dettached = config.getboolean('gost-crypto-gui', 'dettached')
        except ConfigParser.NoSectionError:
            return
        except ConfigParser.NoOptionError:
            return
        except ConfigParser.MissingSectionHeaderError:
            return
        self.ui.action_CSP.setChecked(self.provider == 'cprocsp')
        self.ui.actionOpenSSL.setChecked(self.provider == 'openssl')
        self.ui.actionBase64.setChecked(self.encoding == 'base64')
        self.ui.actionDER.setChecked(self.encoding == 'der')
        self.ui.actionSignCheckOn.setChecked(True if self.signcheck else False)
        self.ui.actionSignCheckOff.setChecked(False if self.signcheck else True)
        self.ui.actionDettachedOn.setChecked(True if self.dettached else False)
        self.ui.actionDettachedOff.setChecked(False if self.dettached else True)

    def setOptions(self):
        if self.ui.actionDER.isChecked():
            self.encoding = 'der'
        elif self.ui.actionBase64.isChecked():
            self.encoding = 'base64'
        if self.ui.action_CSP.isChecked():
            self.provider = 'cprocsp'
        if self.ui.actionSignCheckOn.isChecked():
            self.signcheck = True
        elif self.ui.actionSignCheckOff.isChecked():
            self.signcheck = False
        if self.ui.actionDettachedOn.isChecked():
            self.dettached = True
        elif self.ui.actionDettachedOff.isChecked():
            self.dettached = False
        self.writeConfig()

    def sign(self, *args):
        if self.sender():
            file_names = QtGui.QFileDialog().getOpenFileNames(self, u"Выберите файл(ы)", "", "")
            if not file_names:
                return
        else:
            file_names = args
        try:
            choose = ChooseCert(True)
        except Exception as error:
            QtGui.QMessageBox().warning(self, u"Cообщение", u"Произошла ошибка:\n%s" % error)
            return
        if choose.exec_():
            cert_info = choose.getCertificate()
        else:
            return
        progressDialog = QtGui.QProgressDialog("", u"Отмена", 0, 0, self)
        progressDialog.setValue(-1)
        for index, filename in enumerate(file_names, start=1):
            progressDialog.setLabelText(u'Подпись файла %s из %s<br>Текущий файл: %s' % (index, len(file_names),
                                                                                         filename.split('/')[-1]))
            progressDialog.show()
            if progressDialog.wasCanceled():
                return
            try:
                result = CryptoPro().sign(cert_info['thumbprint'], unicode(filename), self.encoding, self.dettached)
                message = ''
                if result[0]:
                    message = u"Файл %s успешно подписан.\n\nПодписанный файл: %s\n\n" % \
                              (unicode(filename), unicode(filename + '.sig'))
                    message += u'Сертификат:\n{p[subjectCN]}\nВыдан: {p[issuerCN]}\nСерийный номер: {p[serial]}\nНе действителен до: {p[notValidBefore]}\nНе действителен после: {p[notValidAfter]}\n\n'.format(p=cert_info)
                if result[1]:
                    message += u"\n\nПредупреждение: %s" % result[1]
                progressDialog.hide()
                ResultDialog(unicode(filename), unicode(filename + '.sig'),
                             message, dettached=self.dettached).show()
            except Exception as error:
                QtGui.QMessageBox().warning(self, u"Cообщение", u"Произошла ошибка:\n%s" % error)
        progressDialog.close()

    def verify(self, dettach=False, *args):

        def add_line(text=None):
            item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
            if text:
                label = QtGui.QLabel()
                label.setText(text)
                cert_view.ui.cert_listview.setItemWidget(item, label)

        if self.sender():
            file_names = QtGui.QFileDialog().getOpenFileNames(self, u"Выберите файл(ы)", "", "*.sig")
            if not file_names:
                return
        else:
            file_names = args
        progressDialog = QtGui.QProgressDialog("", u"Отмена", 0, 0, self)
        progressDialog.setValue(-1)
        progressDialog.show()
        for index, filename in enumerate(file_names, start=1):
            progressDialog.setLabelText(u'Проверка подписи файла %s из %s<br>Текущий файл: %s' % (index, len(file_names),
                                                                                         filename.split('/')[-1]))
            if progressDialog.wasCanceled():
                return
            try:
                cert_info, chain, revoked, expired = CryptoPro().verify(unicode(filename), dettach)
                cert_info = list(cert_info)[0]
                cert_view = ViewCert()
                add_line(u'Файл: %s' % unicode(filename))
                add_line(u'<b>Информация о сертификате подписи:</b>:')
                add_line(u'<b>Эмитент</b>:')
                for field, value in cert_info['issuerDN'].items():
                    add_line('<b>%s</b>: %s' % (self.translate_cert_fields(field), value))
                add_line()
                add_line(u'<b>Субъект</b>:')
                for field, value in cert_info['subjectDN'].items():
                    add_line('<b>%s</b>: %s' % (self.translate_cert_fields(field), value))
                add_line()
                add_line(u'<b>Серийный номер</b>: %s' % cert_info['serial'])
                not_valid_before = datetime.strptime(cert_info['notValidBefore'], '%d/%m/%Y  %H:%M:%S ')
                add_line(u'<b>Не действителен до</b>: %s' % datetime.strftime(not_valid_before, '%d.%m.%Y %H:%M:%S'))
                not_valid_after = datetime.strptime(cert_info['notValidAfter'], '%d/%m/%Y  %H:%M:%S ')
                add_line(u'<b>Не действителен после</b>: %s' % datetime.strftime(not_valid_after, '%d.%m.%Y %H:%M:%S'))
                add_line()
                if chain:
                    add_line(u'<font color="green"><b>Цепочка сертификатов была проверена.</b></font>')
                else:
                    add_line(u'<font color="orange"><b>ВНИМАНИЕ: Цепочка сертификатов не была проверена.</b></font>')
                if revoked:
                    add_line(u'<font color="red"><b>ВНИМАНИЕ: Один или несколько сертификатов в цепочке отозваны!</b></font>')
                elif expired:
                    add_line(u'<font color="red"><b>ВНИМАНИЕ: Срок действия сертификата истек или еще не наступил!</b></font>')
                elif chain:
                    add_line(u'<font color="green"><b>Сертификат действителен.</b></font>')
                cert_view.exec_()
            except Exception as error:
                QtGui.QMessageBox().warning(self, u"Cообщение", u"Произошла ошибка:\n%s" % error)
        progressDialog.close()

    def encrypt(self, *args):
        if self.sender():
            file_names = QtGui.QFileDialog().getOpenFileNames(self, u"Выберите файл(ы)", "", "")
            if not file_names:
                return
        else:
            file_names = args
        try:
            choose = ChooseCert(False)
        except Exception as error:
            QtGui.QMessageBox().warning(self, u"Cообщение", u"Произошла ошибка:\n%s" % error)
            return
        if choose.exec_():
            cert_info = choose.getCertificate()
            if cert_info == 'file':
                thumbprint = QtGui.QFileDialog().getOpenFileName(self, u"Выберите файл(ы)", "", "*.crt *cer")
                if not thumbprint:
                    return
                cert_info = list(CryptoPro().get_store_certs(crt_file=thumbprint))[0]
            else:
                thumbprint = cert_info['thumbprint']
        else:
            return
        progressDialog = QtGui.QProgressDialog("", u"Отмена", 0, 0, self)
        progressDialog.setValue(-1)
        for index, filename in enumerate(file_names, start=1):
            progressDialog.setLabelText(u'Шифрование файла %s из %s<br>Текущий файл: %s' % (index, len(file_names),
                                                                                         filename.split('/')[-1]))
            progressDialog.show()
            if progressDialog.wasCanceled():
                return
            try:
                encrypted, chain, revoked, expired = CryptoPro().encrypt(unicode(thumbprint), unicode(filename), self.encoding)
                if encrypted:
                    message = u'Файл %s успешно зашифрован.\n\nЗашифрованный файл: %s\n\n' % (unicode(filename), unicode(filename)+'.enc')
                    message += u'Сертификат:\n{p[subjectCN]}\nВыдан: {p[issuerCN]}\nСерийный номер: {p[serial]}\nНе действителен до: {p[notValidBefore]}\nНе действителен после: {p[notValidAfter]}\n\n'.format(p=cert_info)
                    if not chain:
                        message += u'ВНИМАНИЕ: Статус отзыва сертификата не был проверен!\n'
                    if revoked:
                        message += u'ВНИМАНИЕ: Один или несколько сертификатов в цепочке отозваны!\n'
                    if expired:
                        message += u'ВНИМАНИЕ: Срок действия сертификата истек или еще не наступил!\n'
                    progressDialog.hide()
                    ResultDialog(unicode(filename), unicode(filename)+'.enc', message).show()
                    #QtGui.QMessageBox().information(self, u"Cообщение", message)
            except Exception as error:
                QtGui.QMessageBox().warning(self, u"Cообщение", u"Произошла ошибка:\n%s" % error)
        progressDialog.close()

    def decrypt(self, *args):
        if self.sender():
            file_names = QtGui.QFileDialog().getOpenFileNames(self, u"Выберите файл(ы)", "", "*.enc *.encr")
            if not file_names:
                return
        else:
            file_names = args
        try:
            choose = ChooseCert(True)
        except Exception as error:
            QtGui.QMessageBox().warning(self, u"Cообщение", u"Произошла ошибка:\n%s" % error)
            return
        if choose.exec_():
            cert_info = choose.getCertificate()
        else:
            return
        progressDialog = QtGui.QProgressDialog("", u"Отмена", 0, 0, self)
        progressDialog.setValue(-1)
        for index, filename in enumerate(file_names, start=1):
            progressDialog.setLabelText(u'Расшифровка файла %s из %s<br>Текущий файл: %s' % (index, len(file_names),
                                                                                         filename.split('/')[-1]))
            progressDialog.show()
            if progressDialog.wasCanceled():
                return
            try:
                decrypted, chain, revoked, expired = CryptoPro().decrypt(cert_info['thumbprint'], unicode(filename))
                if decrypted:
                    message = u'Файл %s успешно расшифрован.\n\nРасшифрованный файл: %s\n\n' % (unicode(filename), unicode(filename)[:-4])
                    if not chain:
                        message += u'ВНИМАНИЕ: Статус отзыва сертификата не был проверен!\n'
                    if revoked:
                        message += u'ВНИМАНИЕ: Один или несколько сертификатов в цепочке отозваны!\n'
                    if expired:
                        message += u'ВНИМАНИЕ: Срок действия сертификата истек или еще не наступил!\n'
                    progressDialog.hide()
                    ResultDialog(unicode(filename), unicode(filename)[:-4], message).show()
            except Exception as error:
                QtGui.QMessageBox().warning(self, u"Cообщение", u"Произошла ошибка:\n%s" % error)
        progressDialog.close()

    def translate_cert_fields(self, fieldname):
        fields = {'1.2.840.113549.1.9.2': u'неструктурированное имя',
                  '1.2.643.5.1.5.2.1.2': u'код должности',
                  '1.2.643.5.1.5.2.1.1': u'код структурного подразделения ФССП России (ВКСП)',
                  '1.2.643.5.1.5.2.2.1': u'Полномочия публикации обновлений ПО',
                  '1.2.643.5.1.5.2.2.2': u'Подсистема АИС ФССП России',
                  '1.2.643.5.1.24.2.9': u'Главный судебный пристав Российской Федерации',
                  '1.2.643.5.1.24.2.10': u'Заместитель главного судебного пристава Российской Федерации',
                  '1.2.643.5.1.24.2.11': u'Главный судебный пристав субъекта Российской Федерации',
                  '1.2.643.5.1.24.2.12': u'Заместитель главного судебного пристава субъекта Российской Федерации',
                  '1.2.643.5.1.24.2.13': u'Старший судебный пристав',
                  '1.2.643.5.1.24.2.14': u'Судебный пристав-исполнитель',
                  '1.2.643.100.2.1': u'Доступ к СМЭВ (ФЛ)',
                  '1.2.643.100.2.2': u'Доступ к СМЭВ (ЮЛ)',
                  '1.2.643.2.2.34.2': u'Временный доступ к Центру Регистрации',
                  '1.2.643.2.2.34.4': u'Администратор Центра Регистрации КриптоПро УЦ',
                  '1.2.643.2.2.34.5': u'Оператор Центра Регистрации КриптоПро УЦ',
                  '1.2.643.2.2.34.6': u'Пользователь центра регистрации КриптоПро УЦ',
                  '1.2.643.2.2.34.7': u'Центр Регистрации КриптоПро УЦ',
                  '1.3.6.1.5.5.7.3.1': u'Проверка подлинности сервера',
                  '1.3.6.1.5.5.7.3.2': u'Проверка подлинности клиента',
                  '1.3.6.1.5.5.7.3.4': u'Защищенная электронная почта',
                  '1.3.6.1.5.5.7.3.8': u'Установка штампа времени',
                  '1.2.643.3.61.502710.1.6.3.4.1.1': u'Администратор организации',
                  '1.2.643.3.61.502710.1.6.3.4.1.2': u'Уполномоченный специалист',
                  '1.2.643.3.61.502710.1.6.3.4.1.3': u'Должностное лицо с правом подписи контракта',
                  '1.2.643.3.61.502710.1.6.3.4.1.4': u'Специалист с правом направления проекта контракта участнику размещения заказа',
                  'CN': u'общее имя',
                  'SN': u'фамилия',
                  'G': u'имя и отчество',
                  'I': u'инициалы',
                  'T': u'должность',
                  'OU': u'структурное подразделение',
                  'O': u'организация',
                  'L': u'населенный пункт',
                  'S': u'субъект РФ',
                  'C': u'страна',
                  'E': u'адрес электронной почты',
                  'INN': u'ИНН',
                  'OGRN': u'ОГРН',
                  'SNILS': u'СНИЛС',
                  'STREET': u'название улицы, номер дома',
                  'StreetAddress': u'адрес места нахождения',
                  'Unstructured Name': u'неструктурированное имя'}
        try:
            return fields[fieldname]
        except KeyError:
            return fieldname

    def aboutProgram(self):
        QtGui.QMessageBox().about(self, u"О программе",
                                  u"<b>gost-crypto-gui 0.3</b><br>"
                                  u"<br>2017г. Борис Макаренко<br>УИТ ФССП России"
                                  u"<br>E-mail: <a href='mailto:makarenko@fssprus.ru'>makarenko@fssprus.ru</a>"
                                  u"<br> <a href='mailto:bmakarenko90@gmail.com'>bmakarenko90@gmail.com</a><br><br>"
                                  u"<a href='http://opensource.org/licenses/MIT'>Лицензия MIT</a>")
