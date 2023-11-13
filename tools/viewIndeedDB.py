import sqlite3

db = sqlite3.connect("./indeed_aerospace_jobs.db")

cur = db.cursor()

tempRes = cur.execute("""SELECT * FROM jobs""")

tempPrint = tempRes.fetchall()

print(tempPrint)