from location import Location
from databaseHandler import GenericDatabaseHandler

dbh = GenericDatabaseHandler()

#writing new location
"""
print("BEFORE NEW LOC:"+str(dbh.getTable('locations')))

tempCity = "San Francisco"
tempState = "CA"

tempLoc = Location().assignID(tempCity,tempState)

print("AFTER NEW LOC:"+str(dbh.getTable('locations')))

print("===========================================")
print("ID: "+str(tempLoc.getID()))
print("LOCATION: "+tempLoc.getLocationName())
print("LATITUDE: "+str(tempLoc.getLat()))
print("LONGITUDE: "+str(tempLoc.getLong()))
"""

#comparing location
sanfran = Location().assignID("San Francisco", "CA")
newyork = Location().assignID("New York","NY")

print(sanfran.getLat())
print(newyork.getLat())


distance = sanfran.distanceFrom(newyork)

print(distance,type(distance))