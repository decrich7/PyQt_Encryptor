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
        elif self.size == 64:
            self.key = ''.join(random.choice(string.ascii_lowercase) for i in range(self.size // 8))

    def print_key(self):
        return self.key

    def enc_aes(self, message):
        plaintext = message.encode('utf-8')
        key = self.key.encode('utf-8')
        aes = pyaes.AESModeOfOperationCTR(key)
        return str(aes.encrypt(plaintext))[2:-1]

    def dec_aes(self, message, key):
        aes = pyaes.AESModeOfOperationCTR(key.encode('utf-8'))
        decrypted = aes.decrypt(message).decode('utf-8')
        return decrypted


# ex = Aes(128)
# ex.generate_key()
# dfg = ex.enc_aes('Внутри генерировters ые буквы.Чтобы сгенерировать')
# print(ex.print_key(), 'key')
# print(dfg)
# print(ex.dec_aes('\xe2\x003\xc5\xf4|L\xbd\x17\x92\xdbG\xde\x07F\xf6\xbeL\x8c\xb1\xfc~\xfc$\x06\x8bFB\xb1\xc8\xab\x03\xa0*\x99]\xa0&\xeb\x0f\x98\x98\xa0\xd8\xe3f\xa6?\xc0B\xad\xa8\x8a\xc5\x8eE\x16Y6,\x87\xfd\xa5L\x90\t\xeck\xa7l\xb8\x1et\x13\xd4\x81\x9f<\xf3\x82K\x85l\x02\xef\x9f\xff\xec\xe2', 'mlnvynhwzcnaicci'))
