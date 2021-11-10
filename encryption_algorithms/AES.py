# -*- coding: utf-8 -*-

import base64
import random
import string
import pyaes


class Aes:
    def __init__(self, size, key=None):
        # self.message = message
        self.size = size
        self.key = key

    def generate_key(self):
        if self.size == 256:
            self.key = ''.join(random.choice(string.ascii_lowercase) for i in range(self.size // 8))
        elif self.size == 128:
            self.key = ''.join(random.choice(string.ascii_lowercase) for i in range(self.size // 8))

    def print_key(self):
        return self.key

    def enc_aes(self, message):
        plaintext = message.encode('utf-8')
        key = self.key.encode('utf-8')
        aes = pyaes.AESModeOfOperationCTR(key)
        str_aes = aes.encrypt(plaintext)
        txt = base64.b64encode(str_aes)
        return txt.decode('utf-8')

    def enc_aes_file(self, message):
        plaintext = message.encode('utf-8')
        key = self.key.encode('utf-8')
        aes = pyaes.AESModeOfOperationCTR(key)
        str_aes = aes.encrypt(plaintext)
        return str_aes

    def enc_aes_file_key(self, message, key):
        plaintext = message.encode('utf-8')
        key = key.encode('utf-8')
        aes = pyaes.AESModeOfOperationCTR(key)
        str_aes = aes.encrypt(plaintext)
        return str_aes

    def dec_aes_file(self, key_path, msg_path):
        key = open(key_path, 'rb').read()
        message = open(msg_path, 'rb').read()
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypted = aes.decrypt(message).decode('utf-8')
        return decrypted

    def dec_aes(self, message, key):
        aes = pyaes.AESModeOfOperationCTR(key.encode('utf-8'))
        decrypted = aes.decrypt(message).decode('utf-8')
        return decrypted

# ex = Aes(128)
# ex.generate_key()
# print(ex.print_key())
# print(ex.dec_aes_file())
# dfg = ex.enc_aes('За эту победу юный князь Александр получил почетное прозвище Невский.')
# print(ex.print_key(), 'key')
# print(dfg)
# # print('\xb1w\x8e\xd1\xfd\xc0\xc9\xf9\xe2\r7D\x9b3c^)\xb6\xa6J\xf7\x1d\x8a7\x91d\x00\xa6\xca'.decode('utf-8'))
# print(ex.dec_aes(b'\x08`\xdd\xe1\xc1\x04W\xfc!\x9b\x8a:\xbeB+\x99\xf2\xf3#H\xd1\\\xc9\xde\x9aC\xd1\xb5\x90e\x87j\x9d\xfd\x18:\xc13B\xa9$*\x7f\x08\x13\xcb\xfc\x82L\x18\x88\xf2\x16\xca.\xe6\x9bd\xa9\x18\xdf\xe0\x1173\xf1\xa7\x02\xa8j\x81\xf8\xac?\x7f\x00\x03\xbcd$\x01\xdb.\xe3`\xe9\x96\xee)', 'qpiynjhuwopepwvv'))
