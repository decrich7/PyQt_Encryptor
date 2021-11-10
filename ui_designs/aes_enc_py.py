# -*- coding: utf-8 -*-




from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowAesEnc(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QPushButton {\n"
" background: #01040f;\n"
"    padding: 20px 30px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    border-radius: 20px;\n"
"    margin: 4px 2px;\n"
"    border: 1px solid #0bd42c;\n"
"\n"
"}\n"
"QMainWindow {\n"
" background: #000;\n"
"\n"
"}\n"
"QLabel {\n"
" background: #000;\n"
"color: #064f15;\n"
"font-size: 17px;\n"
" font-weight: bold;\n"
"\n"
"}\n"
"\n"
"QSpinBox {\n"
" background: #1b4725;\n"
" border-radius: 7px;\n"
" font-weight: bold;\n"
" font-size: 23px;\n"
"\n"
"}\n"
"\n"
"QRadioButton {\n"
" background: #000;\n"
" border-radius: 7px;\n"
" font-weight: bold;\n"
" font-size: 15px;\n"
"color: #1b4725;\n"
"}\n"
"\n"
"QTextEdit {\n"
" background: #6e9c78;\n"
" border-radius: 7px;\n"
" font-weight: bold;\n"
" font-size: 13px;\n"
"color: #fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 311, 41))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 400, 281, 41))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 250, 221, 81))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 450, 361, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 70, 361, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 510, 131, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 510, 171, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 180, 141, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 141, 51))
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 300, 351, 51))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 161, 31))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите текст:"))
        self.label_3.setText(_translate("MainWindow", "Зашифрованный текст:"))
        self.pushButton.setText(_translate("MainWindow", "Зашифровать"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:13px; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))
        self.pushButton_3.setText(_translate("MainWindow", "Главное меню"))
        self.radioButton_3.setText(_translate("MainWindow", "256"))
        self.radioButton_2.setText(_translate("MainWindow", "128"))
        self.label_2.setText(_translate("MainWindow", "Длинна ключа:"))
        self.label_4.setText(_translate("MainWindow", "Ключ:"))
