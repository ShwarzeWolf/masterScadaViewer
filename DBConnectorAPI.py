import DBConnector

class DBCOnnectorAPI:
    def __init__(self):
        self.dbc = DBConnector.DBConnector()
        self.dbc.connectAll()

    def getAlarms(self):
        statement = "select * from MASEVENTDATA"
        return self.dbc.executeStatement("ALARMS", statement)

    def getTablesNamesFromDatabase(self, DBAlias):
        statement = "SELECT RDB$RELATION_NAME FROM RDB$RELATIONS WHERE (RDB$SYSTEM_FLAG <> 1 OR RDB$SYSTEM_FLAG IS NULL) AND RDB$VIEW_BLR IS NULL ORDER BY RDB$RELATION_NAME;"
        return self.dbc.executeStatement(DBAlias, statement).fetchall()

    def getDataFromTable(self, DBAlias, tableName):
        statement = "select * from " + tableName
        return self.dbc.executeStatement(DBAlias, statement).fetchall()

    def getColumnsNamesFromTable(self, DBAlias, tableName):
        statement = "select rdb$field_name from rdb$relation_fields where rdb$relation_name='" + tableName + "'"
        return self.dbc.executeStatement(DBAlias, statement).fetchall()



