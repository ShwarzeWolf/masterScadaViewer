import fdb

class DBConnector:
    def __init__(self):
        self.connectionsList = []

    def createConnection(self, dbPath, DBalias):
        try:
            connection = fdb.connect(
                dsn=dbPath,
                user='sysdba', password='masterkey',
                charset='UTF8'
            )

            self.connectionsList.append([DBalias, connection])
            print("Connection " + DBalias + " established")

        except:
            print("Connection failed")

    def connectAll(self, pathDir = 'C://Users/1358365/Desktop/work/'):
        self.createConnection(pathDir + 'ALARMS.FDB', 'ALARMS')
        self.createConnection(pathDir + 'ACTIONS.FDB', 'ACTIONS')
        self.createConnection(pathDir + 'CALC_GPA.FDB', 'CALC_GPA')
        self.createConnection(pathDir + 'DATA_GPA.FDB', 'DATA_GPA')
        self.createConnection(pathDir + 'PROJECT.FDB', 'PROJECT_GPA')

    def getEstablishedConnection(self, alias):
        for connection in self.connectionsList:
            if connection[0] == alias:
                return connection[1]

    def executeStatement(self, DBalias, statement):
        connection = self.getEstablishedConnection(DBalias)

        cursor = connection.cursor()
        cursor.execute(statement)

        return cursor



