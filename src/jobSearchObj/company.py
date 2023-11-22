from user import User
from databaseHandler import CompanyDBHandler
from words import Industry,Keyword
from review import Review

class Company:
    def __init__(self):

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

        self.reviews = []
    
    # init functions
    def fillByID(self, id): # returns a new Company give the input ID
        dbh = CompanyDBHandler()

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
    
    def findCompany(self,name):
        dbh = CompanyDBHandler()
        companyInfo = dbh.searchByName(name)
        if companyInfo is None:
            raise Exception("Database Search Error: No Existing Company with Name")
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
    
    def addReviews(self,reviews:list[str]):
        for review in reviews:
            self.reviews.append(Review().addReview(self.id,review))
        return self.reviews
    
    def addReview(self,review:str):
        self.reviews.append(Review().addReview(self.id,review))
        return self.reviews

    def fillReviews(self):
        dbh = CompanyDBHandler()

        tempRes = dbh.findReviews(self.id)

        for review in tempRes:
            self.reviews.append(Review().fill(review[0],review[1],review[2]))
        
        return self.reviews
    
    def newCompany(self,name:str,industry:str,keywords:list[str],description:str,ratings: list[float]):
        dbh = CompanyDBHandler()

        self.name = name
        self.industry = Industry().fillbyName(industry)
        self.description = description
        self.rating = ratings[0]
        self.rating_wl = ratings[1]
        self.rating_pb = ratings[2]
        self.rating_career = ratings[3]
        self.rating_management = ratings[4]
        self.rating_culture = ratings[5]
        #tags handling
        for kw in keywords:
            self.keywords.append(Keyword().fillbyName(kw))

        self.id = dbh.writeCompany(self.name,self.industry.getID(),self.description,self.rating,self.rating_wl,self.rating_pb,self.rating_career,self.rating_management,self.rating_culture)

        #write kwd associations
        tempCompKwds = []
        for keywords in self.keywords:
            tempCompKwds.append((keywords.getID(),self.id))

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
    
    def getID(self):
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
    
    def getReviews(self):
        return self.reviews
    
    def getReviewContents(self):
        tempRes = []
        for review in self.reviews:
            tempRes.append(review.getReview())

        return tempRes