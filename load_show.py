import math
import sys
import re
from importlib import reload
import Levenshtein

import PyQt5
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWheelEvent
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow as QMainWindow, QFrame, QTableWidget, QTableWidgetItem, QAction, QFileDialog
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, \
    QRadioButton, QHBoxLayout

import ui_mainWindow
import pandas as pd


class MainWindow(QMainWindow, ui_mainWindow.Ui_MainWindow):

    def updateTable(self, dataframe):
        self.ui.CsvVisualizer.blockSignals(True)

        print(dataframe.columns.values)
        self.df_cols = len(dataframe.columns)
        self.df_rows = len(dataframe.index)
        self.ui.CsvVisualizer.setRowCount(self.df_rows)
        self.ui.CsvVisualizer.setColumnCount(self.df_cols+1)
        for i in range(self.df_rows):
            for j in range(self.df_cols):
                x = '{}'.format(dataframe.iloc[i, j])
                self.ui.CsvVisualizer.setItem(i, j, QTableWidgetItem(x))
            x = str(dataframe.index.values[i])
            item = QTableWidgetItem(x)
            item.setFlags(QtCore.Qt.NoItemFlags)# | QtCore.Qt.ItemIsSelectable)
            self.ui.CsvVisualizer.setItem(i, self.df_cols, item)
        columns=[]
        for c in dataframe.columns:
            columns.append(c)
        columns.append("index")
        self.ui.CsvVisualizer.setHorizontalHeaderLabels(columns)
        self.ui.CsvVisualizer.blockSignals(False)

    def createTable(self):
        fname, something = QFileDialog.getOpenFileName(self, 'Open file', '', "Xlsx files (*.xlsx)")
        if fname:
            self.data_file = fname
        else:
            return
        self.df = pd.read_excel(self.data_file, sheet_name=0)
        self.updateTable(self.df)

    def new_option(self):
        new_item = self.ui.AddOption.toPlainText()
        if new_item != "":
            items = filter(None, re.split("[,\n]+", new_item))
            for i in items:
                stripped = i.strip()
                if stripped not in self.items:
                    self.items.add(stripped)
                    self.ui.ListSelector.addItem(stripped)

    def RemoveOption(self):
        remove = self.ui.ListSelector.selectedItems()
        for i in remove:
            if i.text() in self.items:
                self.items.remove(i.text())
        self.ui.ListSelector.clear()
        self.ui.ListSelector.addItems(self.items)

    def ClearOptions(self):
        self.ui.ListSelector.clear()

    def LoadOptions(self):
        col = self.ui.CsvVisualizer.currentColumn()
        uniques = set()
        uniques.clear()
        for i in range(self.df_rows):
            splitted = str(self.df.iloc[i, col]).split(',')
            for s in splitted:
                uniques.add(s.strip())
        if '' in uniques:
            uniques.remove('')
        if "" in uniques:
            uniques.remove("")
        self.items = uniques
        self.ui.ListSelector.clear()
        self.ui.ListSelector.addItems(self.items)
        self.ui.ListSelector.sortItems()

    def writeValues(self):
        val = ""
        sep = ""
        if len(self.ui.ListSelector.selectedItems()) == 0:
            return
        if len(self.ui.CsvVisualizer.selectedIndexes()) == 0:
            return
        for i in self.ui.ListSelector.selectedItems():
            if i != "":
                val = val + sep + i.text()
                sep = ", "
        for cell in self.ui.CsvVisualizer.selectedItems():
            cell.setText(val)
        self.ui.ListSelector.clearSelection()
        row = self.ui.CsvVisualizer.currentRow()
        col = self.ui.CsvVisualizer.currentColumn()
        if len(self.ui.CsvVisualizer.selectedItems()) == 1:
            self.ui.CsvVisualizer.setCurrentCell(row+1, col)

    def applyFilter(self):
        categories = [str(self.ui.ListSelector.item(i).text()).strip() for i in range(self.ui.ListSelector.count())]

        print(categories)
        selected_col = self.ui.CsvVisualizer.currentColumn()
        filtered_index = ~self.df[self.df.columns[selected_col]].isin(categories)
        filter_nan = False
        if "nan" in categories:
            filter_nan = True
        filtered_index = ~self.df[self.df.columns[selected_col]].apply(
            lambda x: bool((str(x) != "nan" and all(elem.strip() in categories for elem in x.split(","))) or (str(x) == "nan" and filter_nan)))
        filtered_df = self.df[filtered_index]
        self.updateTable(filtered_df)

    def restoreAll(self):
        self.updateTable(self.df)

    def filterValues(self):
        if self.ui.FilterBox.isChecked():
            self.applyFilter()
        else:
            self.restoreAll()

    def UpdateDataframe(self, row, col):
        real_row = int(self.ui.CsvVisualizer.item(row, self.df_cols).text())
        self.df.iloc[real_row, col] = self.ui.CsvVisualizer.item(row, col).text()

    def SaveFile(self):
        fname, something = QFileDialog.getSaveFileName(self, 'Save file', '', "Xlsx files (*.xlsx)")
        if fname:
            self.data_file = fname
        else:
            return
        self.df.to_excel(self.data_file, index_label=None)

    def ProcessFileMenu(self, action):
        if action == self.ui.actionOpen:
            self.createTable()
        if action == self.ui.actionSave:
            self.SaveFile()

    def DeselectAllOptions(self):
        self.ui.ListSelector.clearSelection()

    def ProcessCategoryMenu(self, action):
        if action == self.ui.actionConfirm_and_write:
            self.writeValues()
        if action == self.ui.actionAdd_options:
            self.new_option()
        if action == self.ui.actionLoad_from_column:
            self.LoadOptions()
        if action == self.ui.actionRemove_options:
            self.RemoveOption()
        if action == self.ui.actionHide_good_ones:
            self.ui.FilterBox.toggle()
        if action == self.ui.actionDeselect_All:
            self.DeselectAllOptions()

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() == QtCore.Qt.ControlModifier:
            self.font_size = self.font_size + event.angleDelta().y()/3
            if self.font_size < 5:
                self.font_size = 5
            fnt = self.ui.CsvVisualizer.font()
            fnt.setPointSize(self.font_size)
            self.ui.CsvVisualizer.setFont(fnt)
        else:
            event.ignore()

    def eventFilter(self, obj, event):
        if obj.objectName() == "ListSelector":
            if event.type() == QtCore.QEvent.KeyPress:
                if event.modifiers() == QtCore.Qt.ControlModifier and event.key() == Qt.Key_C:
                    QtGui.QClipboard.clear(QApplication.clipboard(), mode=QtGui.QClipboard.Clipboard)
                    output = '\n'.join(s.text() for s in self.ui.ListSelector.selectedItems())
                    QtGui.QClipboard.setText(QApplication.clipboard(), output, mode=QtGui.QClipboard.Clipboard)
                    return True
        return False

    def computeFancy(self):
        if not self.fancy_suggestion:
            return
        if self.ui.CsvVisualizer.currentItem() is None:
            return
        self.ui.ListSelector.clearSelection()
        value = str(self.ui.CsvVisualizer.currentItem().text())
        words = filter(None, re.split("[, ]+", value))

        words_l = set()
        for w in words:
            words_l.add(w)
        print('number of comparison: {}'.format(str(self.ui.ListSelector.count())))
        for c in range(self.ui.ListSelector.count()):
            print(c)
            c_text = self.ui.ListSelector.item(c).text()
            for w in words_l:
                print('comparing {} {}'.format(w, c_text))
                if Levenshtein.distance(w, c_text) < 3:
                    self.ui.ListSelector.item(c).setSelected(True)

    def enableFancy(self):
        self.fancy_suggestion = self.ui.EnableFancy.isChecked()

    def __init__(self):
        """ Initialization
        Parameters
        ----------
        """

        self.fancy_suggestion = False
        self.items = set()
        self.df = None
        self.df_cols = 1
        self.df_rows = 1
        self.font_size = 12

        # Base class
        QMainWindow.__init__(self)

        # Initialize the UI widgets
        self.ui = ui_mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.data_file = "data.csv"
        self.ui.menuCategories.triggered[QAction].connect(self.ProcessCategoryMenu)
        self.ui.menuOpenFile.triggered[QAction].connect(self.ProcessFileMenu)

        self.ui.ConfirmButton.clicked.connect(self.writeValues)
        self.ui.AddButton.clicked.connect(self.new_option)
        self.ui.FilterBox.stateChanged.connect(self.filterValues)
        self.ui.LoadOptions.clicked.connect(self.LoadOptions)
        self.ui.RemoveOption.clicked.connect(self.RemoveOption)
        self.ui.ClearOption.clicked.connect(self.ClearOptions)
        self.ui.CsvVisualizer.cellChanged.connect(self.UpdateDataframe)
        self.ui.DeselectButton.clicked.connect(self.DeselectAllOptions)
        self.ui.EnableFancy.stateChanged.connect(self.enableFancy)
        self.ui.CsvVisualizer.itemSelectionChanged.connect(self.computeFancy)
        self.ui.splitter.setStretchFactor(1, 0)

        self.ui.ListSelector.installEventFilter(self)


def main():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    app.exec_()


if __name__ == '__main__':
    main()
