from jobHandler import JobHandler

test_keywords = ['PathFinder','Engineer','Software']

jh = JobHandler()

test_result = jh.searchTags(test_keywords)

for job in test_result:
    print(str(job.getID()))
    print(str(job.getSalaryRange()))


# general search function

#inputs
tempCompany = 'PathFinder'
tempCity = 'Orlando'
tempState = 'FL'
tempDistance = 1000
tempMinSal = 1
tempMaxSal = 1000

test_result = jh.searchDB(test_keywords,tempCompany,tempCity,tempState,tempDistance,tempMinSal,tempMaxSal)

for job in test_result:
    print(str(job.getID()))
    print(str(job.getSalaryRange()))

