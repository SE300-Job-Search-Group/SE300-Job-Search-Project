from jobHandler import JobHandler

test_keywords = ['PathFinder','Engineer','Software']

jh = JobHandler()

test_result = jh.searchTags(test_keywords)

for job in test_result:
    print(str(job.getId()))