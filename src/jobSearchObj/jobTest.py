from job import Job

print("Testing Job Object:")

#example case of how to use job Object
tempJob = Job(1) # ID = 1
print("Job ID: ",tempJob.getId())
print("Title: ",tempJob.getTitle())
print("Keywords: ", tempJob.getKeywords())
print("Company: ", tempJob.getCompany())
print("Salary Range: ", tempJob.getSalaryRange())
print("Location: ", tempJob.getCity()+', '+tempJob.getState())
print("Description: ", tempJob.getDesc())