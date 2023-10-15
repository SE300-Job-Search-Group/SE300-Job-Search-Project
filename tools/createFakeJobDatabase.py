import sqlite3

db = sqlite3.connect("./database/test.db")

dbctrl = db.cursor()

dbctrl.execute("""
INSERT INTO jobs VALUES
(1,'Entry Level Software Engineer', 'PathFinder', 'Daytona Beach','FL','idk')
""")

#commits insert changes
db.commit()
