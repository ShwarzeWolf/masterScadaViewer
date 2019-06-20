from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

def createTable(data, columnNames):
    table = QTableWidget()

    try:
        table.setColumnCount(len(data[0]))
    except:
        return table

    table.setHorizontalHeaderLabels(convertToList(columnNames))

    rowPosition = 0

    for row in data:
        table.insertRow(rowPosition)

        columnPosition = 0

        for item in row:
            try:
                item = QTableWidgetItem(str(row[columnPosition]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                table.setItem(rowPosition, columnPosition, item)
            except:
                table.setItem(rowPosition, columnPosition, QTableWidgetItem("NAN"))

            columnPosition += 1

        rowPosition += 1

    table.resizeColumnsToContents()
    table.resizeRowsToContents()

    return table


def parseTime(timeStr):
    try:
        data, time = timeStr.split()
        time = time.split('.')[0]
    except:
        time = ""

    return "    " + time + "    "

def convertToList(values):
    if type(values) == str:
        return values.split('@')
    elif type(values == tuple):
        vals = []
        for val in values:
            val = "".join(val)
            vals.append(val)
        return vals
    else:
        return values