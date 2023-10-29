from databaseHandler import DatabaseHandler
class GenericWord:
    def __init__(self,word):
        self.word = word
        self.id = None
        self.type = None

    #Methods
    def assignID(self):
        # searches db if exists
        dbh = DatabaseHandler("./database/test.db")
        
        existingID = dbh.findID(self.word,self.type)
        if existingID is None:
            newID = dbh.assignID(self.word,self.type)
            self.id = newID
        else:
            self.id = existingID

        return self.id
    
    #Functions

    def getWord(self):
        return self.word
    

class Tag(GenericWord):
    def __init__(self,word):
        super().__init__(word)
        self.type = 'tag'

class Keyword(GenericWord):
    def __init__(self,word):
        super().__init__(word)
        self.type = 'keyword'

class Skill(GenericWord):
    def __init__(self,word):
        super().__init__(word)
        self.type = 'skill'