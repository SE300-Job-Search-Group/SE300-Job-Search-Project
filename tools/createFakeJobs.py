import sqlite3

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
