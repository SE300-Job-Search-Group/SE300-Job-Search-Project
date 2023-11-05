from databaseHandler import GenericDatabaseHandler
from words import Tag, Keyword, Skill

dbh = GenericDatabaseHandler("./database/test.db")

print(dbh.getTable("tags"))
print(dbh.getTable("keywords"))
print(dbh.getTable("skills"))
print(dbh.getTable('locations'))
print(dbh.getTable('users'))
print(dbh.getTable('user_keyword'))

dbh.close()


# test cases for word addition and search
"""
testTag = Tag().fillbyName('TESTTAG')

print(testTag.getWord())

print(testTag.getID())

testKeyword = Keyword().fillbyName('TESTKEYWORD')

print(testKeyword.getWord())
print(testKeyword.getID()) # assigns id to object from database 

testSkill = Skill().fillbyName('TESTSKILL')

print(testSkill.getWord())
print(testSkill.getID())

testTag = Tag().fillbyName('TESTTAG2')

print(testTag.getWord())

print(testTag.getID())

testKeyword = Keyword().fillbyName('TESTKEYWORD2')

print(testKeyword.getWord())
print(testKeyword.getID()) # assigns id to object from database 

testSkill = Skill().fillbyName('TESTSKILL2')

print(testSkill.getWord())
print(testSkill.getID())

testSkillByID = Skill().fillByID(2)

print('TEST fillbyid(2)')
print(testSkillByID.getWord())

testSkillbyName = Skill().fillbyName('TESTSKILL')

print("Test fillbyName('TESTSKILL')")
print(testSkillbyName.getID())
"""