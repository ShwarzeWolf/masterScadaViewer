from PyQt5 import QtWidgets
from src.userInterface.App import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from src.DataProceedure import Logic
from functools import partial

class userAPI(QtWidgets.QMainWindow):
    def __init__(self):
        super(userAPI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.logic = Logic.Logic()

        self.showDialog()
        self.showListOfConnectedDBs()

    def showDialog(self):
        directoryName = QFileDialog.getExistingDirectory(self, 'Choose working directory')
        self.logic.connectToDBsInDirectory(directoryName)

    def showListOfConnectedDBs(self):
        table = self.logic.loadDBNames()
        table.itemDoubleClicked.connect(self.loadTablesFromDB)

        self.ui.tabBar.addTab(table, "DataBases")

    def loadTablesFromDB(self, chosenDB):
        table = self.logic.loadTablesNames(chosenDB.text())
        table.itemDoubleClicked.connect(partial(self.loadTable, chosenDB.text()))

        self.ui.tabBar.addTab(table, chosenDB.text())

    def loadTable(self, chosenDB, chosenTable):
        table = self.logic.loadData(chosenDB, chosenTable.text())
        self.ui.tabBar.addTab(table, chosenTable.text())
