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

    def __executeStatement(self, DBalias, statement):
        connection = self.getEstablishedConnection(DBalias)

        cursor = connection.cursor()
        cursor.execute(statement)

        return cursor

    def getAlarms(self):
        connection = self.getEstablishedConnection('ALARMS')

        cursor = connection.cursor()
        cursor.execute("select * from MASEVENTDATA")

        return cursor


    def getTablesFromDatabase(self, DBAlias):
        executionCommand = "SELECT RDB$RELATION_NAME FROM RDB$RELATIONS WHERE (RDB$SYSTEM_FLAG <> 1 OR RDB$SYSTEM_FLAG IS NULL) AND RDB$VIEW_BLR IS NULL ORDER BY RDB$RELATION_NAME;"

        connection = self.getEstablishedConnection(DBAlias)

        cursor = connection.cursor()
        cursor.execute(executionCommand)

        return cursor.fetchall()

    def getDataFromTable(self, DBAlias, tableName):
        connection = self.getEstablishedConnection(DBAlias)

        cursor = connection.cursor()
        cursor.execute("select * from " + tableName)

        return cursor.fetchall()

    def getAllDataFromDB(self, DBAlias):
        tablesNames = self.getTablesFromDatabase(DBAlias)

        for table in tablesNames:
            table = "".join(table)
            print(table)
            print(self.getDataFromTable(DBAlias, table))




