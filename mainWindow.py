from PyQt5 import QtWidgets
from App import Ui_MainWindow
from PyQt5.QtWidgets import QGridLayout, QWidget, QTableWidget, QTableWidgetItem
import DBConnector

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

        self.dbconnector = DBConnector.DBConnector()
        self.dbconnector.connectAll()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.loadAlarmsTable()
        self.loadDBTable("alarms")

    def loadAlarmsTable(self):
        table = QTableWidget(self)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Начало", "Конец",  "Сообщение"])

        table.horizontalHeaderItem(0).setToolTip("InputTime")
        table.horizontalHeaderItem(1).setToolTip("OutputTime")
        table.horizontalHeaderItem(2).setToolTip("Message")

        self.grid_layout.addWidget(table, 0, 0)

        queryResult = self.dbconnector.getAlarms()

        rowPosition = 0

        for row in queryResult.itermap():
           table.insertRow(rowPosition)

           table.setItem(rowPosition, 0, QTableWidgetItem(parseTime("%(ACTIVETIME)s   " %row)))
           table.setItem(rowPosition, 1, QTableWidgetItem(parseTime("%(INACTIVETIME)s   " % row)))
           table.setItem(rowPosition, 2, QTableWidgetItem('%(MESSAGE)s   ' %row))

           rowPosition += 1

        table.resizeColumnsToContents()

    def loadDBTable(self, DBAlias):
        tablesNames = self.dbconnector.getTablesFromDatabase(DBAlias)

        for table in tablesNames:
            table = "".join(table)
            print(table)
            # print(self.getDataFromTable(DBAlias, table))

        '''
        table = QTableWidget(self)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Начало", "Конец", "Сообщение"])

        table.horizontalHeaderItem(0).setToolTip("InputTime")
        table.horizontalHeaderItem(1).setToolTip("OutputTime")
        table.horizontalHeaderItem(2).setToolTip("Message")

        self.grid_layout.addWidget(table, 0, 0)

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



