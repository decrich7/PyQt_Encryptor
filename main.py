# -*- coding: utf-8 -*-
import base64
import sqlite3
from DB_API import Database
from encryption_algorithms.caesar_cipher import CaesarRu, CaesarEn
from encryption_algorithms.AES import Aes
from encryption_algorithms.RSA import Rsa
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog, QMainWindow, QFileDialog
from ui_designs.untitled import Ui_MainWindow
from ui_designs.aes_dec_py import Ui_MainWindowAesDec
from ui_designs.aes_enc_py import Ui_MainWindowAesEnc
from ui_designs.algoritm_encript_py import Ui_MainWindowAlgoritmEncript
from ui_designs.caesar_py import Ui_MainWindowCaezar
from ui_designs.ceasar_dec_py import Ui_MainWindowCaezarDec
from ui_designs.rsa_dec_py import Ui_MainWindowRsaDec
from ui_designs.rsa_enc_py import Ui_MainWindowRsaEnc
from ui_designs.aes_dec_file import Ui_MainWindowDecFile
from ui_designs.aes_enc_file import Ui_MainWindowEncFile
db = Database()
# form_file, base_file = uic.loadUiType('ui_designs/aes_enc_file.ui')
# form_1, base_1 = uic.loadUiType('ui_designs/untitled.ui')
# form_algoritm, base_algoritm = uic.loadUiType('ui_designs/algoritm_encript.ui')
# form_ceasar, base_ceasar = uic.loadUiType('ui_designs/caesar.ui')
# form_ceasar_dec, base_ceasar_dec = uic.loadUiType('ui_designs/caesar_dec.ui')
# form_aes_encr, base_aes_encr = uic.loadUiType('ui_designs/aes_enc.ui')
# form_aes_decr, base_aes_decr = uic.loadUiType('ui_designs/aes_dec.ui')
# form_rsa_encr, base_rsa_encr = uic.loadUiType('ui_designs/rsa_enc.ui')
# form_rsa_encr, base_rsa_encr = uic.loadUiType('ui_designs/rsa_dec.ui')

list1 = []


class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        db.create_table_users()
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
        self.pushButton_3.clicked.connect(self.run_enc_file)
        self.pushButton_4.clicked.connect(self.run_dec_file)

    def run_dec_file(self):
        self.dec_file = DecFile()
        self.dec_file.show()
        self.close()

    def run_enc_file(self):
        self.enc_file = EncFile()
        self.enc_file.show()
        self.close()

    def run_algoritm_encript(self):
        self.algoritm_encript = AlgoritmEncript()
        self.algoritm_encript.show()
        self.close()

    def run_algoritm_decript(self):
        self.algoritm_decript = AlgoritmDecript()
        self.algoritm_decript.show()
        self.close()


class AlgoritmEncript(QtWidgets.QMainWindow, Ui_MainWindowAlgoritmEncript):
    def __init__(self):
        super().__init__()
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


class RsaEnc(QtWidgets.QMainWindow, Ui_MainWindowRsaEnc):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_2.clicked.connect(self.beak_to_alg_enc)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)
        self.pushButton_4.clicked.connect(self.delete_key)
        self.pushButton_5.clicked.connect(self.print_key)

    def print_key(self):

        self.textEdit_3.setText(
            f'Ключ который нужно передать собеседнику: {db.select_key_rsa(list1[0])[0][0]}\nПриватный ключ:'
            f' {db.select_key_rsa(list1[0])[0][1]}')


    def delete_key(self):
        db.delete_key_rsa(list1[0])
        self.textEdit_3.setText('Ключи удалены')


    def encrypt(self):
        text_enc = self.textEdit_2.toPlainText()
        if text_enc != '':
            if self.textEdit_3.toPlainText() != '':
                rsa = Rsa(text_enc)
                self.textEdit.setText(rsa.encript(self.textEdit_3.toPlainText(), text_enc))
            else:
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


class AesEncr(QtWidgets.QMainWindow, Ui_MainWindowAesEnc):
    def __init__(self):
        super().__init__()
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
        self.buttonBox.buttonClicked.connect(self.write_db_key_aes)
        self.buttonBox.exec_()

    def write_db_key_aes(self, btn):
        if btn.text() == '&Yes':
            global list1
            db.insert_key_aes(self.aes.print_key(), list1[0])
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


class Window_Caesar(QtWidgets.QMainWindow, Ui_MainWindowCaezar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_2.clicked.connect(self.beak_to_alg_enc)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)

    def encrypt(self):
        text_enc = self.textEdit_2.toPlainText()
        self.key = self.spinBox.value()
        if self.radioButton.isChecked():
            if text_enc != '' and self.key <= 33:
                enc = CaesarRu(self.key, text_enc)
                self.textEdit.setText(enc.cipher())
        elif self.radioButton_2.isChecked():
            if text_enc != '' and self.key <= 33:
                enc = CaesarEn(self.key, text_enc)
                self.textEdit.setText(enc.cipher())

        self.buttonBox = QMessageBox()
        self.buttonBox.setWindowTitle('Сохранение ключа')
        self.buttonBox.setText("Вы хотите запомнить ключ, чтобы не вводить его каждый раз при дешифровке?")
        self.buttonBox.setIcon(QMessageBox.Warning)
        self.buttonBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.buttonBox.buttonClicked.connect(self.insert_key_ceazar)
        self.buttonBox.exec_()

    def insert_key_ceazar(self, btn):
        if btn.text() == '&Yes':
            global list1
            db.insert_key_ceazar(self.key, list1[0])
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


class AlgoritmDecript(QtWidgets.QMainWindow, Ui_MainWindowAlgoritmEncript):
    def __init__(self):
        super().__init__()
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


class RsaDecr(QtWidgets.QMainWindow, Ui_MainWindowRsaDec):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.decrypt)
        self.pushButton_2.clicked.connect(self.beak_to_alg_enc)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)

    def decrypt(self):
        text_enc = self.textEdit_2.toPlainText()
        key = self.textEdit_3.toPlainText()
        rsa = Rsa(text_enc)

        if text_enc != '':
            if db.select_key_rsa(list1[0])[0][1] is not None:
                self.textEdit.setText(rsa.decript(db.select_key_rsa(list1[0])[0][1], text_enc))
            else:
                self.textEdit.setText(rsa.decript(key, text_enc))

    def beak_to_alg_enc(self):
        self.alg_enc = AlgoritmDecript()
        self.alg_enc.show()
        self.close()

    def beak_to_my_widg(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()


class AesDecr(QtWidgets.QMainWindow, Ui_MainWindowAesDec):
    def __init__(self):
        super().__init__()
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
            if db.select_key_aes(list1[0])[0][0] is not None:
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


class WindowCaesarDec(QtWidgets.QMainWindow, Ui_MainWindowCaezarDec):
    def __init__(self):
        super().__init__()
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
                if db.select_key_ceazar(list1[0])[0][0] is not None:
                    enc = CaesarRu(int(db.select_key_ceazar(list1[0])[0][0]), text_enc)
                    self.textEdit.setText(enc.dec())
                else:
                    enc = CaesarRu(key, text_enc)
                    self.textEdit.setText(enc.dec())
        elif self.radioButton_2.isChecked():
            if text_enc != '' and key <= 33:
                if db.select_key_ceazar(list1[0])[0][0] is not None:
                    enc = CaesarEn(int(db.select_key_ceazar(list1[0])[0][0]), text_enc)
                    self.textEdit.setText(enc.dec())
                else:
                    enc = CaesarEn(key, text_enc)
                    self.textEdit.setText(enc.dec())

    def beak_to_my_widg(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()


class EncFile(QtWidgets.QMainWindow, Ui_MainWindowEncFile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path_key = ''
        self.pushButton.clicked.connect(self.enc)
        self.pushButton_2.clicked.connect(self.beak_to_my_widg)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)
        self.pushButton_4.clicked.connect(self.choise_file_enc)
        self.pushButton_5.clicked.connect(self.choise_key)

    def enc(self):
        if self.path != '':
            self.text = open(self.path).read()
            if self.path_key != '':
                self.key = str(open(self.path_key, 'rb').read())[2:-1]
                self.aes = Aes(000)
                enc_text = self.aes.enc_aes_file_key(self.text, self.key)
                file = open('encrypted_message.bin', 'wb')
                file.write(enc_text)
                file.close()

            if self.radioButton_3.isChecked():

                self.aes = Aes(256)
                self.aes.generate_key()
                enc_text_256 = open('encrypted_message_256.bin', 'wb')
                enc_text_256.write(self.aes.enc_aes_file(self.text))
                enc_text_256.close()
                key = open('keyAes.bin', 'wb')
                key.write(bytes(self.aes.print_key(), 'utf-8'))
                key.close()

            elif self.radioButton_2.isChecked():
                self.aes = Aes(128)
                self.aes.generate_key()
                enc_text_256 = open('encrypted_message_128.bin', 'wb')
                enc_text_256.write(self.aes.enc_aes_file(self.text))
                enc_text_256.close()
                key = open('keyAes.bin', 'wb')
                key.write(bytes(self.aes.print_key(), 'utf-8'))
                key.close()

    def beak_to_my_widg(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()

    def choise_file_enc(self):
        self.path = QFileDialog.getOpenFileName(self, 'Выбрать текстовый файл', '', 'Текстовый файл (*.txt)')[0]

    def choise_key(self):
        self.path_key = QFileDialog.getOpenFileName(self, 'Выбрать файл с ключем', '', 'Ключ шифрования (*.bin)')[0]


class DecFile(QtWidgets.QMainWindow, Ui_MainWindowDecFile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.dec)
        self.pushButton_2.clicked.connect(self.beak_to_my_widg)
        self.pushButton_3.clicked.connect(self.beak_to_my_widg)
        self.pushButton_4.clicked.connect(self.choise_file_dec)
        self.pushButton_5.clicked.connect(self.choise_key)

    def dec(self):
        if self.path_key != '' and self.path_file != '':
            dec_aes = Aes(000)
            text_decript = dec_aes.dec_aes_file(self.path_key, self.path_file)
            open('Decript_message.txt', 'w').write(text_decript)

    def beak_to_my_widg(self):
        self.mywidget = MyWidget()
        self.mywidget.show()
        self.close()

    def choise_file_dec(self):
        self.path_file = QFileDialog.getOpenFileName(self, 'Выбрать зашифрованный файл', '', '(*.bin)')[0]

    def choise_key(self):
        self.path_key = QFileDialog.getOpenFileName(self, 'Выбрать файл с ключем', '', 'Ключ шифрования (*.bin)')[0]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
