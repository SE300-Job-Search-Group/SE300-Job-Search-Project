from job import Job

class JobHandler:

    def __init__(self):
        self.jobs = [] #list of jobs to be shown
        self.userCriteria = [] #input search parameters(title, key words, company, locations, salary range)

    #methods

    def searchDB(self):
        #searches sql database for relavent jobs(first 10)

        

        tempJobs = [] # result from search
        self.jobs = tempJobs

    #functions
    