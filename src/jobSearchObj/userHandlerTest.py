from userHandler import UserHandler
from databaseHandler import GenericDatabaseHandler

testDB = "./database/test.db"

testUH = UserHandler()
dbh = GenericDatabaseHandler(testDB)

print('BEFORE NEW ACC')
print(dbh.getTable("keywords"))
print(dbh.getTable("skills"))
print(dbh.getTable('locations'))
print(dbh.getTable('users'))

testUser = 'sungje'
testPass = 'ilovecodingsm'
testKeywords = ['work-life balance','Flat Hierarchy','opportunity','communication','test: sungje keyword']
testSkills = ['python','programming','management','microsoft']
testCity = 'Daytona Beach'
testState = 'FL'
testMinSalary = 1000000000
testMaxSalary = 1000000001

testUH.createAccount(testUser,testPass,testKeywords,testSkills,testCity,testState,testMinSalary,testMaxSalary)
print('AFTER NEW ACC')
print(dbh.getTable("keywords"))
print(dbh.getTable("skills"))
print(dbh.getTable('locations'))
print(dbh.getTable('users'))