import sqlite3

class User:
    
    def __init__(self,id):
        self.id = id

        #connects to test database
        db = sqlite3.connect("./database/test.db")

        #fetch user data
        dbctrl = db.cursor()

        # setting attributes
        self._username = tempData[1]
        self._password = tempData[2]
        self.keywords = tempData[3].split(",")
        self.skills = tempData[4].split(",")
        self.city = tempData[5]
        self.state = tempData[6]
        self.minSalary = tempData[7]
        self.maxSalary = tempData[8]


