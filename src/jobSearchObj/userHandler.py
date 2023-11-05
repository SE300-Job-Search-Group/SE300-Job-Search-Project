from user import User
from location import Location
from words import Keyword, Skill
from typing import Union

class UserHandler:

    def __init__(self):
        self.curUser = User()

    #methods
    def login(self, user: str, password: str) -> Union[bool, int]:
        # Assuming self.curUser is an instance of the user class
        loginSuccess = self.curUser.login(user, password)

        return loginSuccess  # This will now return either False or the user ID
    
    def logout(self):
        self.curUser = User()
        

    def updateAccount(self, user_id, new_location, new_salary_range, new_keywords, new_skills):
        # Assuming you have a User object and a method to update user information
        user = self.curUser.get_user_by_id(user_id)

        # Update the user's information
        user.location = new_location
        user.salary_range = new_salary_range
        user.keywords = new_keywords
        user.skills = new_skills

        # Save the updated user to the data store
        # You need to implement this part based on your data store (e.g., database)

        return True  # Return True if the update was successful, otherwise handle errors


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