from PyQt5 import QtWidgets
from App import Ui_MainWindow
from PyQt5.QtWidgets import QGridLayout, QWidget, QTableWidget, QTableWidgetItem
import DBConnectorAPI
def parseTime(timeStr):
    try:
        data, time = timeStr.split()
        time = time.split('.')[0]
    except:
        time = ""

    return "    " + time + "    "

class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dbcAPI = DBConnectorAPI.DBCOnnectorAPI()

        self.loadAlarmsTable()
        self.loadDBTables("ALARMS")

    def loadAlarmsTable(self):
        table = QTableWidget(self)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Начало", "Конец",  "Сообщение"])

        table.horizontalHeaderItem(0).setToolTip("InputTime")
        table.horizontalHeaderItem(1).setToolTip("OutputTime")
        table.horizontalHeaderItem(2).setToolTip("Message")

        self.ui.tabsMenu.addTab(table, "Alarms")

        queryResult = self.dbcAPI.getAlarms()

        rowPosition = 0

        for row in queryResult.itermap():
           table.insertRow(rowPosition)

           table.setItem(rowPosition, 0, QTableWidgetItem(parseTime("%(ACTIVETIME)s   " %row)))
           table.setItem(rowPosition, 1, QTableWidgetItem(parseTime("%(INACTIVETIME)s   " % row)))
           table.setItem(rowPosition, 2, QTableWidgetItem('%(MESSAGE)s   ' %row))

           rowPosition += 1

        table.resizeColumnsToContents()

    def loadDBTables(self, DBAlias):
        tablesNames = self.dbcAPI.getTablesNamesFromDatabase(DBAlias)

        for tableName in tablesNames:
            tableName = "".join(tableName)

            tableColumns = self.dbcAPI.getColumnsNamesFromTable(DBAlias, tableName)

            table = QTableWidget(self)
            table.setColumnCount(len(tableColumns))

            i = 0
            headerLabels = []

            for column in tableColumns:
                headerLabels.append("".join(column))
                #table.horizontalHeaderItem(i).setToolTip("".join(column))
                i = i + 1


            table.setHorizontalHeaderLabels(headerLabels)
            table.resizeColumnsToContents()

            self.ui.tabsMenu.addTab(table, "also Alarms")
        '''    
        table.setHorizontalHeaderLabels(["Начало", "Конец", "Сообщение"])

        table.horizontalHeaderItem(0).setToolTip("InputTime")
        table.horizontalHeaderItem(1).setToolTip("OutputTime")
        table.horizontalHeaderItem(2).setToolTip("Message")
        '''
        '''
        queryResult = self.dbconnector.getAlarms()

        rowPosition = 0

        for row in queryResult.itermap():
            table.insertRow(rowPosition)

            table.setItem(rowPosition, 0, QTableWidgetItem(parseTime("%(ACTIVETIME)s   " % row)))
            table.setItem(rowPosition, 1, QTableWidgetItem(parseTime("%(INACTIVETIME)s   " % row)))
            table.setItem(rowPosition, 2, QTableWidgetItem('%(MESSAGE)s   ' % row))

            rowPosition += 1

        table.resizeColumnsToContents()
        '''




