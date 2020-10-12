# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.CsvVisualizer = QtWidgets.QTableWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.CsvVisualizer.sizePolicy().hasHeightForWidth())
        self.CsvVisualizer.setSizePolicy(sizePolicy)
        self.CsvVisualizer.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.CsvVisualizer.setTextElideMode(QtCore.Qt.ElideNone)
        self.CsvVisualizer.setRowCount(2)
        self.CsvVisualizer.setColumnCount(2)
        self.CsvVisualizer.setObjectName("CsvVisualizer")
        self.CsvVisualizer.horizontalHeader().setCascadingSectionResizes(True)
        self.verticalLayout_5.addWidget(self.CsvVisualizer)
        self.FilterBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.FilterBox.setObjectName("FilterBox")
        self.verticalLayout_5.addWidget(self.FilterBox)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.RemoveOption = QtWidgets.QPushButton(self.layoutWidget_2)
        self.RemoveOption.setObjectName("RemoveOption")
        self.horizontalLayout_7.addWidget(self.RemoveOption)
        self.LoadOptions = QtWidgets.QPushButton(self.layoutWidget_2)
        self.LoadOptions.setObjectName("LoadOptions")
        self.horizontalLayout_7.addWidget(self.LoadOptions)
        self.ClearOption = QtWidgets.QPushButton(self.layoutWidget_2)
        self.ClearOption.setObjectName("ClearOption")
        self.horizontalLayout_7.addWidget(self.ClearOption)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ListSelector = QtWidgets.QListWidget(self.layoutWidget_2)
        self.ListSelector.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.ListSelector.setObjectName("ListSelector")
        self.horizontalLayout_5.addWidget(self.ListSelector)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ConfirmButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.verticalLayout_2.addWidget(self.ConfirmButton)
        self.EnableFancy = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.EnableFancy.setObjectName("EnableFancy")
        self.verticalLayout_2.addWidget(self.EnableFancy)
        self.GreenButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.GreenButton.setStyleSheet("background-color: rgb(0, 230, 117);")
        self.GreenButton.setText("")
        self.GreenButton.setFlat(False)
        self.GreenButton.setObjectName("GreenButton")
        self.verticalLayout_2.addWidget(self.GreenButton)
        self.RedButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.RedButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.RedButton.setText("")
        self.RedButton.setObjectName("RedButton")
        self.verticalLayout_2.addWidget(self.RedButton)
        self.BlueButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.BlueButton.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.BlueButton.setText("")
        self.BlueButton.setObjectName("BlueButton")
        self.verticalLayout_2.addWidget(self.BlueButton)
        self.PurpleButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.PurpleButton.setStyleSheet("background-color: rgb(117, 80, 123);")
        self.PurpleButton.setText("")
        self.PurpleButton.setObjectName("PurpleButton")
        self.verticalLayout_2.addWidget(self.PurpleButton)
        self.YellowButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.YellowButton.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.YellowButton.setText("")
        self.YellowButton.setObjectName("YellowButton")
        self.verticalLayout_2.addWidget(self.YellowButton)
        self.DeselectButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.DeselectButton.setObjectName("DeselectButton")
        self.verticalLayout_2.addWidget(self.DeselectButton)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 1)
        self.verticalLayout_2.setStretch(7, 4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.AddOption = QtWidgets.QPlainTextEdit(self.layoutWidget_2)
        self.AddOption.setObjectName("AddOption")
        self.horizontalLayout_6.addWidget(self.AddOption)
        self.AddButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.AddButton.setObjectName("AddButton")
        self.horizontalLayout_6.addWidget(self.AddButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 22))
        self.menubar.setObjectName("menubar")
        self.menuOpenFile = QtWidgets.QMenu(self.menubar)
        self.menuOpenFile.setObjectName("menuOpenFile")
        self.menuCategories = QtWidgets.QMenu(self.menubar)
        self.menuCategories.setObjectName("menuCategories")
        self.menuEditing = QtWidgets.QMenu(self.menubar)
        self.menuEditing.setObjectName("menuEditing")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad_from_column = QtWidgets.QAction(MainWindow)
        self.actionLoad_from_column.setObjectName("actionLoad_from_column")
        self.actionRemove_options = QtWidgets.QAction(MainWindow)
        self.actionRemove_options.setObjectName("actionRemove_options")
        self.actionAdd_options = QtWidgets.QAction(MainWindow)
        self.actionAdd_options.setObjectName("actionAdd_options")
        self.actionConfirm_and_write = QtWidgets.QAction(MainWindow)
        self.actionConfirm_and_write.setObjectName("actionConfirm_and_write")
        self.actionHide_good_ones = QtWidgets.QAction(MainWindow)
        self.actionHide_good_ones.setObjectName("actionHide_good_ones")
        self.actionDeselect_All = QtWidgets.QAction(MainWindow)
        self.actionDeselect_All.setObjectName("actionDeselect_All")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.menuOpenFile.addAction(self.actionOpen)
        self.menuOpenFile.addAction(self.actionSave)
        self.menuOpenFile.addAction(self.actionSave_as)
        self.menuCategories.addAction(self.actionLoad_from_column)
        self.menuCategories.addAction(self.actionRemove_options)
        self.menuCategories.addAction(self.actionAdd_options)
        self.menuCategories.addSeparator()
        self.menuCategories.addAction(self.actionConfirm_and_write)
        self.menuCategories.addAction(self.actionDeselect_All)
        self.menuCategories.addSeparator()
        self.menuCategories.addAction(self.actionHide_good_ones)
        self.menuEditing.addAction(self.actionUndo)
        self.menuEditing.addAction(self.actionRedo)
        self.menubar.addAction(self.menuOpenFile.menuAction())
        self.menubar.addAction(self.menuCategories.menuAction())
        self.menubar.addAction(self.menuEditing.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FilterBox.setText(_translate("MainWindow", "Hide good ones"))
        self.RemoveOption.setText(_translate("MainWindow", "Remove options"))
        self.LoadOptions.setText(_translate("MainWindow", "Load from column"))
        self.ClearOption.setText(_translate("MainWindow", "Clear options"))
        self.ConfirmButton.setText(_translate("MainWindow", "Confirm and write"))
        self.EnableFancy.setText(_translate("MainWindow", "Enable fancy"))
        self.DeselectButton.setText(_translate("MainWindow", "Deselect"))
        self.AddButton.setText(_translate("MainWindow", "Add options"))
        self.menuOpenFile.setTitle(_translate("MainWindow", "Menu"))
        self.menuCategories.setTitle(_translate("MainWindow", "Categories"))
        self.menuEditing.setTitle(_translate("MainWindow", "Editing"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Alt+O"))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionLoad_from_column.setText(_translate("MainWindow", "Load from column"))
        self.actionLoad_from_column.setShortcut(_translate("MainWindow", "Alt+L"))
        self.actionRemove_options.setText(_translate("MainWindow", "Remove options"))
        self.actionRemove_options.setShortcut(_translate("MainWindow", "Alt+R"))
        self.actionAdd_options.setText(_translate("MainWindow", "Add options"))
        self.actionAdd_options.setShortcut(_translate("MainWindow", "Alt+A"))
        self.actionConfirm_and_write.setText(_translate("MainWindow", "Confirm and write"))
        self.actionConfirm_and_write.setShortcut(_translate("MainWindow", "Alt+C"))
        self.actionHide_good_ones.setText(_translate("MainWindow", "Hide good ones"))
        self.actionHide_good_ones.setShortcut(_translate("MainWindow", "Alt+H"))
        self.actionDeselect_All.setText(_translate("MainWindow", "Deselect All"))
        self.actionDeselect_All.setShortcut(_translate("MainWindow", "Alt+W"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))

