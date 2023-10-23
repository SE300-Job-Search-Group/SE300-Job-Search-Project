from user import User
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
        print(tempData)
        
        # setting attributes
        self.title = tempData[1]
        self.keywords = tempData[2].split(",")
        self.company = tempData[3]
        self.city = tempData[4]
        self.state = tempData[5]
        self.minSalary = tempData[6]
        self.maxSalary = tempData[7]
        self.description = tempData[8]

    # methods
    
    def userMatch(self,user: User) -> float:
        #compares keywords w/ skills, salary range, location

        #temp until user stuff is setup
        tempUserSkills = ['']
        tempUserSalaryRange = ['']
        tempUserLocation = ['']

        


        return 1 #should return match rating

    # functions

    def getId(self):
        return self.id
    
    def getKeywords(self):
        return self.keywords
    
    def getTitle(self):
        return self.title
    
    def getCompany(self):
        return self.company
    
    def getCity(self):
        return self.city
    
    def getState(self):
        return self.state
    
    def getLocation(self):
        return self.city+ ", "+ self.state
    
    def getSalaryRange(self):
        return [self.minSalary, self.maxSalary]

    def getDesc(self):
        return self.description