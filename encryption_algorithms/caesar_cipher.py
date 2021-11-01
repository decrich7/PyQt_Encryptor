# -*- coding: utf-8 -*-
class CaesarRu:
    def __init__(self, key, message):
        self.key = key
        self.message = message

    def cipher(self):
        if self.key > 33:
            self.key = self.key % 33
        caesar = ''
        for i in self.message:
            if ord(i) >= ord('а') and ord(i) <= ord('я'):
                if ord(i) + self.key > ord('я'):
                    caesar = caesar + chr((ord(i) + self.key) - 33)
                else:
                    caesar = caesar + chr(ord(i) + self.key)
            elif ord(i) >= ord('А') and ord(i) <= ord('Я'):
                if ord(i) + self.key > ord('Я'):
                    caesar = caesar + chr((ord(i) + self.key) - 33)
                else:
                    caesar = caesar + chr(ord(i) + self.key)
            else:
                caesar = caesar + i
        return caesar

    def dec(self):
        if self.key > 33:
            self.key = self.key % 33
        caesar = ''
        for i in self.message:
            if ord(i) >= ord('а') and ord(i) <= ord('я'):
                if ord(i) - self.key < ord('а'):
                    caesar = caesar + chr((ord(i) - self.key) + 33)
                else:
                    caesar = caesar + chr(ord(i) - self.key)
            elif ord(i) >= ord('А') and ord(i) <= ord('Я'):
                if ord(i) - self.key < ord('А'):
                    caesar = caesar + chr((ord(i) - self.key) + 33)
                else:
                    caesar = caesar + chr(ord(i) - self.key)
            else:
                caesar = caesar + i
        return caesar.replace('Ъ', 'ы')


class CaesarEn:
    def __init__(self, key, message):
        self.key = key
        self.message = message

    def cipher(self):
        if self.key > 26:
            self.key = self.key % 26
        caesar = ''
        for i in self.message:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                if ord(i) + self.key > ord('z'):
                    caesar = caesar + chr((ord(i) + self.key) - 26)
                else:
                    caesar = caesar + chr(ord(i) + self.key)
            elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
                if ord(i) + self.key > ord('Z'):
                    caesar = caesar + chr((ord(i) + self.key) - 26)
                else:
                    caesar = caesar + chr(ord(i) + self.key)
            else:
                caesar = caesar + i
        return caesar

    def dec(self):
        if self.key > 26:
            self.key = self.key % 26
        caesar = ''
        for i in self.message:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                if ord(i) - self.key < ord('a'):
                    caesar = caesar + chr((ord(i) - self.key) + 26)
                else:
                    caesar = caesar + chr(ord(i) - self.key)
            elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
                if ord(i) - self.key < ord('A'):
                    caesar = caesar + chr((ord(i) - self.key) + 26)
                else:
                    caesar = caesar + chr(ord(i) - self.key)
            else:
                caesar = caesar + i
        return caesar.replace('Ъ', 'ы')

