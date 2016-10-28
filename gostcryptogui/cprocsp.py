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
import os
import platform
import subprocess
import re


# Класс CryptoPro предназнаечен для выполнения криптографических операций над файлами средствами КриптоПро CSP


class CryptoPro:
    arch = str

    def __init__(self):
        if platform.machine() == 'x86_64':
            self.arch = 'amd64'
        elif platform.machine() == 'i686':
            self.arch = 'ia32'
        else:
            pass

    # Метод error_description принимает код ошибки и возвращает её описание. Если такой ошибки в словаре нет,
    # то код ошибки возвращается обратно
    @staticmethod
    def error_description(error):
        errors = {'0x20000064': u'Мало памяти',
                  '0x20000065': u'Не удалось открыть файл',
                  '0x20000066': u'Операция отменена пользователем',
                  '0x20000067': u'Некорректное преобразование BASE64',
                  '0x20000068': u'Если указан параметр -help, то других быть не должно',
                  '0x200000c8': u'Указан лишний файл',
                  '0x200000c9': u'Указан неизвестный ключ',
                  '0x200000ca': u'Указана лишняя команда',
                  '0x200000cb': u'Для ключа не указан параметр',
                  '0x200000cc': u'Не указана команда',
                  '0x200000cd': u'Не указан необходимый ключ',
                  '0x200000ce': u'Указан неверный ключ',
                  '0x200000cf': u'Параметром ключа -q должно быть натуральное число',
                  '0x200000d0': u'Не указан входной файл',
                  '0x200000d1': u'Не указан выходной файл',
                  '0x200000d2': u'Команда не использует параметр с именем файла',
                  '0x200000d3': u'Не указан  файл сообщения',
                  '0x2000012c': u'Не удалось открыть хранилище сертификатов:',
                  '0x2000012d': u'Сертификаты не найдены',
                  '0x2000012e': u'Найдено более одного сертификата (ключ -1)',
                  '0x2000012f': u'Команда подразумевает использование только одного сертификата',
                  '0x20000130': u'Неверно указан номер',
                  '0x20000131': u'Нет используемых сертификатов',
                  '0x20000132': u'Данный сертификат не может применяться для этой операции',
                  '0x20000133': u'Цепочка сертификатов не проверена. Установите требуемые корневые сертификаты и списки'
                                u' отзыва сертификатов.',
                  '0x20000134': u'Криптопровайдер, поддерживающий необходимый алгоритм не найден',
                  '0x20000135': u'Неудачный ввод пароля ключевого контейнера',
                  '0x20000136': u'Ошибка связи с закрытым ключом',
                  '0x20000190': u'Не указана маска файлов',
                  '0x20000191': u'Указаны несколько масок файлов',
                  '0x20000192': u'Файлы не найдены',
                  '0x20000193': u'Задана неверная маска',
                  '0x20000194': u'Неверный хеш',
                  '0x200001f4': u'Ключ -start указан, а выходной файл нет',
                  '0x200001f5': u'Содержимое файла - не подписанное сообщение',
                  '0x200001f6': u'Неизвестный алгоритм подписи',
                  '0x200001f7': u'Сертификат автора подписи не найден',
                  '0x200001f8': u'Подпись не найдена',
                  '0x200001f9': u'Подпись не верна',
                  '0x20000200': u'Штамп времени не верен',
                  '0x20000258': u'Содержимое файла - не зашифрованное сообщение',
                  '0x20000259': u'Неизвестный алгоритм шифрования',
                  '0x2000025a': u'Не найден сертификат с соответствующим секретным ключом',
                  '0x200002bc': u'Не удалось инициализировать cOM',
                  '0x200002bd': u'Контейнеры не найдены',
                  '0x200002be': u'Не удалось получить ответ от сервера',
                  '0x200002bf': u'Сертификат не найден в ответе сервера',
                  '0x200002c0': u'Файл не содержит идентификатор запроса:',
                  '0x200002c1': u'Некорректный адрес ЦС',
                  '0x200002c2': u'Получен неверный cookie',
                  '0x20000320': u'Серийный номер содержит недопустимое количество символов',
                  '0x20000321': u'Неверный код продукта',
                  '0x20000322': u'Не удалось проверить серийный номер',
                  '0x20000323': u'Не удалось сохранить серийный номер',
                  '0x20000324': u'Не удалось загрузить серийный номер',
                  '0x20000325': u'Лицензия просрочена'}
        try:
            return errors[error]
        except KeyError:
            return error

    # Генератор get_store_certs выдает найденные в заданном хранилище сертификаты в виде словарей
    def get_store_certs(self, store):
        certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % self.arch, '-list', '-store', store],
                                   stdout=subprocess.PIPE)
        output = certmgr.communicate()[0]
        m = re.findall(
            r'\d+-{7}\nIssuer.*?: (.+?)\n.*?Subject.*?: (.+?)\n.*?SHA1 Hash.*?0x(.+?)\nNot valid before.*?(\d.+?)UTC\nNot valid after.*?(\d.+?)UTC.+?PrivateKey Link.*?(Yes|No).*?\n',
            output, re.MULTILINE + re.DOTALL)
        for cert in m:
            issuerDN = dict(re.findall(ur'([A-Z0-9\.]+?)=("?[\w \.\,0-9@\-\#\/\"]+"?)(?:, |$)',
                                       cert[0].decode('utf-8'), re.UNICODE))
            issuerCN = issuerDN['CN']
            subjectDN = dict(re.findall(ur'([A-Z0-9\.]+?)=("?[\w \.\,0-9@\-\#\/\"]+"?)(?:, |$)',
                                        cert[1].decode('utf-8'), re.UNICODE))
            subjectCN = subjectDN['CN']
            secretKey = cert[5]
            thumbprint = cert[2]
            notValidBefore = cert[3]
            notValidAfter = cert[4]
            yield dict(issuerDN=issuerDN, issuerCN=issuerCN, subjectDN=subjectDN, subjectCN=subjectCN,
                       secretKey=secretKey, thumbprint=thumbprint, notValidBefore=notValidBefore,
                       notValidAfter=notValidAfter)

    # Метод sign выполняет операцию подписи заданного файла(filepath), при помощи заданного SHA-отпечатка
    # сертификата(thumbprint) и используя заданную кодировку(encoding): DER или BASE64
    # Путь до файла должен быть абсолютным. Подписанный файл сохраняется в той же директории с расширением '.sig'
    def sign(self, thumbprint, filepath, encoding):
        # Исправляем криптопрошные крокозябры
        new_env = dict(os.environ)
        new_env['LANG'] = 'en_US.UTF-8'

        if encoding == 'der':
            cryptcp = subprocess.Popen(['/opt/cprocsp/bin/%s/cryptcp' % self.arch, '-sign', '-thumbprint', thumbprint,
                                        '-errchain', '-der', filepath],
                                       cwd=os.path.dirname(filepath), stdout=subprocess.PIPE, env=new_env)
        else:
            cryptcp = subprocess.Popen(['/opt/cprocsp/bin/%s/cryptcp' % self.arch, '-sign', '-thumbprint', thumbprint,
                                        '-errchain', filepath],
                                       cwd=os.path.dirname(filepath), stdout=subprocess.PIPE, env=new_env)
        output = cryptcp.stdout.read()
        errorcode = re.search(r'(?:ErrorCode: |ReturnCode: )(?P<errorcode>\w+)', output,
                              re.MULTILINE + re.DOTALL).groupdict()['errorcode']
        if not errorcode == '0':
            raise Exception(self.error_description(errorcode))
        else:
            return True

    # Метод verify проверяет подпись файла(filepath).
    # Если требуется при этом отсоединить подпись от файла, указываем параметр dettach=True
    # Возвращает кортеж, состоящий из словаря сертификата и булева значения
    # указывающего была ли проверена цепочка сертификатов или нет. True - была, False - нет
    def verify(self, filepath, dettach=False):
        # Если это не файл подписи, проверяем лежащий рядом файл с расширением '.sig'
        if not filepath[-4:] == '.sig':
            filepath += '.sig'
            dettach = False
        # Исправляем криптопрошные крокозябры
        new_env = dict(os.environ)
        new_env['LANG'] = 'en_US.UTF-8'
        if dettach:
            cryptcp = subprocess.Popen(
                ['/opt/cprocsp/bin/%s/cryptcp' % self.arch, '-verify', '-verall', filepath, filepath[:-4]],
                stdout=subprocess.PIPE, stdin=subprocess.PIPE, env=new_env, shell=False)
        else:
            cryptcp = subprocess.Popen(['/opt/cprocsp/bin/%s/cryptcp' % self.arch, '-verify', '-verall', filepath],
                                       stdout=subprocess.PIPE, stdin=subprocess.PIPE, env=new_env, shell=False)
        # Согласиться
        cryptcp.stdin.write('Y')
        output = cryptcp.stdout.read()
        chainisverified = not 'The certificate revocation status or one of the certificates in the certificate chain ' \
                              'is unknown.' in output
        m = re.search(r'Signer: (?P<signer>.+?)\n.*(?:ErrorCode: |ReturnCode: )(?P<errorcode>\w+)', output,
                      re.MULTILINE + re.DOTALL)
        errorcode = re.search(r'(?:ErrorCode: |ReturnCode: )(?P<errorcode>\w+)', output,
                              re.MULTILINE + re.DOTALL).groupdict()['errorcode']
        if not errorcode == '0':
            raise Exception(self.error_description(errorcode))
        else:
            return m.groupdict(), chainisverified

    # Метод encrypt шифрует заданный файл(filepath), при помощи SHA-отпечатка сертификата(thumbprint),
    # и используя заданную кодировку(encoding): DER или BASE64
    # Путь до файла должен быть абсолютным. Зашифрованный файл сохраняется в той же директории с расширением '.enc'
    def encrypt(self, thumbprint, filepath, encoding):
        # Исправляем криптопрошные крокозябры
        new_env = dict(os.environ)
        new_env['LANG'] = 'en_US.UTF-8'

        if encoding == 'der':
            cryptcp = subprocess.Popen(['/opt/cprocsp/bin/%s/cryptcp' % self.arch, '-encr', '-der',
                                        '-thumbprint', thumbprint, filepath, filepath + '.enc'],
                                       stdout=subprocess.PIPE, stdin=subprocess.PIPE, env=new_env, shell=False)
        else:
            cryptcp = subprocess.Popen(
                ['/opt/cprocsp/bin/%s/cryptcp' % self.arch, '-encr', '-thumbprint', thumbprint, filepath,
                 filepath + '.enc'],
                stdout=subprocess.PIPE, stdin=subprocess.PIPE, env=new_env, shell=False)
        # Согласит
        cryptcp.stdin.write('Y')
        output = cryptcp.stdout.read()
        chainisverified = not 'The certificate revocation status or one of the certificates in the certificate chain ' \
                              'is unknown.' in output
        errorcode = re.search(r'(?:ErrorCode: |ReturnCode: )(?P<errorcode>\w+)', output,
                              re.MULTILINE + re.DOTALL).groupdict()['errorcode']
        if not errorcode == '0':
            raise Exception(self.error_description(errorcode))
        else:
            return True, chainisverified

    # Метод decrypt расшифровывает заданный файл(filepath) при помощи SHA-отпечатка сертификата(thumbprint)
    # Расшифрованный файл сохраняется в той же директории, лишаясь расширения '.enc'
    def decrypt(self, thumbprint, filepath):
        if not filepath[-4:] == '.enc':
            pass
        # Исправляем криптопрошные крокозябры
        new_env = dict(os.environ)
        new_env['LANG'] = 'en_US.UTF-8'

        cryptcp = subprocess.Popen(['/opt/cprocsp/bin/%s/cryptcp' % self.arch, '-decr',
                                    '-thumbprint', thumbprint, filepath, filepath[:-4]],
                                   stdout=subprocess.PIPE, stdin=subprocess.PIPE, env=new_env, shell=False)
        # Согласит
        cryptcp.stdin.write('Y')
        output = cryptcp.stdout.read()
        chainisverified = not 'The certificate revocation status or one of the certificates in the certificate chain ' \
                              'is unknown.' in output
        errorcode = re.search(r'(?:ErrorCode: |ReturnCode: )(?P<errorcode>\w+)', output,
                              re.MULTILINE + re.DOTALL).groupdict()['errorcode']
        if not errorcode == '0':
            raise Exception(self.error_description(errorcode))
        else:
            return True, chainisverified
