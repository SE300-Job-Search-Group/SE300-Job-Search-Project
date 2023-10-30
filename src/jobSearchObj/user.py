from databaseHandler import UserDBHandler
from location import Location
from words import Keyword, Skill

class User:
    
    def __init__(self):
        self.db = "./database/test.db"

        #attributes
        self.id = None
        self.username = None
        self.__password = None
        self.keywords = []
        self.skills = []
        self.location = None
        self.minSalary = None
        self.maxSalary = None

    # methods
    def login(self,user: str,password: str) -> bool:  # login & user id filling. Returns False if login failed
        dbh = UserDBHandler(self.db)
        self.id = dbh.validateLogin(user,password)
        if self.id is None:
            return False
        else:
            userInfo = dbh.searchByID(self.id)
            self.username = userInfo[1]
            self.__password = userInfo[2]
            self.location = Location().fillByID(userInfo[3])
            self.minSalary = userInfo[4]
            self.maxSalary = userInfo[5]

            # sets all keywords
            tempKeywordID = dbh.findKeywordIDs(self.id)

            for id in tempKeywordID:
                self.keywords.append(Keyword().fillByID(id[0]))

            #sets all skills
            tempSkillID = dbh.findSkillIDs(self.id)

            for id in tempSkillID:
                self.skills.append(Skill().fillByID(id[0]))

            return True
        
    def newUser(self):
        pass

    #methods

    # functions

    def getID(self):
        return self.id
    
    def getUsername(self):
        return self.username
    
    def getKeywords(self):
        tempKeywords = []
        for keyword in self.keywords:
            tempKeywords.append(keyword.getWord())
        return tempKeywords
    
    def getSkills(self):
        tempSkills = []
        for skill in self.skills:
            tempSkills.append(skill.getWord())

        return tempSkills
    
    def getLocation(self):
        return self.location.getLocationName()
    
    def getSalaryRange(self):
        return [self.minSalary, self.maxSalary]