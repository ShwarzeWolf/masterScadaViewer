from PyQt5 import QtWidgets
import userAPI
import sys

app = QtWidgets.QApplication([])
application = userAPI.userAPI()
application.show()

sys.exit(app.exec())