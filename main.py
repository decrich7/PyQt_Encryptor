# -*- coding: utf-8 -*-
from encryption_algorithms.caesar_cipher import CaesarRu, CaesarEn
from encryption_algorithms.AES import Aes
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_1, base_1 = uic.loadUiType('ui_designs/untitled.ui')
form_algoritm, base_algoritm = uic.loadUiType('ui_designs/algoritm_encript.ui')
form_ceasar, base_ceasar = uic.loadUiType('ui_designs/caesar.ui')
form_ceasar_dec, base_ceasar_dec = uic.loadUiType('ui_designs/caesar_dec.ui')
form_aes_encr, base_aes_encr = uic.loadUiType('ui_designs/aes_enc.ui')
form_aes_decr, base_aes_decr = uic.loadUiType('ui_designs/aes_dec.ui')



class MyWidget(base_1, form_1):
    def __init__(self):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run_algoritm_encript)
        self.pushButton_2.clicked.connect(self.run_algoritm_decript)

    def run_algoritm_encript(self):
        self.algoritm_encript = AlgoritmEncript()
        self.algoritm_encript.show()
        self.close()

    def run_algoritm_decript(self):
        self.algoritm_decript = AlgoritmDecript()
        self.algoritm_decript.show()
        self.close()


class AlgoritmEncript(form_algoritm, base_algoritm):
    def __init__(self):
        super(base_algoritm, self).__init__()
        self.setupUi(self)
        # self.Button_RSA.clicked.connect(self.rsa)
        self.Button_Cezar.clicked.connect(self.Caesar_Cipher)
        self.Button_AES.clicked.connect(self.aes)
        self.pushButton.clicked.connect(self.beak_to_MyWidget)

    #
    def beak_to_MyWidget(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()

    def aes(self):
        self.aesencr = AesEncr()
        self.aesencr.show()
        self.close()

    def Caesar_Cipher(self):
        self.window_Caesar = Window_Caesar()
        self.window_Caesar.show()
        self.close()
        # enc_caesar = Caesar()


class AesEncr(form_aes_encr, base_aes_encr):
    def __init__(self):
        super(base_aes_encr, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_2.clicked.connect(self.beak_to_alg_enc)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)

    def encrypt(self):
        text_enc = self.textEdit_2.toPlainText()
        if self.radioButton_3.isChecked():
            if text_enc != '':
                aes_256 = Aes(256)
                aes_256.generate_key()
                self.textEdit.setText(str(aes_256.enc_aes(text_enc)))
                self.textEdit_3.setText(aes_256.print_key())
        elif self.radioButton_2.isChecked():
            if text_enc != '':
                aes_128 = Aes(128)
                aes_128.generate_key()
                text = str(aes_128.enc_aes(text_enc))
                self.textEdit.setText(text)
                self.textEdit_3.setText(aes_128.print_key())

    def beak_to_alg_enc(self):
        self.alg_enc = AlgoritmEncript()
        self.alg_enc.show()
        self.close()

    def beak_to_my_widg(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()


class Window_Caesar(form_ceasar, base_ceasar):
    def __init__(self):
        super(base_ceasar, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_2.clicked.connect(self.beak_to_alg_enc)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)

    def encrypt(self):
        text_enc = self.textEdit_2.toPlainText()
        key = self.spinBox.value()
        if self.radioButton.isChecked():
            if text_enc != '' and key <= 33:
                enc = CaesarRu(key, text_enc)
                self.textEdit.setText(enc.cipher())
        elif self.radioButton_2.isChecked():
            if text_enc != '' and key <= 33:
                enc = CaesarEn(key, text_enc)
                self.textEdit.setText(enc.cipher())

    def beak_to_alg_enc(self):
        self.alg_enc = AlgoritmEncript()
        self.alg_enc.show()
        self.close()

    def beak_to_my_widg(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()


class AlgoritmDecript(form_algoritm, base_algoritm):
    def __init__(self):
        super(base_algoritm, self).__init__()
        self.setupUi(self)
        self.Button_RSA.clicked.connect(self.rsa)
        self.Button_Cezar.clicked.connect(self.caesar_cipher_dec)
        self.pushButton.clicked.connect(self.beak_to_MyWidget)

    def beak_to_MyWidget(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()

    def rsa(self):
        pass

    def caesar_cipher_dec(self):
        self.window_caesar_dec = WindowCaesarDec()
        self.window_caesar_dec.show()
        self.close()


class AesDecr(form_aes_decr, base_aes_decr):
    def __init__(self):
        super(base_aes_decr, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_2.clicked.connect(self.beak_to_alg_enc)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)

    def encrypt(self):
        text_enc = self.textEdit_2.toPlainText()
        if self.radioButton_3.isChecked():
            if text_enc != '':
                aes_256 = Aes(256)
                aes_256.generate_key()
                self.textEdit.setText(str(aes_256.enc_aes(text_enc)))
                self.textEdit_3.setText(aes_256.print_key())
        elif self.radioButton_2.isChecked():
            if text_enc != '':
                aes_128 = Aes(128)
                aes_128.generate_key()
                text = str(aes_128.enc_aes(text_enc))
                self.textEdit.setText(text)
                self.textEdit_3.setText(aes_128.print_key())

    def beak_to_alg_enc(self):
        self.alg_enc = AlgoritmEncript()
        self.alg_enc.show()
        self.close()

    def beak_to_my_widg(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()

class WindowCaesarDec(form_ceasar_dec, base_ceasar_dec):
    def __init__(self):
        super(base_ceasar_dec, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.decrypt)
        self.pushButton_2.clicked.connect(self.beak_to_alg_dec)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)

    def beak_to_alg_dec(self):
        self.algdec = AlgoritmDecript()
        self.algdec.show()
        self.close()

    def decrypt(self):
        text_enc = self.textEdit_2.toPlainText()
        key = self.spinBox.value()
        if self.radioButton.isChecked():
            if text_enc != '' and key <= 33:
                enc = CaesarRu(key, text_enc)
                self.textEdit.setText(enc.dec())
        elif self.radioButton_2.isChecked():
            if text_enc != '' and key <= 33:
                enc = CaesarEn(key, text_enc)
                self.textEdit.setText(enc.dec())

    def beak_to_my_widg(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
