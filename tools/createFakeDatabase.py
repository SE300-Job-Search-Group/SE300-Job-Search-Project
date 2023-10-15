import sqlite3

#initialization
db = sqlite3.connect("./database/test.db")
dbctrl = db.cursor()

#deletes tables that are being setup
dbctrl.execute("""
    DROP TABLE IF EXISTS
        jobs
""")

dbctrl.execute("""
    DROP TABLE IF EXISTS
        companies
""")

dbctrl.execute("""
    DROP TABLE IF EXISTS
        job_company
""")

#stores all jobs
dbctrl.execute("""
    CREATE TABLE jobs(
        job_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL, 
        company TEXT NOT NULL,
        location_city TEXT,
        location_state TEXT,
        description TEXT
    )
""")

#stores all companies
dbctrl.execute("""
    CREATE TABLE companies(
        company_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        industry TEXT,
        description TEXT
    )
""")

# Table that stores all relations between jobs and companies 
dbctrl.execute("""
    CREATE TABLE job_company(
        job_id INTEGER,
        company_id INTEGER,
        PRIMARY KEY (job_id, company_id),
        FOREIGN KEY (job_id)
            REFERENCES jobs (job_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
    )
""")

#cleanup
db.close()