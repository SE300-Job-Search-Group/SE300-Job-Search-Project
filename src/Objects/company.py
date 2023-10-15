import user
import sqlite3

class company:
    def __init__(self,id):
        self.id = id

    def getId(self):
        return self.id

    def userMatch(self,usr: user) -> float:
        return 1 #should return match ranking 