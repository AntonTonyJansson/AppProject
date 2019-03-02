# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrueOrFalse.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# Testing new branch, fourth try

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def __init__(self):
        self.quiz = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hLO = QtWidgets.QHBoxLayout(self.centralwidget)
        self.hLO.setObjectName("hLO")
        self.vLO = QtWidgets.QVBoxLayout()
        self.vLO.setObjectName("vLO")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setObjectName("createButton")
        self.vLO.addWidget(self.createButton)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setObjectName("editButton")
        self.vLO.addWidget(self.editButton)
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setObjectName("removeButton")
        self.vLO.addWidget(self.removeButton)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.vLO.addWidget(self.startButton)
        self.hLO.addLayout(self.vLO)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.model = QtGui.QStandardItemModel()
        files = []
        for f in os.listdir():
            try:
                ext = f.split('.')[1]
                if ext == 'txt':
                    files.append(f)
            except:
                continue
        for f in files:
            self.model.appendRow(QtGui.QStandardItem(f))
        self.listView.setModel(self.model)
        self.listView.setAlternatingRowColors(True)

        self.listView.clicked[QtCore.QModelIndex].connect(self.on_clicked)

        self.createButton.clicked.connect(self.create_clicked)
        self.editButton.clicked.connect(self.edit_clicked)
        self.removeButton.clicked.connect(self.remove_clicked)
        self.startButton.clicked.connect(self.start_clicked)

        self.hLO.addWidget(self.listView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.createButton.setText(_translate("MainWindow", "Create quiz"))
        self.editButton.setText(_translate("MainWindow", "Edit quiz"))
        self.removeButton.setText(_translate("MainWindow", "Remove quiz"))
        self.startButton.setText(_translate("MainWindow", "Start quiz"))

    def on_clicked(self, index):
        self.quiz  = self.model.itemFromIndex(index).text()
        self.quiz_index = self.model.itemFromIndex(index).index().row()

    def create_clicked(self):
        if self.quiz:
            print('create quiz clicked with file', self.quiz)

        else:
            print('no list selected')

    def edit_clicked(self):
        print('edit clicked with file', self.quiz)

    def remove_clicked(self):
        if self.quiz:
            result = QtWidgets.QMessageBox.question(MainWindow,
                                          "Confirm Deletion...",
                                          "Are you sure you want to delete quiz {}?".format(self.quiz),
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if result == QtWidgets.QMessageBox.Yes:
                print('remove clicked with file', self.quiz)
                os.remove(self.quiz)
                self.model.removeRow(self.quiz_index)
            else:
                print('Ok not removing')
        else:
            qtMB = QtWidgets.QMessageBox()
            qtMB.setWindowTitle("File input error")
            qtMB.setText("No quiz has been selected")
            qtMB.addButton(QtWidgets.QMessageBox.Ok)
            qtMB.exec()

    def start_clicked(self):
        print('start clicked with file', self.quiz)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

