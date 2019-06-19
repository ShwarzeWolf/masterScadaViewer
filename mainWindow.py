from PyQt5 import QtWidgets
from App import Ui_MainWindow
from PyQt5.QtWidgets import QGridLayout, QWidget, QTableWidget, QFileDialog, QTableWidgetItem
import Logic

class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.logic = Logic.Logic()

        self.showDialog()
        self.showListOfConnectedDatabases()

    def showDialog(self):
        directoryName = QFileDialog.getExistingDirectory(self, 'Choose working directory')
        self.logic.connectToDatabasesInDirectory(directoryName)

    def showListOfConnectedDatabases(self):
        self.logic.loadDatabasesNames(self.ui.databaseList)
        self.ui.layout.addWidget(self.ui.databaseList)

        self.ui.databaseList.itemDoubleClicked.connect(self.loadTablesFromDB)

    def loadTablesFromDB(self, chosenDB):
        self.ui.tablesFromDb = QTableWidget()
        self.logic.loadTablesNames(chosenDB.text(), self.ui.tablesFromDb)

        self.ui.layout.addWidget(self.ui.tablesFromDb)

    '''
    def loadAlarmsTable(self):
        table = QTableWidget(self)

        table = self.logic.loadAlarmsTable(table)

        self.ui.tabsMenu.addTab(table, "Alarms")

    def loadDataTables(self):
        table = QTableWidget(self)

        table = self.logic.loadAlarmsTable(table)
        self.ui.tabsMenu.addTab(table, "Data")

    '''

