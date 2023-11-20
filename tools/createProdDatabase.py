import sqlite3

db = sqlite3.connect("./database/main.db")
dbctrl = db.cursor()

dbctrl.execute("""
    CREATE TABLE locations(
        location_id INTEGER PRIMARY KEY,
        city_name TEXT NOT NULL,
        state_name TEXT NOT NULL,
        latitude REAL,
        longitude REAL,
        UNIQUE(city_name,state_name)
    )
""")

dbctrl.execute("""
    CREATE TABLE industrynames(
        industryname_id INTEGER PRIMARY KEY,
        industryname TEXT NOT NULL UNIQUE
    )
""")

#stores all companies
dbctrl.execute("""
    CREATE TABLE companies(
        company_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        industryname_id INTEGER,
        description TEXT,
        rating_overall REAL,
        rating_worklife REAL,
        rating_paybenefits REAL,
        rating_career REAL,
        rating_management REAL,
        rating_culture REAL,
        FOREIGN KEY (industryname_id)
            REFERENCES industrynames (industryname_id)
                ON UPDATE CASCADE
                ON DELETE SET NULL
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
        url TEXT,
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
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
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
        keyword_id INTEGER,
        user_id INTEGER,
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
        skill_id INTEGER,
        user_id INTEGER,
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