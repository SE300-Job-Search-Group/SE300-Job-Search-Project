from databaseHandler import LocDBHandler

class Location:
    def __init__(self):
        self.db = "./database/test.db"
        self.id = None
        self.city = None
        self.state = None
    
    #init functions
    def fillByID(self,id:int):
        dbh = LocDBHandler(self.db)
        tempLoc = dbh.searchByID(id)
        if tempLoc is None:
            raise Exception("Database Search Error: No Existing Job with ID")
        else:
            self.id = tempLoc[0]
            self.city = tempLoc[1]
            self.state = tempLoc[2]

        dbh.close()
        return self


    #functions

    def getLocationName(self):
        return self.city+', '+self.state
