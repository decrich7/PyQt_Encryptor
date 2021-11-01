# -*- coding: utf-8 -*-
import base64
import sqlite3

import psycopg2

from DB_API import Database
from encryption_algorithms.caesar_cipher import CaesarRu, CaesarEn
from encryption_algorithms.AES import Aes
from encryption_algorithms.RSA import Rsa
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialogButtonBox, QColorDialog, QPushButton, QInputDialog
from untitled import Ui_MainWindow

db = Database()
# form_1, base_1 = uic.loadUiType('ui_designs/untitled.ui')
form_algoritm, base_algoritm = uic.loadUiType('ui_designs/algoritm_encript.ui')
form_ceasar, base_ceasar = uic.loadUiType('ui_designs/caesar.ui')
form_ceasar_dec, base_ceasar_dec = uic.loadUiType('ui_designs/caesar_dec.ui')
form_aes_encr, base_aes_encr = uic.loadUiType('ui_designs/aes_enc.ui')
form_aes_decr, base_aes_decr = uic.loadUiType('ui_designs/aes_dec.ui')
form_rsa_encr, base_rsa_encr = uic.loadUiType('ui_designs/rsa_enc.ui')
form_rsa_encr, base_rsa_encr = uic.loadUiType('ui_designs/rsa_dec.ui')

list1 = []


class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        if len(list1) == 0:
            name, ok_pressed = QInputDialog.getText(self, "Nickname", "Введите ваш Nickname")
            list1.append(name)
            if ok_pressed:
                try:
                    db.insert_name(name)
                except sqlite3.IntegrityError:
                    pass

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
        self.Button_RSA.clicked.connect(self.rsa)
        self.Button_Cezar.clicked.connect(self.Caesar_Cipher)
        self.Button_AES.clicked.connect(self.aes)
        self.pushButton.clicked.connect(self.beak_to_MyWidget)

    def beak_to_MyWidget(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()

    def rsa(self):
        self.rsa = RsaEnc()
        self.rsa.show()
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


class RsaEnc(form_rsa_encr, base_rsa_encr):
    def __init__(self):
        super(base_rsa_encr, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_2.clicked.connect(self.beak_to_alg_enc)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)

    def encrypt(self):
        text_enc = self.textEdit_2.toPlainText()
        if text_enc != '':
            rsa = Rsa(text_enc)
            self.fin = rsa.generate_enc_message()
            self.textEdit.setText(self.fin[-1])
            self.textEdit_3.setText(
                f'Ключ который нужно передать собеседнику: {self.fin[0]}\nПриватный ключ: {self.fin[1]}')
            self.buttonBox = QMessageBox()
            self.buttonBox.setWindowTitle('Сохранение ключа')
            self.buttonBox.setText("Вы хотите запомнить ключи, чтобы не вводить их каждый раз?")
            self.buttonBox.setIcon(QMessageBox.Warning)
            self.buttonBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            self.buttonBox.buttonClicked.connect(self.write_db_key_rsa)
            self.buttonBox.exec_()

    def write_db_key_rsa(self, btn):
        if btn.text() == '&Yes':
            global list1
            print(list1[0])
            db.insert_key_rsa(self.fin[0], self.fin[1], list1[0])
        else:
            pass

    def beak_to_alg_enc(self):
        self.alg_enc = AlgoritmEncript()
        self.alg_enc.show()
        self.close()

    def beak_to_my_widg(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()


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
                self.aes = Aes(256)
                self.aes.generate_key()
                self.textEdit.setText(str(self.aes.enc_aes(text_enc)))
                self.textEdit_3.setText(self.aes.print_key())
        elif self.radioButton_2.isChecked():
            if text_enc != '':
                self.aes = Aes(128)
                self.aes.generate_key()
                text = str(self.aes.enc_aes(text_enc))
                self.textEdit.setText(text)
                self.textEdit_3.setText(self.aes.print_key())

        self.buttonBox = QMessageBox()
        self.buttonBox.setWindowTitle('Сохранение ключа')
        self.buttonBox.setText("Вы хотите запомнить ключ, чтобы не вводить его каждый раз при дешифровке?")
        self.buttonBox.setIcon(QMessageBox.Warning)
        self.buttonBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.buttonBox.buttonClicked.connect(self.write_db_key_rsa)
        self.buttonBox.exec_()

    def write_db_key_rsa(self, btn):
        if btn.text() == '&Yes':
            global list1
            try:
                db.insert_key_aes(self.aes.print_key(), list1[0])
            except Exception as r:
                print(r)
        else:
            pass

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
        self.Button_AES.clicked.connect(self.aes)
        self.Button_Cezar.clicked.connect(self.caesar_cipher_dec)
        self.pushButton.clicked.connect(self.beak_to_MyWidget)

    def rsa(self):
        self.rsa = RsaDecr()
        self.rsa.show()
        self.close()

    def beak_to_MyWidget(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()

    def aes(self):
        self.aesdecr = AesDecr()
        self.aesdecr.show()
        self.close()

    def caesar_cipher_dec(self):
        self.window_caesar_dec = WindowCaesarDec()
        self.window_caesar_dec.show()
        self.close()


class RsaDecr(form_rsa_encr, base_rsa_encr):
    def __init__(self):
        super(base_rsa_encr, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.decrypt)
        self.pushButton_2.clicked.connect(self.beak_to_alg_enc)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)

    def decrypt(self):
        text_enc = self.textEdit_2.toPlainText()
        key = self.textEdit_3.toPlainText()
        if text_enc != '':
            rsa = Rsa(text_enc)
            self.textEdit.setText(rsa.decript(key, text_enc))

    def beak_to_alg_enc(self):
        self.alg_enc = AlgoritmDecript()
        self.alg_enc.show()
        self.close()

    def beak_to_my_widg(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()


class AesDecr(form_aes_decr, base_aes_decr):
    def __init__(self):
        super(base_aes_decr, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.decrypt)
        self.pushButton_2.clicked.connect(self.beak_to_alg_enc)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)

    def decrypt(self):
        global list1
        text_enc = self.textEdit_2.toPlainText()
        text_enc = base64.b64decode(text_enc)
        key = self.textEdit_3.toPlainText()
        if text_enc != '':
            aes = Aes(128)
            if db.select_key_aes(list1[0]) is not None:
                self.textEdit.setText(aes.dec_aes(text_enc, str(db.select_key_aes(list1[0]))[3:-4]))
            else:
                self.textEdit.setText(aes.dec_aes(text_enc, key))

    def beak_to_alg_enc(self):
        self.alg_enc = AlgoritmDecript()
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
