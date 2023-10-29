from databaseHandler import DatabaseHandler
from words import Tag, Keyword, Skill

dbh = DatabaseHandler("./database/test.db")

print(dbh.getTable("tags"))
print(dbh.getTable("keywords"))
print(dbh.getTable("skills"))

testTag = Tag('TESTTAG')

print(testTag.getWord())

print(testTag.assignID())

testKeyword = Keyword('TESTKEYWORD')

print(testKeyword.getWord())
print(testKeyword.assignID()) # assigns id to object from database 

testSkill = Skill('TESTSKILL')

print(testSkill.getWord())
print(testSkill.assignID())

testTag = Tag('TESTTAG2')

print(testTag.getWord())

print(testTag.assignID())

testKeyword = Keyword('TESTKEYWORD2')

print(testKeyword.getWord())
print(testKeyword.assignID()) # assigns id to object from database 

testSkill = Skill('TESTSKILL2')

print(testSkill.getWord())
print(testSkill.assignID())