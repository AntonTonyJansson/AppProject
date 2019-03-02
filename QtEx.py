# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtEx.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox, QDialogButtonBox, QMainWindow, QHBoxLayout, QVBoxLayout, QApplication, \
    QWidget, QGridLayout, QPushButton, QCheckBox, QFrame, QSpacerItem, QSizePolicy, QRadioButton, QLabel, QLineEdit,\
    QMenuBar, QMenu, QStatusBar, QAction
from PyQt5.QtCore import QMetaObject, QRect, QCoreApplication, pyqtSignal, Qt
from QtEx2 import Ui_MainWindow2
import os

class FirstMainWindow(QMainWindow):

    def closeEvent(self, event):
        result = QMessageBox.question(self,
                                            "Confirm Exit...",
                                            "Are you sure you want to exit ?",
                                            QMessageBox.Yes | QMessageBox.No)
        event.ignore()
        if result == QMessageBox.Yes:
            try:
                ui.window
            except:
                pass
            else:
                ui.window.close()

            event.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


class Ui_MnWndw_1(object):

    def __init__(self):
        # Define initial object attributes
        # Empty lineedit
        self.txt = ""
        # Default number of terms
        self.s = 2

    def openWindow(self, subject, s):
        '''
        :param subject: str: Determine which subject to study
        :param s: int: determine number of terms
        '''
        self.window = QMainWindow()
        self.ui = Ui_MainWindow2(subject, s)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MnWndw_1):
        # Set layout for Mainwindow, including widgets
        # Main window
        MnWndw_1.setObjectName("MnWndw_1")
        MnWndw_1.resize(543, 434)
        self.cntrlWdgt = QWidget(MnWndw_1)
        self.cntrlWdgt.setObjectName("cntrlWdgt")
        self.grdLO_1 = QGridLayout(self.cntrlWdgt)
        self.grdLO_1.setObjectName("grdLO_1")

        # Insert widgets
        # Dialog button box, left down corner
        self.btnBx = QDialogButtonBox(self.cntrlWdgt)
        self.btnBx.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.btnBx.setObjectName("btnBx")
        self.grdLO_1.addWidget(self.btnBx, 2, 1, 1, 1)
        self.HLO_3 = QHBoxLayout()
        self.HLO_3.setObjectName("HLO_3")
        # Add left push button
        self.pshBtn_2 = QPushButton(self.cntrlWdgt)
        self.pshBtn_2.setObjectName("pshBtn_2")
        self.HLO_3.addWidget(self.pshBtn_2)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ChkBx = QCheckBox(self.cntrlWdgt)
        self.ChkBx.setObjectName("ChkBx")
        self.verticalLayout_3.addWidget(self.ChkBx)
        self.ChkBx_2 = QCheckBox(self.cntrlWdgt)
        self.ChkBx_2.setObjectName("ChkBx_2")
        self.verticalLayout_3.addWidget(self.ChkBx_2)
        self.ChkBx_3 = QCheckBox(self.cntrlWdgt)
        self.ChkBx_3.setObjectName("ChkBx_3")
        self.verticalLayout_3.addWidget(self.ChkBx_3)
        self.ChkBx_4 = QCheckBox(self.cntrlWdgt)
        self.ChkBx_4.setObjectName("ChkBx_4")
        self.verticalLayout_3.addWidget(self.ChkBx_4)
        self.line = QFrame(self.cntrlWdgt)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.ChkBx_5 = QCheckBox(self.cntrlWdgt)
        self.ChkBx_5.setObjectName("ChkBx_5")
        self.verticalLayout_3.addWidget(self.ChkBx_5)
        self.HLO_3.addLayout(self.verticalLayout_3)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.HLO_3.addItem(spacerItem)
        self.grdLO_2 = QGridLayout()
        self.grdLO_2.setObjectName("grdLO_2")
        self.RadBtn_5 = QRadioButton(self.cntrlWdgt)
        self.RadBtn_5.setObjectName("RadBtn_5")
        self.grdLO_2.addWidget(self.RadBtn_5, 2, 1, 1, 1)
        self.RadBtn_4 = QRadioButton(self.cntrlWdgt)
        self.RadBtn_4.setObjectName("RadBtn_4")
        self.grdLO_2.addWidget(self.RadBtn_4, 4, 1, 1, 1)
        self.pshBtn = QPushButton(self.cntrlWdgt)
        self.pshBtn.setObjectName("pshBtn")
        self.grdLO_2.addWidget(self.pshBtn, 0, 0, 1, 1)
        self.RadBtn_2 = QRadioButton(self.cntrlWdgt)
        self.RadBtn_2.setObjectName("RadBtn_2")
        self.grdLO_2.addWidget(self.RadBtn_2, 0, 1, 1, 1)
        self.RadBtn_3 = QRadioButton(self.cntrlWdgt)
        self.RadBtn_3.setObjectName("RadBtn_3")
        self.grdLO_2.addWidget(self.RadBtn_3, 1, 1, 1, 1)
        self.RadBtn = QRadioButton(self.cntrlWdgt)
        self.RadBtn.setObjectName("RadBtn")
        self.grdLO_2.addWidget(self.RadBtn, 3, 1, 1, 1)
        self.HLO_3.addLayout(self.grdLO_2)
        self.grdLO_1.addLayout(self.HLO_3, 1, 1, 1, 1)
        self.HLO_4 = QHBoxLayout()
        self.HLO_4.setObjectName("HLO_4")
        self.lbl_2 = QLabel(self.cntrlWdgt)
        self.lbl_2.setObjectName("lbl_2")
        self.HLO_4.addWidget(self.lbl_2)
        self.lbl = QLabel(self.cntrlWdgt)
        self.lbl.setObjectName("lbl")
        self.HLO_4.addWidget(self.lbl)
        self.grdLO_1.addLayout(self.HLO_4, 0, 1, 1, 1)
        self.lineEdit = QLineEdit(self.cntrlWdgt)
        self.lineEdit.setObjectName("lineEdit")
        self.grdLO_1.addWidget(self.lineEdit, 3, 1, 1, 1)
        MnWndw_1.setCentralWidget(self.cntrlWdgt)
        self.menubar = QMenuBar(MnWndw_1)
        self.menubar.setGeometry(QRect(0, 0, 543, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MnWndw_1.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MnWndw_1)
        self.statusbar.setObjectName("statusbar")
        MnWndw_1.setStatusBar(self.statusbar)
        self.actionExit = QAction(MnWndw_1)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MnWndw_1)
        self.ChkBx_5.toggled['bool'].connect(self.ChkBx_4.setChecked)
        self.ChkBx_5.toggled['bool'].connect(self.ChkBx_3.setChecked)
        self.ChkBx_5.toggled['bool'].connect(self.ChkBx_2.setChecked)
        self.ChkBx_5.toggled['bool'].connect(self.ChkBx.setChecked)
        self.btnBx.accepted.connect(self.lineEdit.clear)
        QMetaObject.connectSlotsByName(MnWndw_1)

    def retranslateUi(self, MnWndw_1):
        _translate = QCoreApplication.translate
        MnWndw_1.setWindowTitle(_translate("MnWndw_1", "ExampleProject"))
        self.pshBtn_2.setText(_translate("MnWndw_1", "Lock choice"))
        self.ChkBx.setText(_translate("MnWndw_1", "Division"))
        self.ChkBx_2.setText(_translate("MnWndw_1", "Multiplication"))
        self.ChkBx_3.setText(_translate("MnWndw_1", "Subtraktion"))
        self.ChkBx_4.setText(_translate("MnWndw_1", "Addition"))
        self.ChkBx_5.setText(_translate("MnWndw_1", "Check all"))
        self.RadBtn_5.setText(_translate("MnWndw_1", "3"))
        self.RadBtn_4.setText(_translate("MnWndw_1", "5"))
        self.pshBtn.setText(_translate("MnWndw_1", "Lock choice"))
        self.RadBtn_2.setText(_translate("MnWndw_1", "1"))
        self.RadBtn_3.setText(_translate("MnWndw_1", "2"))
        self.RadBtn.setText(_translate("MnWndw_1", "4"))
        self.lbl_2.setText(_translate("MnWndw_1", "Select subject"))
        self.lbl.setText(_translate("MnWndw_1", "Select difficulty"))
        self.menuFile.setTitle(_translate("MnWndw_1", "File"))
        self.actionExit.setText(_translate("MnWndw_1", "Exit"))

        # LineEdit signals
        self.btnBx.accepted.connect(lambda: self.txtAtt(self.lineEdit.text()))
        self.btnBx.rejected.connect(lambda: self.lineEdit.setText(""))

        # Radiobutton signals
        self.RadBtn.clicked.connect(lambda: self.sizing(self.RadBtn.text()))
        self.RadBtn_5.clicked.connect(lambda: self.sizing(self.RadBtn_5.text()))
        self.RadBtn_4.clicked.connect(lambda: self.sizing(self.RadBtn_4.text()))
        self.RadBtn_2.clicked.connect(lambda: self.sizing(self.RadBtn_2.text()))
        self.RadBtn_3.clicked.connect(lambda: self.sizing(self.RadBtn_3.text()))

        # Checkboxes signals
        self.ChkBx_5.toggled['bool'].connect(lambda: self.lineEdit.setText(self.txt))
        self.ChkBx_4.toggled['bool'].connect(lambda: self.openWindow(self.ChkBx_4.text(), self.s))
        self.ChkBx_3.toggled['bool'].connect(lambda: self.openWindow(self.ChkBx_3.text(), self.s))
        self.ChkBx_2.toggled['bool'].connect(lambda: self.openWindow(self.ChkBx_2.text(), self.s))
        self.ChkBx.toggled['bool'].connect(lambda: self.openWindow(self.ChkBx.text(), self.s))


        QMetaObject.connectSlotsByName(MnWndw_1)

    def txtAtt(self, txt):
        self.txt = txt
        fn = "tstfile" + ".txt"
        if fn not in os.listdir():
            f = open(fn, "w+")
        else:
            a = input("Do you want to overwrite file?").lower()
            if a == 'y':
                f = open(fn, "w+")
        with open(fn, "a") as f:
            f.write(txt + "\n")

    def sizing(self, s):
        self.s = int(s)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MnWndw_1 = FirstMainWindow()
    ui = Ui_MnWndw_1()
    ui.setupUi(MnWndw_1)
    MnWndw_1.show()
    sys.exit(app.exec_())

