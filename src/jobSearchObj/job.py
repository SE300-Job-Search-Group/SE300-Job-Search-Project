import user
import sqlite3

class Job:
    def __init__(self,id):
        self.id = id
        
        # connects to test database
        db = sqlite3.connect("./database/test.db")
        #should have option to connect to actual database

        #fetch job data
        dbctrl = db.cursor()

        tempDB=dbctrl.execute('SELECT * FROM jobs WHERE job_id ='+str(id))
        tempData = tempDB.fetchone()

        #debug print
        #print(tempData)
        
        # setting attributes
        self.title = tempData[1]
        self.company = tempData[2]
        self.city = tempData[3]
        self.state = tempData[4]
        self.description = tempData[5]

    # methods
    
    def userMatch(self,usr: user) -> float:
        return 1 #should return match ranking 

    # functions

    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getCompany(self):
        return self.company
    
    def getCity(self):
        return self.city
    
    def getState(self):
        return self.state
    
    def getDesc(self):
        return self.description