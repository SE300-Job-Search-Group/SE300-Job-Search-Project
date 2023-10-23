import sqlite3

# RUNNING THIS DELETES ALL DATA IN test.db

def reinitDatabase():
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
            users
    """)

    dbctrl.execute("""
        DROP TABLE IF EXISTS
            reviews
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
            keywords TEXT,
            company TEXT NOT NULL,
            location_city TEXT,
            location_state TEXT,
            max_salary INTEGER,
            min_salary INTEGER, 
            description TEXT
        )
    """)

    #stores all companies
    dbctrl.execute("""
        CREATE TABLE companies(
            company_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            industry TEXT,
            keywords TEXT,
            description TEXT,
            rating_overall REAL,
            rating_worklife REAL,
            rating_paybenefits REAL,
            rating_career REAL,
            rating_management REAL,
            rating_culture REAL
        )
    """)

    #stores users
    dbctrl.execute("""
        CREATE TABLE users(
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT,
            keywords TEXT,
            skills TEXT,
            city REAL,
            state REAL,
            minSalary REAL,
            maxSalary REAL
        )
    """)

    #stores all company reviews NEEDS TO BE MADE link w/ company_id
    # dbctrl.execute("""
    #     CREATE TABLE reviews(
            
    #     )
    # """)

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

def fillJobs():
    db = sqlite3.connect("./database/test.db")
    dbctrl = db.cursor()
    
    # yea idk i just wanted to test it out :) add more as needed
    jobData = [
        (1, 'Entry Level Software Engineer', 'Software, Entry-level, Programming, Computer Science, Engineering', 'PathFinder', 'Daytona Beach', 'FL', 5, 100000, 'idk'),
        (2, 'Project Manager', 'Project Management, Manager, Software, Engineering', 'PathFinder', 'Daytona Beach', 'FL', 1000000, 2000000, 'manage the projects duh')
    ]
    
    dbctrl.executemany("""
    INSERT or IGNORE INTO jobs VALUES
        (?,?,?,?,?,?,?,?,?)
    """,jobData)

    #commits insert changes
    db.commit()
    db.close()

def fillCompanies():
    db = sqlite3.connect("./database/test.db")
    dbctrl = db.cursor()

    # yea idk i just wanted to test it out :) add more as needed
    companyData = [
        (1,'PathFinder', 'Technology','Work-Life Balance, Flat Hierarchy, Family-like, Opportunity', 'The PathFinder company is the best company in the world',5.0,4.9,4.8,4.7,4.6,4.5)
    ]
    dbctrl.executemany("""
    INSERT or IGNORE INTO companies VALUES
        (?,?,?,?,?,?,?,?,?,?,?)
    """,companyData)

    #commits insert changes
    db.commit()
    db.close()

def fillUser():
    db = sqlite3.connect("./database/test.db")
    dbctrl = db.cursor()

    # add more as needed
    userData = [
        #User skills, pref. location, keywords
        (1, 'luv2code', 'Passcode123%', 'work-life balance, vacation, benefits', 'python, programming, soft skills', 'New York', 'NY', 70000, 100000),
        (2, 'NGNeer365', 'J1mmyJ@hns', 'healthy deadlines, communication, recognition', 'matlab, leadership, microsoft', 'Huntsville', 'AL', 90000, 150000)
    ]
    dbctrl.executemany("""
    INSERT or IGNORE INTO users VALUES
        (?,?,?,?,?,?,?,?,?)
    """,userData)

    #commits insert changes
    db.commit()
    db.close()

#runs functions
reinitDatabase() #reinitiates tables
fillJobs() #fills job database with fake test jobs
fillCompanies() #fills company database with fake test companies
fillUser() # fills user database with fake test users
#fillReviews() #fills review database w/ company relations
#relateJobsCompanies() #fills job_company database