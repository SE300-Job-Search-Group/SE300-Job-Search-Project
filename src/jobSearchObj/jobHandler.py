from job import Job
from company import Company
from words import Tag
import sqlite3
from databaseHandler import JobSearchDBHandler

class JobHandler:

    def __init__(self):
        self.db = "./database/test.db"
        self.jobs = [] #list of jobs to be shown

    #methods

    def searchDB(self, tags:list, company: str, loc:str, sal_min: int, sal_max: int):
        tag_res = []
        if tags is not None:
            tag_res = self.searchTags(tags)
        
        #temp keyword results
        self.jobs = tag_res

    def searchTags(self,tags: list)-> list[Job]:
        #consts. change as needed
        numMatches = 1
        
        jsdb = JobSearchDBHandler(self.db)

        tag_ids = []
        for kw in tags:
            
            tag_ids.append(Tag().fillbyName(kw).getID())

        #fetch job data
        job_ids = jsdb.searchByTags(tag_ids,numMatches)

        jobs = []

        for id in job_ids:
            jobs.append(Job().fillByID(id))

        return jobs

    #functions

    def getJobs(self):
        return self.jobs
    
    def getJob(self,index:int)-> Job:
        return self.jobs[index]
    
    def getJobTitle(self,index:int)-> str: #add get functions as needed
        return self.jobs[index].getTitle()
    