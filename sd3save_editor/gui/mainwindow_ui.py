# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.locationLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.locationLabel.setObjectName("locationLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.locationLabel)
        self.locationComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.locationComboBox.setObjectName("locationComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.locationComboBox)
        self.labelCharacter1Name = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelCharacter1Name.setObjectName("labelCharacter1Name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelCharacter1Name)
        self.c1NameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.c1NameLineEdit.setObjectName("c1NameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.c1NameLineEdit)
        self.labelCharacter2Name = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelCharacter2Name.setObjectName("labelCharacter2Name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelCharacter2Name)
        self.c2NameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.c2NameLineEdit.setObjectName("c2NameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.c2NameLineEdit)
        self.labelCharacter3Name = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelCharacter3Name.setObjectName("labelCharacter3Name")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelCharacter3Name)
        self.c3NameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.c3NameLineEdit.setObjectName("c3NameLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.c3NameLineEdit)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setGeometry(QtCore.QRect(690, 530, 81, 22))
        self.saveButton.setObjectName("saveButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Seiken Densetsu 3 Save Editor"))
        self.locationLabel.setText(_translate("MainWindow", "Location"))
        self.labelCharacter1Name.setText(_translate("MainWindow", "Character 1 Name"))
        self.labelCharacter2Name.setText(_translate("MainWindow", "Character 2 Name"))
        self.labelCharacter3Name.setText(_translate("MainWindow", "Character 3 Name"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

