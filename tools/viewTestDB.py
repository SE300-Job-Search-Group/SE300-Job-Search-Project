import sqlite3

db = sqlite3.connect("./database/test.db")
cur = db.cursor()

def viewJobs():
    jobs = cur.execute("""SELECT * FROM jobs""")

    return jobs.fetchall()


def viewCompanies():
    companies = cur.execute("""SELECT * FROM companies""")

    return companies.fetchall()

def viewUsers():
    users = cur.execute("""SELECT * FROM users""")

    return users.fetchall()


#print results (Add and Remvoe as needed)
print(viewJobs())
print(viewCompanies())
print(viewUsers())