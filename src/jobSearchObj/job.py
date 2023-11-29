from user import User
from databaseHandler import JobDBHandler
from words import Tag
from location import Location
from company import Company

class Job:
    def __init__(self):
        
        # setting attributes
        self.id = None
        self.title = None
        self.tags = []
        self.company_id = None
        self.location = None
        self.minSalary = None
        self.maxSalary = None
        self.description = None
        self.url = None

    # init functions
    def fillByID(self,id): # returns a new job object filled based on provided job_id
        dbh = JobDBHandler()

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
            self.url = jobInfo[7]

            #sets all tags
            tempTagIDs = dbh.findTagIDs(self.id)

            for id in tempTagIDs:
                self.tags.append(Tag().fillByID(id[0]))

        dbh.close()
        return self
    
    def newJob(self,title: str,tags: list[str],company_id: int,city: str,state: str,minSalary: int, maxSalary: int, description: str,url: str):
        dbh = JobDBHandler()

        self.title = title
        self.company_id = company_id
        self.location = Location().assignID(city,state)
        self.minSalary = minSalary
        self.maxSalary = maxSalary
        self.description = description
        self.url = url
        #tags handling
        for tag in tags:
            self.tags.append(Tag().fillbyName(tag))

        #write jobs
        self.id = dbh.writeJob(self.title,self.company_id,self.location.getID(),self.minSalary,self.maxSalary,self.description,self.url)

        #write tag associations
        tempJobTags = []
        for tag in self.tags:
            tempJobTags.append((tag.getID(),self.id))

        dbh.writeTags(tempJobTags)

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

    def getID(self):
        return self.id
    
    def getTags(self):
        tempTags = []
        for tag in self.tags:
            tempTags.append(tag.getWord())

        return tempTags
    
    def getTagIDs(self):
        tempTags = []
        for tag in self.tags:
            tempTags.append(tag.getID())

        return tempTags
    
    def getTitle(self):
        return self.title
    
    def getCompanyID(self):
        return self.company_id
    
    def getCompanyName(self):
        return Company().fillByID(self.id).getName()
    
    def getCompany(self):
        return Company().fillByID(self.company_id)
    
    def getLocationName(self):
        return self.location.getLocationName()
    
    def getLocation(self):
        return self.location
    
    def getSalaryRange(self):
        return [self.minSalary, self.maxSalary]
    
    def getMaxSalary(self):
        return self.maxSalary
    
    def getMinSalary(self):
        return self.minSalary

    def getDesc(self):
        return self.description
    
    def getURL(self):
        return self.url
    
