import sqlite3
from dbConnect import connect
import getpass
import texttable as tt

class dataOwner(connect):
    def validasipass(self,a,c):
        self.__a = a
        self.__c = c
        query = "SELECT * FROM owner"
        result = self.executeSelectOne(query)
        if result[2] == self.__a and result[3] == self.__c:
            return True
        else:
            return False

    def validasi(self):
        query = "SELECT * FROM owner"
        res = self.executeSelectOne(query)
        return (res)

    def show(self):
        query = "SELECT idowner,namaowner FROM owner"
        self.res = self.executeSelectOne(query)
        print(self.res)

    def insert(self,a,b,c,d,e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.query = "INSERT INTO owner(namaowner, usernameowner, passowner, alamat, contact) VALUES('{}', '{}', '{}', '{}','{}')".format(self.a,self.b,self.c,self.d,self.e)
        self.execute(self.query)
        print("Owner Telah Terdaftar")

    def updateakun(self):
        pilihid = str(input("\nPilih Id Owner => "))
        username = str(input("\nMasukkan Username Yang Baru => "))
        password = str(getpass.getpass("\nMasukkan Password Yang Baru => "))
        self.query = "UPDATE `owner` SET usernameowner = '{}', password = '{}' WHERE idowner= '{}'".format(username,password,pilihid)
        print("Data Berhasil Diubah")