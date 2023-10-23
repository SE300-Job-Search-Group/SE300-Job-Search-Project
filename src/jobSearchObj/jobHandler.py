from .job import Job

class JobHandler:

    def __init__(self):
        #initialize an empty list to store job objects.
        self.jobs = []

    def search_jobs(self, keywords):
        #this where the code actually handles the keywords

        #initialize an empty list to store matching jobs.
        matching_jobs = [job for job in self.jobs if any(keyword in job.title for keyword in keywords)]
        
        #print statements to verify keywords 
        print(f"Received keywords: {keywords}")
        print(f"Matching jobs: {matching_jobs}")
        
        #returning the list of matched jobs
        return matching_jobs