from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from encryption_algorithms.caesar_cipher import Caesar

form_ceasar_dec, base_ceasar_dec = uic.loadUiType('ui_designs/caesar_dec.ui')


class WindowCaesarDec(form_ceasar_dec, base_ceasar_dec):
    def __init__(self):
        super(base_ceasar_dec, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encrypt)
        # self.pushButton_2.clicked.connect(self.beak_to_alg_dec)

    # def beak_to_alg_dec(self):
    #     self.Algdec = AlgoritmDecript()
    #     self.Algdec.show()
    #     self.close()

    def encrypt(self):
        text_enc = self.textEdit_2.toPlainText()
        key = self.spinBox.value()
        if text_enc != '' and key <= 33:
            enc = Caesar(key, text_enc)
            self.textEdit.setText(enc.dec())
