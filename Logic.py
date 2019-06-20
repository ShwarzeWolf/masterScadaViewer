from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import DBConnectorAPI
import TableCreator
import os

class Logic:
    def __init__(self):
        self.dbcAPI = DBConnectorAPI.DBCOnnectorAPI()

    def connectToDBsInDirectory(self, directoryPath):
        listOfDatabases = []

        for filename in os.listdir(directoryPath):
            if filename.capitalize().endswith(".fdb"):
                listOfDatabases.append([directoryPath + '/' + filename, filename.split('.')[0]])

        self.dbcAPI.connectDatabases(listOfDatabases)

    def loadDBNames(self):
        dbNames = self.dbcAPI.getEstablishedConnectionsNames()
        return TableCreator.createTable(dbNames, "Databases")

    def loadTablesNames(self, dbAlias):
        tableNames = self.dbcAPI.getTablesNamesFromDB(dbAlias)
        return TableCreator.createTable(tableNames, dbAlias)

    def loadData(self, dbAlias, tableName):
        data = self.dbcAPI.getDataFromTable(dbAlias, tableName)
        dataColumns = self.dbcAPI.getColumnsNamesFromTable(dbAlias, tableName)
        return TableCreator.createTable(data, dataColumns)

    '''
    def loadAlarmsTable(self, table):
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Начало", "Конец",  "Сообщение"])

        table.horizontalHeaderItem(0).setToolTip("InputTime")
        table.horizontalHeaderItem(1).setToolTip("OutputTime")
        table.horizontalHeaderItem(2).setToolTip("Message")

        queryResult = self.dbcAPI.getAlarms()

        rowPosition = 0

        for row in queryResult.itermap():
           table.insertRow(rowPosition)

           table.setItem(rowPosition, 0, QTableWidgetItem(parseTime("%(ACTIVETIME)s   " %row)))
           table.setItem(rowPosition, 1, QTableWidgetItem(parseTime("%(INACTIVETIME)s   " % row)))
           table.setItem(rowPosition, 2, QTableWidgetItem('%(MESSAGE)s   ' %row))

           rowPosition += 1

        table.resizeColumnsToContents()

        return table

    def loadListOfTables(self, tab):
        tablesNames = self.dbcAPI.getTablesNamesFromDatabase()

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
    
        table.setHorizontalHeaderLabels(["Начало", "Конец", "Сообщение"])

        table.horizontalHeaderItem(0).setToolTip("InputTime")
        table.horizontalHeaderItem(1).setToolTip("OutputTime")
        table.horizontalHeaderItem(2).setToolTip("Message")
        
        
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


def parseDirectoryPath(dirStr):
    return dirStr.replace('/', '\\')
