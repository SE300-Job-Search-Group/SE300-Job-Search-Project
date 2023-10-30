from job import Job
from company import Company
import sqlite3

class JobHandler:

    def __init__(self):
        self.jobs = [] #list of jobs to be shown

    #methods

    def searchDB(self,keywords: list,comp: Company,loc,sal_min: int, sal_max: int): # NEEDS TO BE FIXED/RESTRUCTURED TO USE databaseHandler
        #searches sql database for relavent jobs(first 10)
        
        # connects to test database
        db = sqlite3.connect("./database/test.db")
        #should have option to connect to actual database

        #fetch job data
        dbctrl = db.cursor()

        # this var is an array of job listings (define which vars are needed)
        tempDB=dbctrl.execute("SELECT job_id FROM jobs WHERE keywords LIKE '"+ ','.join(keywords)+"'")

        tempJobs = tempDB.fetchall() # result from search

        return tempJobs
    
        #formating to job objects
        # self.jobs = tempJobs

    #functions
