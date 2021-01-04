import sqlite3
from sqlite3 import Error

class connect:
    def __init__(self):
        self.con  = None

    def executeInsert(self,query):
        try:
            self.con = sqlite3.connect('myDb.db')
            cursor = self.con.cursor()
            cursor.execute(query)
            self.con.commit()
            print("success")
        except Error as e:
            print(e)

    def executeSelect(self,query):
        try:
            self.con = sqlite3.connect('myDb.db')
            cursor = self.con.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            print("success")
            return record
        except Error as e:
            print(e)

