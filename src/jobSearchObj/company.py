from user import User
from databaseHandler import CompanyDBHandler
from words import Industry,Keyword

class Company:
    def __init__(self):

        # DB TO USE
        self.db = "./database/test.db";

        # Attributes
        self.id = None
        self.name = None
        self.industry = None # Industry Object
        self.keywords = [] # list of Keyword Object
        self.description = None
        self.rating = None
        self.rating_wl = None
        self.rating_pb = None
        self.rating_career = None
        self.rating_management = None
        self.rating_culture = None
    
    # init functions
    def fillByID(self, id): # returns a new Company give the input ID
        dbh = CompanyDBHandler(self.db)

        companyInfo = dbh.searchByID(id)

        if companyInfo is None:
            raise Exception("Database Search Error: No Existing Company with ID")
        else:
            self.id = companyInfo[0]
            self.name = companyInfo[1]
            self.industry = Industry().fillByID(companyInfo[2])
            self.description = companyInfo[3]
            self.rating = companyInfo[4]
            self.rating_wl = companyInfo[5]
            self.rating_pb = companyInfo[6]
            self.rating_career = companyInfo[7]
            self.rating_management = companyInfo[8]
            self.rating_culture = companyInfo[9]
            
            #sets all keywords
            tempKeywordIDs = dbh.findKeywordIDs(self.id)

            for id in tempKeywordIDs:
                self.keywords.append(Keyword().fillByID(id[0]))

        dbh.close()
        return self

    # methods
    
    def userMatch(self,usr: User) -> float:
        #considers keyword w/ desired company traits, ratings w/ desired traits, and overall ratings

        #temp user stuff until user is made
        tempUserDCT = ['']
        tempUserRatingRanked = ['']

        return 1 #should return match rating
    
    # functions
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getIndustry(self):
        return self.industry.getWord()
    
    def getKeywords(self):
        tempKwds = []
        for kw in self.keywords:
            tempKwds.append(kw.getWord())
        return tempKwds
    
    def getDesc(self):
        return self.description
    
    def getRating(self):
        return [self.rating, self.rating_wl, self.rating_pb, self.rating_career, self.rating_management, self.rating_culture]