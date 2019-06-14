from PyQt5 import QtWidgets, QtGui, QtCore
from App import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QFileDialog
import fdb

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
        self.loadTable()

    def loadTable(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        table = QTableWidget(self)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Начало", "Конец",  "Сообщение"])

        table.horizontalHeaderItem(0).setToolTip("inputTime")
        table.horizontalHeaderItem(1).setToolTip("outputTime")
        table.horizontalHeaderItem(2).setToolTip("Message")

        grid_layout.addWidget(table, 0, 0)

        con = fdb.connect(
            dsn='C://Users/1358365/Desktop/work/ALARMS.FDB',
            user='sysdba', password='masterkey',
            charset='UTF8'
        )

        cur = con.cursor()
        cur.execute("select * from MASEVENTDATA")

        rowPosition = 0

        for row in cur.itermap():
           table.insertRow(rowPosition)

           table.setItem(rowPosition, 0, QTableWidgetItem(parseTime("%(ACTIVETIME)s   " %row)))
           table.setItem(rowPosition, 1, QTableWidgetItem(parseTime("%(INACTIVETIME)s   " % row)))
           table.setItem(rowPosition, 2, QTableWidgetItem('%(MESSAGE)s   ' %row))

           rowPosition += 1

        table.resizeColumnsToContents()

