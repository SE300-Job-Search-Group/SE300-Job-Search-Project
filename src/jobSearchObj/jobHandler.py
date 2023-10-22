from .job import Job

class JobHandler:

    def __init__(self):
        self.jobs = []

    def search_jobs(self, keywords):
        # this where the code actually handles the keywords
        matching_jobs = [job for job in self.jobs if any(keyword in job.title for keyword in keywords)]
        print(f"Received keywords: {keywords}")
        print(f"Matching jobs: {matching_jobs}")
        return matching_jobs