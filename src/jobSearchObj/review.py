from databaseHandler import ReviewDBHandler

class Review:
    def __init__(self):
        self.id = None
        self.company_id = None
        self.review = None
    
    #init functions
    def fillByID(self,id:int):
        dbh = ReviewDBHandler()

        reviewResults = dbh.searchByID(id)
        
        if reviewResults is None:
            raise Exception("DatabaseSearch Error: No Existing Review with ID")
        else:
            self.id = reviewResults[0]
            self.company_id = reviewResults[1]
            self.review = reviewResults[2]
        dbh.close()
        return self
    
    def fill(self,id:int,company_id:int,review:str):
        self.id = id
        self.company_id = company_id
        self.review = review

        return self
    
    def addReview(self,company_id:int,review:str):
        dbh = ReviewDBHandler()

        self.id = dbh.writeReview(company_id,review)
        self.company_id = company_id
        self.review = review
        dbh.close()
        return self

    #functions

    def getID(self):
        return self.id
    
    def getCompanyID(self):
        return self.company_id
    
    def getReview(self):
        return self.review