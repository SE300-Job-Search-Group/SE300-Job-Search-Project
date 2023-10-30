from user import User

tempUser = User()

loginSuccess = tempUser.login('luv2code','Passcode123%')
print('Login?: '+str(loginSuccess))

print('User ID: ',tempUser.getID())
print('Username: ',tempUser.getUsername())
print('User Password: Nice try :)')
print('User Keywords: ', tempUser.getKeywords())
print('User Skills: ', tempUser.getSkills())
print('User Location: ',tempUser.getLocation())
print('User Salary: ',tempUser.getSalaryRange())
