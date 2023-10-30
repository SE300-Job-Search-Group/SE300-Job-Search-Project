from databaseHandler import WordsDBHandler
class GenericWord:
    def __init__(self):
        self.db = "./database/test.db"
        self.word = None
        self.id = None
        self.type = None

    #Methods

    def fillByID(self,id: int):
        dbh = WordsDBHandler(self.db)
        self.id = id
        tempWord = dbh.searchByID(self.id,self.type)
        if tempWord is None:
            raise Exception("Database Search Error: No Existing "+self.type+" with ID")
        else:
            self.word = tempWord

        dbh.close()
        return self

    def assignID(self):
        # searches db if exists
        dbh = WordsDBHandler(self.db)
        
        existingID = dbh.findID(self.word,self.type)
        if existingID is None:
            newID = dbh.assignID(self.word,self.type)
            self.id = newID
        else:
            self.id = existingID

        dbh.close()
        return self.id
    
    #Functions

    def getWord(self):
        return self.word
    
    def setWord(self,word):
        self.word = word
        return self

class Tag(GenericWord):
    def __init__(self):
        super().__init__()
        self.type = 'tag'

class Keyword(GenericWord):
    def __init__(self):
        super().__init__()
        self.type = 'keyword'

class Skill(GenericWord):
    def __init__(self):
        super().__init__()
        self.type = 'skill'

class Industry(GenericWord):
    def __init__(self):
        super().__init__()
        self.type = 'industryname'

    