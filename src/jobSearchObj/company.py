from .user import User
import sqlite3

class Company:
    def __init__(self,id):
        self.id = id

        # connects to test database
        db = sqlite3.connect("./database/test.db")
        # should have option to connect to actual database

        # fetch job data
        dbctrl = db.cursor()

        tempDB=dbctrl.execute('SELECT * FROM companies WHERE company_id ='+str(id))
        tempData = tempDB.fetchone()
        
        # debug print
        # print(tempData)
        
        # setting attributes
        self.name = tempData[1]
        self.industry = tempData[2]
        self.keywords = tempData[3].split(",")
        self.description = tempData[4]
        

    # methods
    
    def userMatch(self,usr: User) -> float:
        return 1 #should return match ranking 
    
    # functions
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getIndustry(self):
        return self.industry
    
    def getKeywords(self):
        return self.keywords
    
    def getDesc(self):
        return self.description
    
    def getRating(self):
        return 1