from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

def createTable(data):
    table = QTableWidget()

    table.setColumnCount(len(data[0]))
    rowPosition = 0

    for row in data:
        table.insertRow(rowPosition)

        row = "".join(row)

        table.setItem(rowPosition, 0, QTableWidgetItem(row))
        rowPosition += 1

    table.resizeColumnsToContents()

    return table
