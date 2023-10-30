from job import Job

print("Testing Job Object:")

#example case of how to use job Object
tempJob = Job().fillByID(1) # ID = 1
print("Job ID: ",tempJob.getId(),type(tempJob.getId()))
print("Title: ",tempJob.getTitle(),type(tempJob.getTitle()))
print("Tags: ", tempJob.getTags(),type(tempJob.getTags()))
print("Company: ", tempJob.getCompanyID(),type(tempJob.getCompanyID()))
print("Salary Range: ", tempJob.getSalaryRange(),type(tempJob.getSalaryRange()))
print("Location: ", tempJob.getLocation(),type(tempJob.getLocation()))
print("Description: ", tempJob.getDesc(),type(tempJob.getDesc()))