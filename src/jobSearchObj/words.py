from databaseHandler import WordsDBHandler
class GenericWord:
    def __init__(self):
        self.word = None
        self.id = None
        self.type = None

    #init Methods

    def fillByID(self,id: int): # returns a GenericWord Object with filled info from input ID
        dbh = WordsDBHandler()
        self.id = id
        tempWord = dbh.searchByID(self.id,self.type)
        if tempWord is None:
            raise Exception("Database Search Error: No Existing "+self.type+" with ID")
        else:
            self.word = tempWord

        dbh.close()
        return self
    
    def fillbyName(self,name: str): # returns a GenericWord Object with filled info from input word. Creates new ID if necessary
        self._setWord(name)
        self._assignID()
        return self

    # methods

    def _assignID(self): #assigns a new id INTERNAL
        # searches db if exists
        dbh = WordsDBHandler()
        
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
    
    def _setWord(self,word):
        self.word = word
        return self
    
    def getID(self):
        return self.id

# child objects with a defined type

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

    