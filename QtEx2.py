# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtEx2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

from snippets import ClickableLineEdit, FeedbackMessage

class Ui_MainWindow2(object):
    def __init__(self, subject, size):
        self.q = self.q_gen(subject, size)

    def q_gen(self, subject, size):
        a = (map(str, np.random.randint(10, size=size)))
        if subject == 'Addition':
            return '+'.join(a)
        elif subject == 'Subtraktion':
            return '-'.join(a)
        elif subject == 'Multiplication':
            return '*'.join(a)
        return '/'.join(a)

    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(550, 232)
        MainWindow2.setWindowIcon(QtGui.QIcon("C:/Users/anton/Skrivbord/greenTick.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = ClickableLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 26))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.buttonBox.accepted.connect(lambda: print(self.lineEdit.text()))

        self.a = eval(self.q)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)
        self.lineEdit.clicked.connect(self.t2)
        self.lineEdit.submit.connect(self.buttonBox.accepted)

        self.lineEdit.kill.connect(MainWindow2.close)

        self.buttonBox.accepted.connect(self.showFeedback)

        self.retranslateUi(MainWindow2)


    def copy_and_print(self):
        self.label.setText(self.lineEdit.text())

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.label.setText(_translate("MainWindow2", 'What is the answer to {} ?'.format(self.q)))
        self.lineEdit.setText(_translate("MainWindow2", "Type answer here"))
        font = QtGui.QFont("Times", 15, QtGui.QFont.StyleItalic)
        self.lineEdit.setFont(font)

    def t2(self):
        self.lineEdit.clear()
        self.lineEdit.clicked.disconnect()

    def showFeedback(self):
        self.Fdbk = FeedbackMessage((self.lineEdit.text(), self.a))
        print(self.Fdbk)
        self.Fdbk.next_q.connect(self.testing)

    def testing(self):
        print('det här funkar inte')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
