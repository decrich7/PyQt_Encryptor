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
