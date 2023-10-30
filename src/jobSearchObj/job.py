from user import User
from databaseHandler import JobDBHandler
from words import Tag
from location import Location

class Job:
    def __init__(self):
        
        # DB TO USE
        self.db = "./database/test.db";
        
        # setting attributes
        self.id = None
        self.title = None
        self.tags = []
        self.company_id = None
        self.location = None
        self.minSalary = None
        self.maxSalary = None
        self.description = None

    # init functions
    def fillByID(self,id): # returns a new job object filled based on provided job_id
        dbh = JobDBHandler(self.db)

        jobInfo = dbh.searchByID(id)

        if jobInfo is None:
            raise Exception("Database Search Error: No Existing Job with ID")
        else:
            self.id = jobInfo[0]
            self.title = jobInfo[1]
            self.company_id = jobInfo[2]
            self.location = Location().fillByID(jobInfo[3])
            self.maxSalary = jobInfo[4]
            self.minSalary = jobInfo[5]
            self.description = jobInfo[6]

            #sets all tags
            tempTagIDs = dbh.findTagIDs(self.id)

            for id in tempTagIDs:
                self.tags.append(Tag().fillByID(id[0]))

        dbh.close()
        return self

    # methods
    
    def userMatch(self,user: User) -> float:
        #compares tags w/ skills, salary range, location

        #temp until user stuff is setup
        tempUserSkills = ['']
        tempUserSalaryRange = ['']
        tempUserLocation = ['']

        


        return 1 #should return match rating

    # functions

    def getId(self):
        return self.id
    
    def getTags(self):
        tempTags = []
        for tag in self.tags:
            tempTags.append(tag.getWord())

        return tempTags
    
    def getTitle(self):
        return self.title
    
    def getCompanyID(self):
        return self.company_id
    
    def getLocation(self):
        return self.location.getLocationName()
    
    def getSalaryRange(self):
        return [self.minSalary, self.maxSalary]

    def getDesc(self):
        return self.description