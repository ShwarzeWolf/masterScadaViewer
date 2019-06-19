from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import DBConnectorAPI
import os

class Logic:
    def __init__(self):
        self.dbcAPI = DBConnectorAPI.DBCOnnectorAPI()

    def connectToDatabasesInDirectory(self, directoryPath):
        listOfDatabases = []

        for filename in os.listdir(directoryPath):
            if filename.capitalize().endswith(".fdb"):
                listOfDatabases.append([directoryPath + '/' + filename, filename.split('.')[0]])

        self.dbcAPI.connectDatabases(listOfDatabases)

    def loadDatabasesNames(self, table):
        dbNames = self.dbcAPI.getEstablishedConnectionsNames()

        table.setColumnCount(1)
        rowPosition = 0

        for name in dbNames:
            table.insertRow(rowPosition)
            table.setItem(rowPosition, 0, QTableWidgetItem(name))
            rowPosition += 1

        table.resizeColumnsToContents()


    def loadTablesNames(self, dbAlias, table):
        tablenames = self.dbcAPI.getTablesNamesFromDB(dbAlias)

        table.setColumnCount(1)
        rowPosition = 0


        for tableName in tablenames:
            tableName = "".join(tableName)
            table.insertRow(rowPosition)

            table.setItem(rowPosition, 0, QTableWidgetItem(tableName))
            rowPosition += 1

        table.resizeColumnsToContents()




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


def parseTime(timeStr):
    try:
        data, time = timeStr.split()
        time = time.split('.')[0]
    except:
        time = ""

    return "    " + time + "    "

def parseDirectoryPath(dirStr):
    return dirStr.replace('/', '\\')
