import math
import sys
import re
from collections import deque
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
import logging
import logging.config


class History:
    def __init__(self):
        self.stack = deque(maxlen=10)

    def push(self, df):
        self.stack.append(df.copy())

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()


class MainWindow(QMainWindow, ui_mainWindow.Ui_MainWindow):

    def updateTable(self, dataframe):
        self.ui.CsvVisualizer.blockSignals(True)
        self.logger.debug(dataframe.columns.values)
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
            item.setFlags(QtCore.Qt.NoItemFlags) # | QtCore.Qt.ItemIsSelectable)
            self.ui.CsvVisualizer.setItem(i, self.df_cols, item)
        columns = []
        for c in dataframe.columns:
            columns.append(c)
        columns.append("index")
        self.ui.CsvVisualizer.setHorizontalHeaderLabels(columns)
        self.ui.CsvVisualizer.blockSignals(False)

    def createTable(self):
        f_name, something = QFileDialog.getOpenFileName(self, 'Open file', '', "Xlsx files (*.xlsx)")
        if f_name:
            self.ui.statusbar.showMessage("opening "+f_name, 3000)
        else:
            return
        self.df = pd.read_excel(f_name, sheet_name=0)
        self.ui.statusbar.showMessage(f_name + " opened", 3000)
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
        self.ui.ListSelector.setSortingEnabled(True)
        self.ui.ListSelector.sortItems()


    def RemoveOption(self):
        remove = self.ui.ListSelector.selectedItems()
        for i in remove:
            if i.text() in self.items:
                self.items.remove(i.text())
        self.ui.ListSelector.clear()
        self.ui.ListSelector.addItems(self.items)
        self.ui.statusbar.showMessage("Options removed", 3000)

    def ClearOptions(self):
        self.ui.ListSelector.clear()
        self.ui.statusbar.showMessage("Options cleared", 3000)

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
        self.ui.statusbar.showMessage("Loaded %s options"%str(len(uniques)), 3000)


    def writeValues(self):
        self.history.push(self.df)
        self.ui.CsvVisualizer.blockSignals(True)

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
            self.UpdateDataframeNoHistory(cell.row(), cell.column())
        self.ui.ListSelector.clearSelection()
        if len(self.ui.CsvVisualizer.selectedItems()) == 1:
            row = self.ui.CsvVisualizer.currentRow()
            col = self.ui.CsvVisualizer.currentColumn()
            self.ui.CsvVisualizer.setCurrentCell(row+1, col)
        self.ui.CsvVisualizer.blockSignals(False)

    def applyFilter(self):
        categories = [str(self.ui.ListSelector.item(i).text()).strip() for i in range(self.ui.ListSelector.count())]

        self.logger.debug(categories)
        selected_col = self.ui.CsvVisualizer.currentColumn()
        filter_nan = False
        if "nan" in categories:
            filter_nan = True
        filtered_index = ~self.df[self.df.columns[selected_col]].apply(
            lambda x: bool((str(x) != "nan" and all(elem.strip() in categories for elem in str(x).split(","))) or (str(x) == "nan" and filter_nan)))
        filtered_df = self.df[filtered_index]
        self.updateTable(filtered_df)
        self.ui.statusbar.showMessage("Applied visibility filter", 3000)

    def restoreAll(self):
        self.updateTable(self.df)
        self.ui.statusbar.showMessage("Restored full visibility", 3000)

    def filterValues(self):
        if self.ui.FilterBox.isChecked():
            self.applyFilter()
        else:
            self.restoreAll()

    def UpdateDataframe(self, row, col):
        self.history.push(self.df)
        self.UpdateDataframeNoHistory(row, col)

    def UpdateDataframeNoHistory(self, row, col):
        real_row = int(self.ui.CsvVisualizer.item(row, self.df_cols).text())
        self.df.iloc[real_row, col] = self.ui.CsvVisualizer.item(row, col).text()

    def SaveFile(self, find_name):
        if find_name or not self.data_file:
            f_name, something = QFileDialog.getSaveFileName(self, 'Save file', '', "Xlsx files (*.xlsx)")
            if f_name:
                self.data_file = f_name
            else:
                return
        self.df.to_excel(self.data_file, index_label=None)
        self.ui.statusbar.showMessage("Saved file "+self.data_file, 3000)

    def ProcessFileMenu(self, action):
        if action == self.ui.actionOpen:
            self.createTable()
        if action == self.ui.actionSave:
            self.SaveFile(False)
        if action == self.ui.actionSave_as:
            self.SaveFile(True)

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

    def ProcessEditingMenu(self, action):
        # push always K-1 before latest action,
        # save latest K inside redo
        # pop the state K-1 before latest
        if action == self.ui.actionUndo:
            old_df = self.history.pop()
            if old_df is not None:
                self.redo_history.push(self.df)
                self.df = old_df
                self.updateTable(self.df)
                self.ui.statusbar.showMessage("Undo done", 1000)
        # push always state K+1 inside redo
        # save current state K inside undo
        # pop latest state K+1
        if action == self.ui.actionRedo:
            new_df = self.redo_history.pop()
            if new_df is not None:
                self.history.push(self.df)
                self.df = new_df
                self.updateTable(self.df)
                self.ui.statusbar.showMessage("Redo done", 1000)

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() == QtCore.Qt.ControlModifier:
            self.font_size = self.font_size + event.angleDelta().y()/15
            if self.font_size < 5:
                self.font_size = 5
            #fnt = self.ui.CsvVisualizer.font()
            #fnt.setPointSize(self.font_size)
            #self.ui.CsvVisualizer.setFont(fnt)
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
        words = filter(None, re.split("[,]+", value))
        #self.logger.info('parsed words for fancy: ')
        #self.logger.info(' '.join(words))
        words_l = set()
        for w in words:
            words_l.add(w.strip())
        self.logger.debug('number of comparison: {}'.format(str(self.ui.ListSelector.count())))
        self.logger.debug('unique words for fancy: ')
        self.logger.debug(' '.join(words_l))
        for c in range(self.ui.ListSelector.count()):
            c_text = self.ui.ListSelector.item(c).text()
            for w in words_l:
                self.logger.debug('comparing {} {} with distance {}'.format(w, c_text, Levenshtein.distance(w, c_text)))
                if Levenshtein.distance(w, c_text) < round(0.4 + len(w)*0.2):
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
        self.history = History()
        self.redo_history = History()

        # Base class
        QMainWindow.__init__(self)

        # Initialize the UI widgets
        self.ui = ui_mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.data_file = None
        self.ui.menuCategories.triggered[QAction].connect(self.ProcessCategoryMenu)
        self.ui.menuOpenFile.triggered[QAction].connect(self.ProcessFileMenu)
        self.ui.menuEditing.triggered[QAction].connect(self.ProcessEditingMenu)

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
        self.logger = logging.getLogger('main_window')
        logging.basicConfig(filename='categorizer.log', level=logging.DEBUG)


def main():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    app.exec_()


if __name__ == '__main__':
    main()
