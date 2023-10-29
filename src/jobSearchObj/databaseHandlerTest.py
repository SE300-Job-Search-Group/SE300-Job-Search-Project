from databaseHandler import GenericDatabaseHandler
from words import Tag, Keyword, Skill

dbh = GenericDatabaseHandler("./database/test.db")

print(dbh.getTable("tags"))
print(dbh.getTable("keywords"))
print(dbh.getTable("skills"))

dbh.close()

testTag = Tag().setWord('TESTTAG')

print(testTag.getWord())

print(testTag.assignID())

testKeyword = Keyword().setWord('TESTKEYWORD')

print(testKeyword.getWord())
print(testKeyword.assignID()) # assigns id to object from database 

testSkill = Skill().setWord('TESTSKILL')

print(testSkill.getWord())
print(testSkill.assignID())

testTag = Tag().setWord('TESTTAG2')

print(testTag.getWord())

print(testTag.assignID())

testKeyword = Keyword().setWord('TESTKEYWORD2')

print(testKeyword.getWord())
print(testKeyword.assignID()) # assigns id to object from database 

testSkill = Skill().setWord('TESTSKILL2')

print(testSkill.getWord())
print(testSkill.assignID())

testSkillByID = Skill().fillByID(2)

print('TEST fillbyid()')
print(testSkillByID.getWord())