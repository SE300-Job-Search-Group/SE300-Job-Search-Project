from .job import Job

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
    
        self.jobs = []

    def search_jobs(self, keywords):
        # this where the code actually handles the keywords
        matching_jobs = [job for job in self.jobs if any(keyword in job.title for keyword in keywords)]
        print(f"Received keywords: {keywords}")
        print(f"Matching jobs: {matching_jobs}")
        return matching_jobs
