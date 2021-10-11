# -*- coding: utf-8 -*-

import base64
import random
import string
import pyaes


class Aes:
    def __init__(self, size):
        # self.message = message
        self.size = size
        self.key = None

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
        plaintext = base64.b64encode(bytes(message, 'utf-8'))
        key = self.key.encode('utf-8')
        aes = pyaes.AESModeOfOperationCTR(key)
        return str(base64.b64encode(aes.encrypt(plaintext)))[2:-1]

    def dec_aes(self, message, key):
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypted = aes.decrypt(message).decode('utf-8')
        decoded_data = base64.b64decode(decrypted)
        return decoded_data.decode('utf-8')


ex = Aes(128)
ex.generate_key()
dfg = ex.enc_aes('Внутри функции мы сгенерировали случайную строку с комбинацией нижнего регистра, а затем использовали константу string.ascii_letters. Константа string.ascii_letters включает все строчные и прописные буквы.Чтобы сгенерировать')
# dfgg = ex.dec_aes("b'R\xacW\xa6 \x02\x04\x18\xb9\xe0\x98keT0\x1f>5(\xb5\x15\xc9g\n\x83%\xf9h\x10e9\x8f\xf9Okqp\xc7\'\x1b\x08\x9be\x1b\xf8\x15\xce!\xeb\xcb\x98$\x85g\xe5\xc1R\xf425\xd3J\x85$T\xb92_\x0bF!\x17^j\xd291\xf5I\xebC\xc1\xb6\'h=\x06\x13\xf7\xd9\x85\'\x02\x8a\x8bjC\x0eN4\x19\x8ft\x10\x06\x82\x95i|\xaff\x12\x8b\xf9BU\xe6\xfdd\x1b\xaf\x80\x9c\xfd4\xef\xa2\xe6\xa7\xaa\xe4\xd3"@\xf2\xa3\xe3\x14\xa6\x96E,\x16E(\xafhX\x87$.\xd8\x80-\xbc\x1a\x19D\xa6\x18\xd1B\xf4\x8bs$\x11\xc48"h\xe5\xe6\xe0\xb75&\x06\xc9u\xfdL\xcdD1NYp\\](\xca\x9bJe\xcc\xb5&\x01U\xcbF!\rcN\xd5\xf4u3\xba\x86\x14\xc8\x15{\xbdf\xc1\xfc\xf3\x82\xc9\xcd,G\xad\x90\xa4\x9b\x05e\xfdgx\xd4\x98\xc6\xb3\x1a\x16\xc7J=3\x81[\xfa\x1f\x98\x13\x18~\xd5O\xb7\xda\xe1\x93x\x02=\x8dK\xba\x16\xe7x/\xf7\x9f\x06\x14\xe3\x18\xd8#G\xa0\xf2x\xa5.0lzRI\x03\xb5E4&\xff\xc3\xdb\x8bNb-\xd3yiQ4\xd9jBS\xdaJ\x12 (P\xd7\xc6\xc5\xe8\x02-v^omU:\x02\xa4\xfc\xbb\xd3p\xb3[a\x0c\x9e}\x1d\xc5MK~b\xeb\xb4\x03n\n\x86\x87A\x9a\xbd>2.\xcc\x88\xc3\x07\x9b\xf0_\xf6\xe6\x1a\xfdD\x16V\x80\xc9\x91\x10hks$\x8f0\xce\x14\x07\xef\xbf2\x86r\x04\xba)\xb8\x14\xbd\x02I\xec\xbf:\x1fH\xe5\x03\xdaVR\xce\x1c0\xd3\xca\x1b\xc2\xb5l\xef\xe9zY\xbc\x0cw\xbc\xcf\x8dlG\x13\xb4\x15B\x14k\x8c\xc8~\xfe\xdcP\xc9\xb0\x83\xcb\xc3\xefI\r\xa34kiV)6\x84\xbc\x07\x89\xf3V\xf2\xca@xXY\x0f\xa2|y\t\xda\x97\x13\xc7o\xcd,\xa4\xfc\xa1?\xfa>2\x11\xef\xd8>"7\xd8g\xd1\x11Q\xdd\xef|4\xe1,\xc8\x05L~\xbf\xbad\x03'")
print(ex.print_key())
print(dfg)
# print(dfgg)
