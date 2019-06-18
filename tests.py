import DBConnector

dbc = DBConnector.DBConnector()
dbc.connectAll()

#dbc.getTablesFromDatabase("ALARMS")
#dbc.getDataFromTable("ALARMS", "MASEVENTCHANGES")

dbc.getAllDataFromDB("ALARMS")