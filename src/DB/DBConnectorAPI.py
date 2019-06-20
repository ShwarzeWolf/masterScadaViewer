from src.DB import DBConnector


class DBCOnnectorAPI:
    def __init__(self):
        self.dbc = DBConnector.DBConnector()

    def connectDatabases(self, listOfDatabases):
        for database in listOfDatabases:
            self.dbc.createConnection(database[0], database[1])

    def getEstablishedConnectionsNames(self):
        connectionsNames = []

        for connection in self.dbc.connectionsList:
            connectionsNames.append((connection[0], ))

        return connectionsNames

    def getTablesNamesFromDB(self, DBAlias):
        statement = "SELECT RDB$RELATION_NAME FROM RDB$RELATIONS WHERE (RDB$SYSTEM_FLAG <> 1 OR RDB$SYSTEM_FLAG IS NULL) AND RDB$VIEW_BLR IS NULL ORDER BY RDB$RELATION_NAME;"
        return self.dbc.executeStatement(DBAlias, statement).fetchall()

    def getColumnsNamesFromTable(self, DBAlias, tableName):
        statement = "select rdb$field_name from rdb$relation_fields where rdb$relation_name='" + tableName + "'"
        return self.dbc.executeStatement(DBAlias, statement).fetchall()

    def getDataFromTable(self, DBAlias, tableName):
        statement = "select * from " + tableName
        return self.dbc.executeStatement(DBAlias, statement).fetchall()
