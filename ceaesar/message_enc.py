from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from encryption_algorithms.caesar_cipher import Caesar

form_ceasar, base_ceasar = uic.loadUiType('ui_designs/caesar.ui')


class Window_Caesar(form_ceasar, base_ceasar):
    def __init__(self):
        super(base_ceasar, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encrypt)

    def encrypt(self):
        text_enc = self.textEdit_2.toPlainText()
        print(text_enc)
        key = self.spinBox.value()
        if text_enc != '' and key <= 33:
            enc = Caesar(key, text_enc)
            self.textEdit.setText(enc.cipher())
