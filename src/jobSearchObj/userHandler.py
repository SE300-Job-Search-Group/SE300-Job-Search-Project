from user import User
from location import Location
from words import Keyword, Skill
from typing import Union

class UserHandler:

    def __init__(self):
        self.curUser = User()

    #methods
    def login(self, user: str, password: str) -> Union[bool, int]:
        self.curUser = User()
        # Assuming self.curUser is an instance of the user class
        loginSuccess = self.curUser.login(user, password)

        return loginSuccess  # This will now return either False or the user ID
    
    def logout(self):
        self.curUser = User()

    def createAccount(self,username:str,password:str,keywordNames:list,skillNames:list,city:str,state:str,minSalary:int,maxSalary:int): # creates new account
        
        # changing words from string list to Word Object List
        keywords = []
        for kwName in keywordNames:
            keywords.append(Keyword().fillbyName(kwName))
        
        skills = []
        for skillName in skillNames:
            skills.append(Skill().fillbyName(skillName))

        #from city & state to location
        location = Location().assignID(city, state)
        
        #tells User to put itself in database
        self.curUser.createUser(username,password,keywords,skills,location,minSalary,maxSalary)

    def updateAccount(self, new_keywords, new_skills, new_city, new_state, new_minSal, new_maxSal):

        # finds keyword/skills id
        keywords = []
        for kwName in new_keywords:
            keywords.append(Keyword().fillbyName(kwName))
        
        skills = []
        for skillName in new_skills:
            skills.append(Skill().fillbyName(skillName))

        #location object
        location = Location().assignID(new_city, new_state)
        self.curUser.updateUser(keywords,skills,location,new_minSal,new_maxSal)

    #functions
    def userUsername(self):
        return self.curUser.getUsername()
    
    def userKeywords(self):
        return self.curUser.getKeywords()
    
    def userSkills(self):
        return self.curUser.getSkills()
    
    def userLocation(self):
        return self.curUser.getLocation()
    
    def userSalaryRange(self):
        return self.curUser.getSalaryRange()
    
    def userCity(self):
        return self.curUser.getCity()
    
    def userState(self):
        return self.curUser.getState()
    
    def userMinSalary(self):
        return self.curUser.getMinSalary()
    
    def userMaxSalary(self):
        return self.curUser.getMaxSalary()