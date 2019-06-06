from PyQt5 import QtWidgets
import mainWindow
import sys
import fdb

#app = QtWidgets.QApplication([])
#application = mainWindow.mainwindow()
#application.show()

#sys.exit(app.exec())

#con = fdb.connect(dsn=r'C://Users/1358365/Desktop/работа/ALARMS.fdb', user='sysdba', password='masterkey')
con = fdb.connect(
    dsn='C://Users/1358365/Desktop/work/ALARMS.FDB',
    user='sysdba', password='masterkey',
    charset='UTF8'
  )

# Create a Cursor object that operates in the context of Connection con:
cur = con.cursor()

# Execute the SELECT statement:
cur.execute("select * from MASEVENTDATA")

# Retrieve all rows as a sequence and print that sequence:
print(cur.fetchall())