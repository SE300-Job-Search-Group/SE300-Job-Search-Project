from userHandler import UserHandler
from databaseHandler import GenericDatabaseHandler

testUH = UserHandler()
dbh = GenericDatabaseHandler()

print('BEFORE NEW ACC')
print(dbh.getTable("keywords"))
print(dbh.getTable("skills"))
print(dbh.getTable('locations'))
print(dbh.getTable('users'))

# test user  attributes
testUser = 'sungje'
testPass = 'ilovecodingsm'
testKeywords = ['work-life balance','Flat Hierarchy','opportunity','communication','test: sungje keyword']
testSkills = ['python','programming','management','microsoft']
testCity = 'Daytona Beach'
testState = 'FL'
testMinSalary = 1000000000
testMaxSalary = 1000000001

#performing the create account method
testUH.createAccount(testUser,testPass,testKeywords,testSkills,testCity,testState,testMinSalary,testMaxSalary)

print('AFTER NEW ACC')
print(dbh.getTable("keywords"))
print(dbh.getTable("skills"))
print(dbh.getTable('locations'))
print(dbh.getTable('users'))
dbh.close()