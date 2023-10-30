import sqlite3

class GenericDatabaseHandler:
    def __init__(self,dir):
        self.db = sqlite3.connect(dir)
        self.dbctrl = self.db.cursor()
    
    #Generic Commands
    def close(self):
        self.db.close()

    def getTable(self,table: str):
        tempResults = self.dbctrl.execute('SELECT * FROM '+table)
        tableData = tempResults.fetchall()
        return tableData

class WordsDBHandler(GenericDatabaseHandler):

    def searchByID(self,id: int, type:str) -> str:
        table_name = type+'s'
        col_id = type+'_id'
        tempResults = self.dbctrl.execute("SELECT "+type+" FROM "+table_name+" WHERE EXISTS (SELECT "+col_id+" FROM "+table_name+" WHERE "+col_id+" = '"+str(id)+"') AND "+col_id+" = '"+str(id)+"'")
        
        tempName = tempResults.fetchone()
        if tempName is None:
            return None
        else:
            return tempName[0]

    def findID(self,name: str,type: str) -> int:
        table_name = type+'s'
        col_id = type+'_id'

        tempResults = self.dbctrl.execute("SELECT "+col_id+" FROM "+table_name+" WHERE EXISTS (SELECT "+col_id+" FROM "+table_name+" WHERE "+type+" LIKE '"+name+"') AND "+type+" = '"+name+"'")
        tempID = tempResults.fetchone()
        if tempID is None:
            return None
        else:
            return tempID[0]

    def assignID(self,name: str,type: str) -> int:
        table_name = type+'s'
        col_id = type+'_id'

        #finds new ID
        tempResults = self.dbctrl.execute('SELECT MAX('+col_id+') FROM '+table_name)
        maxID = tempResults.fetchone()[0]
        if maxID is None:
            maxID = 0
        newID = maxID + 1
        #inserts new tag into database
        self.dbctrl.execute("INSERT INTO "+table_name+" VALUES ("+str(newID)+",'"+name+"')")
        self.db.commit()

        return newID

class LocDBHandler(GenericDatabaseHandler):
    def searchByID(self,id: int):
        tempResults = self.dbctrl.execute("SELECT * FROM locations WHERE EXISTS (SELECT location_id FROM locations WHERE location_id = "+str(id)+") AND location_id = "+str(id))
        
        return tempResults.fetchone()
    

class CompanyDBHandler(GenericDatabaseHandler):
    def searchByID(self, id: int):
        tempResults = self.dbctrl.execute("SELECT * FROM companies WHERE EXISTS (SELECT company_id FROM companies WHERE company_id = "+str(id)+") AND company_id = "+str(id))
        
        return tempResults.fetchone()
    
    def findKeywordIDs(self,id: int) -> list:
        tempResults = self.dbctrl.execute("SELECT keyword_id FROM company_keyword WHERE company_id = " + str(id))

        return tempResults.fetchall()
    
class JobDBHandler(GenericDatabaseHandler):
    def searchByID(self, id: int):
        tempResults = self.dbctrl.execute("SELECT * FROM jobs WHERE EXISTS (SELECT job_id FROM jobs WHERE job_id = "+str(id)+") AND job_id = "+str(id))
        
        return tempResults.fetchone()
    
    def findTagIDs(self,id: int) -> list:
        tempResults = self.dbctrl.execute("SELECT tag_id FROM job_tag WHERE job_id = " + str(id))

        return tempResults.fetchall()