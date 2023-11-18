from job import Job
from company import Company

print("Testing Job Object:")

#example case of how to use job Object
tempJob = Job().fillByID(1) # ID = 1
print("Job ID: ",tempJob.getID(),type(tempJob.getID()))
print("Title: ",tempJob.getTitle(),type(tempJob.getTitle()))
print("Tags: ", tempJob.getTags(),type(tempJob.getTags()))
print("Company: ", tempJob.getCompanyID(),type(tempJob.getCompanyID()))
print("Salary Range: ", tempJob.getSalaryRange(),type(tempJob.getSalaryRange()))
print("Location: ", tempJob.getLocation(),type(tempJob.getLocation()))
print("Description: ", tempJob.getDesc(),type(tempJob.getDesc()))

#example case of writing a new job

tempTitle = "CEO"
tempTags = ['PathFinder', 'Manager', 'C-Suite', 'Executive']
tempComp = Company().findCompany('PathFinder')
tempMinSal = 0
tempMaxSal = 1
tempCity = 'Daytona Beach'
tempState = 'FL'
tempDesc = 'Work for a failing company with no product! great pay.'

tempJob = Job().newJob(tempTitle,tempTags,tempComp.getID(),tempCity,tempState,tempMinSal,tempMaxSal,tempDesc)

print("Job ID: ",tempJob.getID(),type(tempJob.getID()))
print("Title: ",tempJob.getTitle(),type(tempJob.getTitle()))
print("Tags: ", tempJob.getTags(),type(tempJob.getTags()))
print("Company: ", tempJob.getCompanyID(),type(tempJob.getCompanyID()))
print("Salary Range: ", tempJob.getSalaryRange(),type(tempJob.getSalaryRange()))
print("Location: ", tempJob.getLocation(),type(tempJob.getLocation()))
print("Description: ", tempJob.getDesc(),type(tempJob.getDesc()))