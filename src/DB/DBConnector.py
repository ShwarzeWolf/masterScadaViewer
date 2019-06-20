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
            print("Connection to " + DBalias + " was established")

        except:
            print("Connection failed")

    def __getEstablishedConnection(self, alias):
        for connection in self.connectionsList:
            if connection[0] == alias:
                return connection[1]

    def executeStatement(self, DBalias, statement):
        connection = self.__getEstablishedConnection(DBalias)

        cursor = connection.cursor()
        cursor.execute(statement)

        return cursor



