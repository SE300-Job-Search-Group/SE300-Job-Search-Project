from jobHandler import JobHandler

test_keywords = ['Engineer']
test_company = None
test_city = None
test_state = None
test_distance = None
test_sal_min = None
test_sal_max = None

jh = JobHandler()

test_result = jh.searchDB(test_keywords,test_company,test_city,test_state,test_distance,test_sal_min,test_sal_max)

for job in test_result:
    print('[TESTING]JOB ID: '+str(job.getID()))
    print('[TESTING]SALARY RANGE: '+str(job.getSalaryRange()))

"""
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

"""