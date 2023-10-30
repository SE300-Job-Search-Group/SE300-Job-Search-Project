from user import User

class UserHandler:

    def __init__(self):
        self.curUser = User()

    #methods
    def login(self, user: str, password: str) -> bool:
        loginSuccess = self.curUser.login(user,password)

        return loginSuccess
    
    def updateUser(self):
        pass