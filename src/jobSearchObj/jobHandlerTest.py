from jobHandler import JobHandler

test_keywords = ['PathFinder','Engineering','Software']

jh = JobHandler()

test_result = jh.searchDB(test_keywords)

print(','.join(test_keywords))
print(test_result)
print("Hello World")