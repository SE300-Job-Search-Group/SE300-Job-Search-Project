import sqlite3

db = sqlite3.connect("./database/test.db")
dbctrl = db.cursor()

# yea idk i just wanted to test it out :) add more as needed
jobData = [
    (1,'Entry Level Software Engineer', 'PathFinder', 'Daytona Beach','FL','idk'),
    (2,'Project Manager','PathFinder','Daytona Beach', 'FL','manage the projects duh')
]
dbctrl.executemany("""
INSERT or IGNORE INTO jobs VALUES
    (?,?,?,?,?,?)
""",jobData)

#commits insert changes
db.commit()
