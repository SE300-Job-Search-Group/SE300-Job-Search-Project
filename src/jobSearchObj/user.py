from databaseHandler import UserDBHandler
from location import Location
from words import Keyword, Skill
from typing import Union

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
    def login(self, user: str, password: str) -> Union[bool, int]:
        dbh = UserDBHandler(self.db)
        self.id = dbh.validateLogin(user, password)
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

            # sets all skills
            tempSkillID = dbh.findSkillIDs(self.id)

            for id in tempSkillID:
                self.skills.append(Skill().fillByID(id[0]))

            return self.id  # Return the user ID if login is successful

        
    def createUser(self,username:str,password:str,keywords:list,skills:list,location:Location,minSalary:int,maxSalary:int): # creates new user
        #adding attributes to object
        self.username = username
        self.__password = password
        self.keywords = keywords    #list of Keywords
        self.skills = skills        #list of Skills
        self.location = location    #Location Object
        self.minSalary = minSalary
        self.maxSalary = maxSalary

        #find available ID & write User Data to ID
        #### MAKE SURE KEYWORDS SKILLS AND OBJECTS EXIST IN DB PRIOR THIS POINT
        dbh = UserDBHandler(self.db)
        self.id = dbh.findAvailableID()
        userInfo = [(self.id,self.username,self.__password,self.location.getID(),self.minSalary,self.maxSalary)]
        dbh.writeUser(userInfo)

        #write Keyword Associations
        tempUserKw = []
        for kw in self.keywords:
            tempUserKw.append((kw.getID(),self.id))

        dbh.writeUserKeywords(tempUserKw)

        #write Skill Associations
        tempUserSkill = []
        for skill in self.skills:
            tempUserSkill.append((skill.getID(),self.id))
        
        dbh.writeUserSkills(tempUserSkill)
    
        dbh.close()
        
    def updateUser(self,keywords: list, skills: list, location: Location, minSal: int, maxSal: int):
        dbh = UserDBHandler(self.db)

        userInfo = [(self.id,self.username,self.__password,self.location.getID(),self.minSalary,self.maxSalary)]
        dbh.writeUser(userInfo)

        keywordsUpdate = []
        for kw in keywords:
            keywordsUpdate.append(kw.getID(),self.id)
        
        skillsUpdate = []
        for skill in skills:
            skillsUpdate.append(skill.getID(),self.id)
        
        dbh.updateUserKeywords(self.id,keywordsUpdate)
        dbh.updateUserSkills(self.id,skillsUpdate)


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