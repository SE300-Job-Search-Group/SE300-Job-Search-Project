import sqlite3

class GenericDatabaseHandler:
    def __init__(self):
        dir = "./database/main.db"
        self.db = sqlite3.connect(dir)
        self.dbctrl = self.db.cursor()
    
    #Generic Commands
    def close(self): #commits and closes the sqlite connection. SHOULD BE RUN EVERY TIME YOU OPEN A HANDLER
        self.db.commit()
        self.db.close()

    def getTable(self,table: str): #general function to read tables
        tempResults = self.dbctrl.execute('SELECT * FROM '+table)
        tableData = tempResults.fetchall()
        return tableData

class WordsDBHandler(GenericDatabaseHandler):

    def searchByID(self,id: int, type:str) -> str: #searches tag,keyword,skill data base for a specific ID. returns the associated word
        table_name = type+'s'
        col_id = type+'_id'
        tempResults = self.dbctrl.execute("SELECT "+type+" FROM "+table_name+" WHERE EXISTS (SELECT "+col_id+" FROM "+table_name+" WHERE "+col_id+" = '"+str(id)+"') AND "+col_id+" = '"+str(id)+"'")
        
        tempName = tempResults.fetchone()
        if tempName is None:
            return None
        else:
            return tempName[0]

    def findID(self,name: str,type: str) -> int: #finds id based on word provided (for tag, keyword, and skills db)
        table_name = type+'s'
        col_id = type+'_id'

        tempResults = self.dbctrl.execute("SELECT "+col_id+" FROM "+table_name+" WHERE EXISTS (SELECT "+col_id+" FROM "+table_name+" WHERE "+type+" LIKE '"+name+"') AND "+type+" = '"+name+"'")
        tempID = tempResults.fetchone()
        if tempID is None:
            return None
        else:
            return tempID[0]

    def assignID(self,name: str,type: str) -> int: #assigns new id for a word
        table_name = type+'s'
        col_id = type+'_id'

        #finds new ID
        tempResults = self.dbctrl.execute('SELECT MAX('+col_id+') FROM '+table_name)
        maxID = tempResults.fetchone()[0]
        if maxID is None:
            maxID = 0
        newID = maxID + 1
        #inserts new tag into database
        self.dbctrl.execute("INSERT INTO "+table_name+" VALUES ("+str(newID)+",'"+name+"')")
        self.db.commit()

        return newID

class LocDBHandler(GenericDatabaseHandler):
    def searchByID(self,id: int):
        tempResults = self.dbctrl.execute("SELECT * FROM locations WHERE EXISTS (SELECT location_id FROM locations WHERE location_id = "+str(id)+") AND location_id = "+str(id))
        
        return tempResults.fetchone()
    
    def addLocation(self,city: str,state: str,lat:float, long: float):
        tempResults = self.dbctrl.execute('SELECT MAX(location_id) FROM locations')
        maxID = tempResults.fetchone()[0]
        if maxID is None:
            maxID = 0
        newID = maxID + 1

        inputStr = "("+str(newID)+",'"+city+"','"+state+"',"+str(lat)+","+str(long)+")"
        self.dbctrl.execute("INSERT OR IGNORE INTO locations VALUES "+inputStr)

        return newID

    def findID(self,city:str,state:str)-> int:
        tempResults = self.dbctrl.execute("SELECT location_id,latitude,longitude FROM locations WHERE EXISTS (SELECT location_id FROM locations WHERE city_name = '"+city+"' AND state_name = '"+state+"') AND city_name = '"+city+"' AND state_name = '"+state+"'")
        return tempResults.fetchone()
    
class CompanyDBHandler(GenericDatabaseHandler):
    def searchByID(self, id: int):
        tempResults = self.dbctrl.execute("SELECT * FROM companies WHERE EXISTS (SELECT company_id FROM companies WHERE company_id = "+str(id)+") AND company_id = "+str(id))
        
        return tempResults.fetchone()
    
    def searchByName(self,name:str):
        tempResults = self.dbctrl.execute("SELECT * FROM companies WHERE EXISTS (SELECT name FROM companies WHERE name = '"+name+"') AND name = '"+name+"'")
        
        return tempResults.fetchone()
    
    def findKeywordIDs(self,id: int) -> list:
        tempResults = self.dbctrl.execute("SELECT keyword_id FROM company_keyword WHERE company_id = " + str(id))

        return tempResults.fetchall()
    
    def writeCompany(self,name,industry_id,desc,rating,r_wl,r_pb,r_cr,r_mm,r_ct):
        tempResults = self.dbctrl.execute('SELECT MAX(company_id) FROM companies')
        maxID = tempResults.fetchone()[0]
        if maxID is None:
            maxID = 0
        newID = maxID + 1

        inputStr = "("+str(newID)+",'"+name+"',"+str(industry_id)+",'"+desc+"',"+str(rating)+","+str(r_wl)+","+str(r_pb)+","+str(r_cr)+","+str(r_mm)+","+str(r_ct)+")"
        print('DEBUG (COMPANY INPUT TO DB):'+inputStr)
        self.dbctrl.execute("INSERT OR IGNORE INTO companies VALUES "+inputStr)

        return newID
    
    def findReviews(self,company_id:int):
        tempResults = self.dbctrl.execute("SELECT * FROM reviews where company_id = "+str(company_id))

        return tempResults.fetchall()
    
class ReviewDBHandler(GenericDatabaseHandler):
    def searchByID(self,id:int):
        tempResults = self.dbctrl.execute('SELECT * FROM reviews WHERE review_id = '+str(id))

    def writeReview(self,company_id: int,review:str):
        tempResults = self.dbctrl.execute('SELECT MAX(review_id) FROM reviews')
        maxID = tempResults.fetchone()[0]
        if maxID is None:
            maxID = 0
        newID = maxID + 1
        inputStr = "("+str(newID)+","+str(company_id)+",'"+review+"')"
        self.dbctrl.execute("INSERT OR IGNORE INTO reviews VALUES "+inputStr)

        return newID

class JobDBHandler(GenericDatabaseHandler):
    def searchByID(self, id: int):
        tempResults = self.dbctrl.execute("SELECT * FROM jobs WHERE EXISTS (SELECT job_id FROM jobs WHERE job_id = "+str(id)+") AND job_id = "+str(id))
        
        return tempResults.fetchone()
    
    def writeJob(self,title,company_id,locID,minSal,maxSal,desc,url):
        tempResults = self.dbctrl.execute('SELECT MAX(job_id) FROM jobs')
        maxID = tempResults.fetchone()[0]
        if maxID is None:
            maxID = 0
        newID = maxID + 1

        inputStr = "("+str(newID)+",'"+title+"',"+str(company_id)+","+str(locID)+","+str(maxSal)+","+str(minSal)+",'"+desc+"','"+url+"')"
        print('DEBUG(JOB INPUT TO DB): '+inputStr)
        tempResults = self.dbctrl.execute("INSERT OR IGNORE INTO jobs VALUES "+inputStr)

        return newID
    
    def writeTags(self,tempJobTags):
        self.dbctrl.executemany("""
        INSERT or IGNORE INTO job_tags VALUES
            (?,?)
        """,tempJobTags)

    
    def findTagIDs(self,id: int) -> list:
        tempResults = self.dbctrl.execute("SELECT tag_id FROM job_tag WHERE job_id = " + str(id))

        return tempResults.fetchall()
    
class UserDBHandler(GenericDatabaseHandler):
    def searchByID(self, id:int): #searches for user using ID
        tempResults = self.dbctrl.execute("SELECT * FROM users WHERE EXISTS (SELECT user_id FROM users WHERE user_id= "+str(id)+") AND user_id = "+str(id))

        return tempResults.fetchone()
    
    def validateLogin(self,username: str,password: str) -> int: #basically a login function but should only be used by User object
        # returns None if failed, returns user id if exists
        tempResults = self.dbctrl.execute("""SELECT user_id FROM users WHERE EXISTS (SELECT user_id FROM users WHERE username = '"""+username+"' AND password = '"+password+"') AND username = '"+username+"' AND password = '"+password+"'")

        tempUserID = tempResults.fetchone()

        if tempUserID is not None:
            tempUserID = tempUserID[0]

        return tempUserID
    
    def findKeywordIDs(self,id: int) -> list: #finds keywords associated with the user
        tempResults = self.dbctrl.execute("SELECT keyword_id FROM user_keyword WHERE user_id = " + str(id))

        return tempResults.fetchall()

    def findSkillIDs(self,id:int) -> list: #finds skills associated with user
        tempResults = self.dbctrl.execute("SELECT skill_id FROM user_skill WHERE user_id = "+ str(id))
        
        return tempResults.fetchall()
    
    def findAvailableID(self) -> int: #finds available ID to be assigned to a new user
        tempResults = self.dbctrl.execute('SELECT MAX(user_id) from users')
        maxID = tempResults.fetchone()[0]
        if maxID is None:
            maxID = 0
        return maxID+1
    
    def writeUser(self,id,username,password,location_id,minSalary,maxSalary): #writes a new user to the user table in DB
        inputstr = "("+str(id)+",'"+username+"','"+password+"',"+str(location_id)+','+str(minSalary)+','+str(maxSalary)+')'
        self.dbctrl.execute("""INSERT INTO users  VALUES """+inputstr)
        
    def writeUserKeywords(self,user_kw_list: list): #write user keyword associations to user_keyword table in db
        self.dbctrl.executemany("""
        INSERT or IGNORE INTO user_keyword VALUES
            (?,?)
        """,user_kw_list)

    def writeUserSkills(self,user_skill_list: list): #see writeUserKeywords but for Skills instead
        self.dbctrl.executemany("""
        INSERT or IGNORE INTO user_skill VALUES
            (?,?)
        """,user_skill_list)
        
    def updateUserKeywords(self,id,user_kw_list):
        self.dbctrl.execute("""
            DELETE FROM user_keyword
                WHERE user_id = """ + str(id))
        
        self.writeUserKeywords(user_kw_list)

    def updateUserSkills(self,id,user_skill_list):
        self.dbctrl.execute("""
            DELETE FROM user_skill
                WHERE user_id = """ + str(id))
        
        self.writeUserSkills(user_skill_list)

class JobSearchDBHandler(GenericDatabaseHandler):
    def searchByTags(self,tag_ids: list,numMatches: int)-> list[int]:

        tag_id_phrase = ''
        for id in tag_ids:
            tag_id_phrase = tag_id_phrase +str(id)+","
        tag_id_phrase = tag_id_phrase.rstrip(tag_id_phrase[-1])

        tempResults = self.dbctrl.execute("""
            SELECT job_id FROM job_tag
                WHERE tag_id IN ("""+tag_id_phrase+""") 
                GROUP BY job_id
                HAVING COUNT(*)>="""+str(numMatches)+"""
        """)
        tempOutput = tempResults.fetchall()
        output = []
        for i in tempOutput:
            output.append(i[0])
        
        return output

class TestDBHandler(GenericDatabaseHandler):
    def execute(self,input):
        return self.dbctrl.execute(input)