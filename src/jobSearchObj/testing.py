from databaseHandler import TestDBHandler
from words import Tag, Keyword, Skill

dbh = TestDBHandler("./database/test.db")

print(dbh.getTable("jobs"))
print(dbh.getTable("tags"))
print(dbh.getTable("job_tag"))

result = dbh.execute("""
    SELECT job_id FROM job_tag
        WHERE tag_id IN (1,2,3,4)
        GROUP BY job_id
        HAVING COUNT(*)>=1
""")
tempOutput = result.fetchall()
output = []
for i in tempOutput:
    output.append(i[0])

print("===================================")
print(output)