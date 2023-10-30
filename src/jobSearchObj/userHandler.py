from user import User
from location import Location
from words import Keyword, Skill

class UserHandler:

    def __init__(self):
        self.curUser = User()

    #methods
    def login(self, user: str, password: str) -> bool:
        loginSuccess = self.curUser.login(user,password)

        return loginSuccess
    
    def createAccount(self,username:str,password:str,keywordNames:list,skillNames:list,city:str,state:str,minSalary:int,maxSalary:int):
        
        # changing words from string list to Word Object List
        keywords = []
        for kwName in keywordNames:
            keywords.append(Keyword().fillbyName(kwName))
        
        skills = []
        for skillName in skillNames:
            skills.append(Skill().fillbyName(skillName))

        #from city & state to location
        location = Location().assignID(city, state)
        
        self.curUser.createUser(username,password,keywords,skills,location,minSalary,maxSalary)
    
    def updateUser(self):
        pass
