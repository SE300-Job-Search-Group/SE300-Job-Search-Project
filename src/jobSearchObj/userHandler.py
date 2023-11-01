from user import User

class UserHandler:

    def __init__(self):
        self.curUser = User()

    #methods
    def login(self, user: str, password: str) -> bool:
        loginSuccess = self.curUser.login(user,password)

        return loginSuccess
    
    def updateUser(self, user_id, new_location, new_salary_range, new_keywords, new_skills):
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