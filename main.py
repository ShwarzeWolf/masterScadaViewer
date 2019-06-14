from PyQt5 import QtWidgets
import mainWindow
import sys

app = QtWidgets.QApplication([])
application = mainWindow.mainwindow()
application.show()

sys.exit(app.exec())