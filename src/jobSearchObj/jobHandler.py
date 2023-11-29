from job import Job
from company import Company
from words import Tag
from databaseHandler import JobSearchDBHandler
from location import Location

class JobHandler:

    def __init__(self):
        self.jobs = [] #list of jobs to be shown

    #methods

    def searchDB(self, tags:list, company: str, city:str, state: str, distance:int, sal_min: int, sal_max: int):

        self.jobs = None
        if tags is not None:
            self.jobs = self.searchTags(tags)
        else:
            Exception("No Inputs Detected")

        if company is not None:
            self.filterCompany(Company().findCompany(company))

        if city and state is not None:
            self.filterDistance(Location().assignID(city,state),distance)

        if sal_min and sal_max is not None:
            self.filterSalary(sal_min,sal_max)

        return self.jobs

    def searchTags(self,tags: list)-> list[Job]:
        #consts. change as needed
        numMatches = 1
        
        jsdb = JobSearchDBHandler()

        tag_ids = []
        for kw in tags:
            
            tag_ids.append(Tag().fillbyName(kw).getID())

        #fetch job data
        print(tag_ids)
        job_ids = jsdb.searchByTags(tag_ids,numMatches)
        print(job_ids)
        jobs = []

        for id in job_ids:
            jobs.append(Job().fillByID(id))

        return jobs

    def filterCompany(self,company: Company):
        tempJobs = []
        for job in self.jobs:
            if job.getCompanyID() == company.getID():
                tempJobs.append(job)
        self.jobs = tempJobs

    def filterDistance(self,location: Location,distance: int):
        tempJobs = []
        for job in self.jobs:

            if location.distanceFrom(job.getLocation()) < distance:
                tempJobs.append(job)

        self.jobs = tempJobs

    def filterSalary(self,minSal:int,maxSal:int):
        tempJobs = []
        for job in self.jobs:
            job.getSalaryRange()
            if job.getMaxSalary() > minSal:
                tempJobs.append(job)

        self.jobs = tempJobs

    #functions

    def getJobs(self):
        return self.jobs
    
    def getJob(self,index:int)-> Job:
        return self.jobs[index]
    
    def getJobTitle(self,index:int)-> str: #add get functions as needed
        return self.jobs[index].getTitle()
    