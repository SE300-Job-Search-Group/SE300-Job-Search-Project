from job import Job
from company import Company
import sqlite3

class JobHandler:

    def __init__(self):
        self.db = "./database/test.db"
        self.jobs = [] #list of jobs to be shown

    #methods

    def searchDB(self,keywords: list,comp: Company,loc,sal_min: int, sal_max: int): # NEEDS TO BE FIXED/RESTRUCTURED TO USE databaseHandler
        #searches sql database for relavent jobs(first 10)
        
        # connects to test database
        db = sqlite3.connect(self.db)

        #fetch job data
        dbctrl = db.cursor()

        # this var is an array of job listings (define which vars are needed)
        tempDB=dbctrl.execute("""
            SELECT job_id FROM jobs 
                INNER JOIN job_keyword
                    ON jobs.job_id = job_keyword.job_id
                WHERE keyword.keyword_id 

        """)

        tempJobs = tempDB.fetchall() # result from search

        return tempJobs
    
        #formating to job objects
        # self.jobs = tempJobs

    #functions
