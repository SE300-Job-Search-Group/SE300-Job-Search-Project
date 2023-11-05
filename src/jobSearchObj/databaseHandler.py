import sqlite3

class GenericDatabaseHandler:
    def __init__(self,dir):
        print(dir)
        self.db = sqlite3.connect(dir)
        self.dbctrl = self.db.cursor()
    
    #Generic Commands
    def close(self): #commits and closes the sqlite connection. SHOULD BE RUN EVERY TIME YOU OPEN A HANDLER
        self.db.commit()
        self.db.close()

    def getTable(self,table: str): #general function to read tables
        tempResults = self.dbctrl.execute('SELECT * FROM '+table)
        tableData = tempResults.fetchall()
        return tableData

class WordsDBHandler(GenericDatabaseHandler):

    def searchByID(self,id: int, type:str) -> str: #searches tag,keyword,skill data base for a specific ID. returns the associated word
        table_name = type+'s'
        col_id = type+'_id'
        tempResults = self.dbctrl.execute("SELECT "+type+" FROM "+table_name+" WHERE EXISTS (SELECT "+col_id+" FROM "+table_name+" WHERE "+col_id+" = '"+str(id)+"') AND "+col_id+" = '"+str(id)+"'")
        
        tempName = tempResults.fetchone()
        if tempName is None:
            return None
        else:
            return tempName[0]

    def findID(self,name: str,type: str) -> int: #finds id based on word provided (for tag, keyword, and skills db)
        table_name = type+'s'
        col_id = type+'_id'

        tempResults = self.dbctrl.execute("SELECT "+col_id+" FROM "+table_name+" WHERE EXISTS (SELECT "+col_id+" FROM "+table_name+" WHERE "+type+" LIKE '"+name+"') AND "+type+" = '"+name+"'")
        tempID = tempResults.fetchone()
        if tempID is None:
            return None
        else:
            return tempID[0]

    def assignID(self,name: str,type: str) -> int: #assigns new id for a word
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
    
    def addLocation(self,city: str,state: str):
        self.dbctrl.execute("")

    def findID(self,city:str,state:str)-> int:
        tempResults = self.dbctrl.execute("SELECT location_id FROM locations WHERE EXISTS (SELECT location_id FROM locations WHERE city_name = '"+city+"' AND state_name = '"+state+"') AND city_name = '"+city+"' AND state_name = '"+state+"'")
        return tempResults.fetchone()[0]
    

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
    
class UserDBHandler(GenericDatabaseHandler):
    def searchByID(self, id:int): #searches for user using ID
        tempResults = self.dbctrl.execute("SELECT * FROM users WHERE EXISTS (SELECT user_id FROM users WHERE user_id= "+str(id)+") AND user_id = "+str(id))

        return tempResults.fetchone()
    
    def validateLogin(self,username: str,password: str) -> int: #basically a login function but should only be used by User object
        # returns None if failed, returns user id if exists
        tempResults = self.dbctrl.execute("""SELECT user_id FROM users WHERE EXISTS (SELECT user_id FROM users WHERE username = '"""+username+"' AND password = '"+password+"') AND username = '"+username+"' AND password = '"+password+"'")

        tempUserID = tempResults.fetchone()

        if tempUserID is not None:
            tempUserID = tempUserID[0]

        return tempUserID
    
    def findKeywordIDs(self,id: int) -> list: #finds keywords associated with the user
        tempResults = self.dbctrl.execute("SELECT keyword_id FROM user_keyword WHERE user_id = " + str(id))

        return tempResults.fetchall()

    def findSkillIDs(self,id:int) -> list: #finds skills associated with user
        tempResults = self.dbctrl.execute("SELECT skill_id FROM user_skill WHERE user_id = "+ str(id))
        
        return tempResults.fetchall()
    
    def findAvailableID(self) -> int: #finds available ID to be assigned to a new user
        tempResults = self.dbctrl.execute('SELECT MAX(user_id) from users')
        maxID = tempResults.fetchone()[0]
        if maxID is None:
            maxID = 0
        return maxID+1
    
    def writeUser(self,userInfo: list): #writes a new user to the user table in DB
        self.dbctrl.executemany("""
        INSERT or REPLACE INTO users VALUES
            (?,?,?,?,?,?)
    """,userInfo)
        
    def writeUserKeywords(self,user_kw_list: list): #write user keyword associations to user_keyword table in db
        self.dbctrl.executemany("""
        INSERT or IGNORE INTO user_keyword VALUES
            (?,?)
    """,user_kw_list)

    def writeUserSkills(self,user_skill_list: list): #see writeUserKeywords but for Skills instead
        self.dbctrl.executemany("""
        INSERT or IGNORE INTO user_skill VALUES
            (?,?)
    """,user_skill_list)