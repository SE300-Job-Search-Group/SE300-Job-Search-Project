from databaseHandler import LocDBHandler
from geopy.distance import geodesic
from opencage.geocoder import OpenCageGeocode

class Location:
    def __init__(self):
        self.db = "./database/test.db"
        self.id = None
        self.city = None
        self.state = None
        self.lat = None
        self.long = None

        #for geocoding
        self.key = '48e8e8889636463da3252718e9bfab0a'
    
    #init functions
    def fillByID(self,id:int): #returns new location object filled from input ID
        dbh = LocDBHandler(self.db)
        tempLoc = dbh.searchByID(id)
        if tempLoc is None:
            raise Exception("Database Search Error: No Existing Job with ID")
        else:
            self.id = tempLoc[0]
            self.city = tempLoc[1]
            self.state = tempLoc[2]
            self.lat = tempLoc[3]
            self.long = tempLoc[4]

        dbh.close()
        return self

    def assignID(self,city: str,state: str): #returns a new location object filled out based on input ID NEEDS WORK TO INCLUDE ID ASSIGNING IF LOCATION DOES NOT EXIST
        dbh = LocDBHandler(self.db)
        self.city = city
        self.state = state

        #searches for existing ID

        tempRes = dbh.findID(self.city, self.state)

        if tempRes is not None:
            self.id = tempRes[0]
            self.lat = tempRes[1]
            self.long = tempRes[2]
        else: # creates new location & writes to db
            geocoder = OpenCageGeocode(self.key)
            res = geocoder.geocode(self.city+' '+self.state)
            self.lat = res[0]['geometry']['lat']
            self.long = res[0]['geometry']['lng']

            #write to db
            self.id = dbh.addLocation(self.city,self.state,self.lat,self.long)
            
        dbh.close()
        return self
    
    def distanceFrom(self,loc2):
        return geodesic((self.lat,self.long),(loc2.getLat(),loc2.getLong())).miles

    #functions

    def getLocationName(self):
        return self.city+', '+self.state
    
    def getID(self):
        return self.id

    def getCity(self):
        return self.city
    
    def getState(self):
        return self.state
    
    def getLat(self):
        return self.lat
    
    def getLong(self):
        return self.long
    