# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabsOverview = QtWidgets.QTabWidget(self.centralwidget)
        self.tabsOverview.setObjectName("tabsOverview")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.locationLabel = QtWidgets.QLabel(self.tab)
        self.locationLabel.setObjectName("locationLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.locationLabel)
        self.locationComboBox = QtWidgets.QComboBox(self.tab)
        self.locationComboBox.setObjectName("locationComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.locationComboBox)
        self.labelLuc = QtWidgets.QLabel(self.tab)
        self.labelLuc.setObjectName("labelLuc")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelLuc)
        self.spinBoxLuc = QtWidgets.QSpinBox(self.tab)
        self.spinBoxLuc.setMaximum(677215)
        self.spinBoxLuc.setObjectName("spinBoxLuc")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxLuc)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tracksComboBox = QtWidgets.QComboBox(self.tab)
        self.tracksComboBox.setObjectName("tracksComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tracksComboBox)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.secondsSpinBox = QtWidgets.QSpinBox(self.tab)
        self.secondsSpinBox.setMaximum(2147483647)
        self.secondsSpinBox.setObjectName("secondsSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.secondsSpinBox)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.tabsOverview.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.labelCharacter1Name = QtWidgets.QLabel(self.tab_2)
        self.labelCharacter1Name.setObjectName("labelCharacter1Name")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelCharacter1Name)
        self.c1NameLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.c1NameLineEdit.setObjectName("c1NameLineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.c1NameLineEdit)
        self.labelCurrentHpChar1 = QtWidgets.QLabel(self.tab_2)
        self.labelCurrentHpChar1.setObjectName("labelCurrentHpChar1")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelCurrentHpChar1)
        self.labelMaxHpChar1 = QtWidgets.QLabel(self.tab_2)
        self.labelMaxHpChar1.setObjectName("labelMaxHpChar1")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelMaxHpChar1)
        self.spinBoxCurrentHpChar1 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBoxCurrentHpChar1.setMaximum(999)
        self.spinBoxCurrentHpChar1.setObjectName("spinBoxCurrentHpChar1")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxCurrentHpChar1)
        self.spinBoxMaxHpChar1 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBoxMaxHpChar1.setMaximum(999)
        self.spinBoxMaxHpChar1.setObjectName("spinBoxMaxHpChar1")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxMaxHpChar1)
        self.gridLayout_3.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.tabsOverview.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.labelCharacter2Name = QtWidgets.QLabel(self.tab_3)
        self.labelCharacter2Name.setObjectName("labelCharacter2Name")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelCharacter2Name)
        self.c2NameLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.c2NameLineEdit.setObjectName("c2NameLineEdit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.c2NameLineEdit)
        self.labelCurrentHpChar2 = QtWidgets.QLabel(self.tab_3)
        self.labelCurrentHpChar2.setObjectName("labelCurrentHpChar2")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelCurrentHpChar2)
        self.labelMaxHpChar2 = QtWidgets.QLabel(self.tab_3)
        self.labelMaxHpChar2.setObjectName("labelMaxHpChar2")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelMaxHpChar2)
        self.spinBoxCurrentHpChar2 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBoxCurrentHpChar2.setMaximum(999)
        self.spinBoxCurrentHpChar2.setObjectName("spinBoxCurrentHpChar2")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxCurrentHpChar2)
        self.spinBoxMaxHpChar2 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBoxMaxHpChar2.setMaximum(999)
        self.spinBoxMaxHpChar2.setObjectName("spinBoxMaxHpChar2")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxMaxHpChar2)
        self.gridLayout_4.addLayout(self.formLayout_4, 0, 0, 1, 1)
        self.tabsOverview.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.labelCharacter3Name = QtWidgets.QLabel(self.tab_4)
        self.labelCharacter3Name.setObjectName("labelCharacter3Name")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelCharacter3Name)
        self.c3NameLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.c3NameLineEdit.setObjectName("c3NameLineEdit")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.c3NameLineEdit)
        self.labelCurrentHpChar3 = QtWidgets.QLabel(self.tab_4)
        self.labelCurrentHpChar3.setObjectName("labelCurrentHpChar3")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelCurrentHpChar3)
        self.labelMaxHpChar3 = QtWidgets.QLabel(self.tab_4)
        self.labelMaxHpChar3.setObjectName("labelMaxHpChar3")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelMaxHpChar3)
        self.spinBoxCurrentHpChar3 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBoxCurrentHpChar3.setMaximum(999)
        self.spinBoxCurrentHpChar3.setObjectName("spinBoxCurrentHpChar3")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxCurrentHpChar3)
        self.spinBoxMaxHpChar3 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBoxMaxHpChar3.setMaximum(999)
        self.spinBoxMaxHpChar3.setObjectName("spinBoxMaxHpChar3")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxMaxHpChar3)
        self.gridLayout_5.addLayout(self.formLayout_5, 0, 0, 1, 1)
        self.tabsOverview.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.storageTableWidget = QtWidgets.QTableWidget(self.tab_5)
        self.storageTableWidget.setCornerButtonEnabled(True)
        self.storageTableWidget.setObjectName("storageTableWidget")
        self.storageTableWidget.setColumnCount(2)
        self.storageTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.storageTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.storageTableWidget.setHorizontalHeaderItem(1, item)
        self.storageTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.storageTableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.storageTableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.storageTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_6.addWidget(self.storageTableWidget, 0, 0, 1, 1)
        self.tabsOverview.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabsOverview, 0, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 0, 1, 1, QtCore.Qt.AlignRight)
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
        self.tabsOverview.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Seiken Densetsu 3 Save Editor"))
        self.locationLabel.setText(_translate("MainWindow", "Location"))
        self.labelLuc.setText(_translate("MainWindow", "Luc"))
        self.label.setText(_translate("MainWindow", "Playing track"))
        self.label_2.setText(_translate("MainWindow", "Playing time"))
        self.secondsSpinBox.setSuffix(_translate("MainWindow", " seconds"))
        self.tabsOverview.setTabText(self.tabsOverview.indexOf(self.tab), _translate("MainWindow", "General"))
        self.labelCharacter1Name.setText(_translate("MainWindow", "Name"))
        self.labelCurrentHpChar1.setText(_translate("MainWindow", "Current HP"))
        self.labelMaxHpChar1.setText(_translate("MainWindow", "Max HP"))
        self.tabsOverview.setTabText(self.tabsOverview.indexOf(self.tab_2), _translate("MainWindow", "Character 1"))
        self.labelCharacter2Name.setText(_translate("MainWindow", "Name"))
        self.labelCurrentHpChar2.setText(_translate("MainWindow", "Current HP"))
        self.labelMaxHpChar2.setText(_translate("MainWindow", "Max HP"))
        self.tabsOverview.setTabText(self.tabsOverview.indexOf(self.tab_3), _translate("MainWindow", "Character 2"))
        self.labelCharacter3Name.setText(_translate("MainWindow", "Name"))
        self.labelCurrentHpChar3.setText(_translate("MainWindow", "Current HP"))
        self.labelMaxHpChar3.setText(_translate("MainWindow", "Max HP"))
        self.tabsOverview.setTabText(self.tabsOverview.indexOf(self.tab_4), _translate("MainWindow", "Character 3"))
        item = self.storageTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item"))
        item = self.storageTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Amount"))
        self.tabsOverview.setTabText(self.tabsOverview.indexOf(self.tab_5), _translate("MainWindow", "Item Storage"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

