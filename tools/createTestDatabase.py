import sqlite3

# RUNNING THIS DELETES ALL DATA IN test.db

#initialization
db = sqlite3.connect("./database/test.db")
dbctrl = db.cursor()

def deleteOldDatabases():
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
            tags
    """)

    dbctrl.execute("""
        DROP TABLE IF EXISTS
            keywords
    """)

    dbctrl.execute("""
        DROP TABLE IF EXISTS
            skills
    """)

    dbctrl.execute("""
        DROP TABLE IF EXISTS
            locations
    """)

    dbctrl.execute("""
        DROP TABLE IF EXISTS
            job_tag
    """)

    dbctrl.execute("""
        DROP TABLE IF EXISTS
            company_keyword
    """)

    dbctrl.execute("""
        DROP TABLE IF EXISTS
            user_keyword
    """)

    dbctrl.execute("""
        DROP TABLE IF EXISTS
            user_skill
    """)

def reinitMainDatabase():

    ## MAIN TABLE

    # location table since jobs and user are dependent
    dbctrl.execute("""
        CREATE TABLE locations(
            location_id INTEGER PRIMARY KEY,
            city_name TEXT,
            state_name TEXT UNIQUE
        )
    """)

    #stores all companies
    dbctrl.execute("""
        CREATE TABLE companies(
            company_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            industry TEXT,
            description TEXT,
            rating_overall REAL,
            rating_worklife REAL,
            rating_paybenefits REAL,
            rating_career REAL,
            rating_management REAL,
            rating_culture REAL
        )
    """)

    #stores all jobs
    dbctrl.execute("""
        CREATE TABLE jobs(
            job_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL, 
            company_id INTEGER,
            location_id INTEGER,
            max_salary INTEGER,
            min_salary INTEGER, 
            description TEXT,
            FOREIGN KEY (company_id)
                REFERENCES companies (company_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            FOREIGN KEY (location_id)
                REFERENCES locations (location_id)
                    ON UPDATE CASCADE
                    ON DELETE SET NULL
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
            location_id INTEGER,
            minSalary REAL,
            maxSalary REAL,
            FOREIGN KEY (location_id)
                REFERENCES locations (location_id)
                    ON UPDATE CASCADE
                    ON DELETE SET NULL
        )
    """)

    ## SUB TABLES

    dbctrl.execute("""
        CREATE TABLE tags(
            tag_id INTEGER PRIMARY KEY,
            tag TEXT NOT NULL UNIQUE
        )
    """)

    dbctrl.execute("""
        CREATE TABLE keywords(
            keyword_id INTEGER PRIMARY KEY,
            keyword TEXT NOT NULL UNIQUE
        )
    """)

    dbctrl.execute("""
        CREATE TABLE skills(
            skill_id INTEGER PRIMARY KEY,
            skill TEXT NOT NULL UNIQUE
        )
    """)

    ## RELATIONS TABLE
    dbctrl.execute("""
        CREATE TABLE job_tag(
            tag_id INTEGER,
            job_id INTEGER,
            PRIMARY KEY (tag_id, job_id)
            FOREIGN KEY (tag_id)
                REFERENCES tags (tags_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            FOREIGN KEY (job_id)
                REFERENCES jobs (job_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
        )
    """)

    dbctrl.execute("""
        CREATE TABLE company_keyword(
            keyword_id INTEGER,
            company_id INTEGER,
            PRIMARY KEY (keyword_id, company_id)
            FOREIGN KEY (keyword_id)
                REFERENCES keywords (keyword_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            FOREIGN KEY (company_id)
                REFERENCES companies (company_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
        )
    """)

    dbctrl.execute("""
        CREATE TABLE user_keyword(
            user_id INTEGER,
            keyword_id INTEGER,
            PRIMARY KEY (user_id, keyword_id)
            FOREIGN KEY (user_id)
                REFERENCES users (user_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            FOREIGN KEY (keyword_id)
                REFERENCES keywords (keywords_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
        )
    """)

    dbctrl.execute("""
        CREATE TABLE user_skill(
            user_id INTEGER,
            skill_id INTEGER,
            PRIMARY KEY (user_id, skill_id)
            FOREIGN KEY (user_id)
                REFERENCES users (user_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            FOREIGN KEY (skill_id)
                REFERENCES skills (skill_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
        )
    """)

    # stores all company reviews NEEDS TO BE MADE link w/ company_id
    dbctrl.execute("""
        CREATE TABLE reviews(
            review_id PRIMARY KEY,
            company_id INTEGER,
            review TEXT,
            FOREIGN KEY (company_id)
                REFERENCES company (company_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
        )
    """)

def fillJobs():
    
    # yea idk i just wanted to test it out :) add more as needed
    jobData = [
        (1, 'Entry Level Software Engineer', 'Software,Entry-level,Programming,Computer Science,Engineering,PathFinder', 1, 'Daytona Beach', 'FL', 5, 100000, 'idk'),
        (2, 'Project Manager', 'Project Management,Manager,Software,Engineering,PathFinder', 1, 'Daytona Beach', 'FL', 1000000, 2000000, 'manage the projects duh')
    ]
    
    dbctrl.executemany("""
    INSERT or IGNORE INTO jobs VALUES
        (?,?,?,?,?,?,?,?,?)
    """,jobData)

    #commits insert changes
    db.commit()

def fillCompanies():

    # yea idk i just wanted to test it out :) add more as needed
    companyData = [
        (1,'PathFinder', 'Technology', 'The PathFinder company is the best company in the world',5.0,4.9,4.8,4.7,4.6,4.5)
    ]
    keywordData = [
        (1,'Work-Life Balance'),
        (2,'Flat Hierarchy'),
        (3,'Family-like'),
        (4,'Opportunity')
    ]
    dbctrl.executemany("""
        INSERT or IGNORE INTO companies VALUES
            (?,?,?,?,?,?,?,?,?,?)
    """,companyData)

    dbctrl.executemany("""
        INSERT or IGNORE INTO keywords VALUES
            (?,?)
    """,keywordData)

    company_keywordData = [
        (1,1),
        (2,1),
        (3,1),
        (4,1)
    ]

    dbctrl.executemany("""
        INSERT or IGNORE INTO company_keyword VALUES
            (?,?)
    """,company_keywordData)

    #commits insert changes
    db.commit()

def fillUser():

    # add more as needed
    userData = [
        #User skills, pref. location, keywords
        (1, 'luv2code', 'Passcode123%', 'work-life balance,vacation,benefits', 'python, programming, soft skills', 'New York', 'NY', 70000, 100000),
        (2, 'NGNeer365', 'J1mmyJ@hns', 'healthy deadlines,communication,recognition', 'matlab, leadership, microsoft', 'Huntsville', 'AL', 90000, 150000)
    ]
    dbctrl.executemany("""
    INSERT or IGNORE INTO users VALUES
        (?,?,?,?,?,?,?,?,?)
    """,userData)

    #commits insert changes
    db.commit()

#runs functions
deleteOldDatabases() # duh
reinitMainDatabase() #reinitiates tables
#fillCompanies() #fills company database with fake test companies
#fillJobs() #fills job database with fake test jobs
#fillUser() # fills user database with fake test users
#fillReviews() #fills review database w/ company relations
#relateJobsCompanies() #fills job_company database

db.close()