# -*- coding: utf-8 -*-
import base64
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialogButtonBox, QColorDialog, QPushButton, QInputDialog
from untitled import Ui_MainWindow
import sys


class testDialog(QtWidgets.QDialog):
    def __init_(self, parent=None):
        self.init_ui()

    def init_ui(self):
        buttonBox = QMessageBox()
        buttonBox.setWindowTitle('Сохранение ключа')
        buttonBox.setText("вапвапвап")
        buttonBox.setIcon(QMessageBox.Warning)
        buttonBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        buttonBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = testDialog()
    ex.show()
    sys.exit(app.exec_())
