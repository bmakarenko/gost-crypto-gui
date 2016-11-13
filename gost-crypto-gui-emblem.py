import os.path
import gostcryptogui
import nautilus
import urllib

class SignatureCheckProvider(nautilus.InfoProvider):
    def __init__(self):
        pass

    def update_file_info(self, file):
        if file.get_uri_scheme() != 'file':
            return
        if os.path.splitext(file.get_name())[1] == ".sig":
            filepath = urllib.unquote(file.get_uri())[7:]
            signer, chain, revoked, expired = gostcryptogui.cprocsp.CryptoPro().verify(unicode(filepath), False)
            if not chain:
                file.add_emblem("nochain")
            elif expired or revoked:
                file.add_emblem("unverified")
            else:
                file.add_emblem("verified")
