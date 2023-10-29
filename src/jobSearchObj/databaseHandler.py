import sqlite3

class DatabaseHandler:
    def __init__(self,dir):
        self.db = sqlite3.connect(dir)
        self.dbctrl = self.db.cursor()
    
    #Generic Commands
    def close(self):
        self.db.close()

    def getTable(self,table: str):
        tempDB = self.dbctrl.execute('SELECT * FROM '+table)
        tableData = tempDB.fetchall()
        return tableData

    # Tag Related

    def findID(self,name: str,type: str) -> int:
        table_name = type+'s'
        col_id = type+'_id'

        tempDB = self.dbctrl.execute("SELECT "+col_id+" FROM "+table_name+" WHERE EXISTS (SELECT "+col_id+" FROM "+table_name+" WHERE "+type+" = '"+name+"')")
        
        tempID = tempDB.fetchone()
        if tempID is None:
            return tempID
        else:
            return tempID[0]

    def assignID(self,name: str,type: str) -> int:
        table_name = type+'s'
        col_id = type+'_id'

        #finds new ID
        tempDB = self.dbctrl.execute('SELECT MAX('+col_id+') FROM '+table_name)
        maxID = tempDB.fetchone()[0]
        if maxID is None:
            maxID = 0
        newID = maxID + 1
        #inserts new tag into database
        self.dbctrl.execute("INSERT INTO "+table_name+" VALUES ("+str(newID)+",'"+name+"')")
        self.db.commit()

        return newID