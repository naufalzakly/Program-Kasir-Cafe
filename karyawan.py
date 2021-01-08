import sqlite3
from dbConnect import connect
import getpass
import texttable as tt

class dataKaryawan(connect):
    def validasipass(self, a, s):
        self.__a = a
        self.__s = s
        query = "SELECT * FROM karyawan"
        self.result = self.executeSelect(query)
        for x in self.result:
            if x[3] == self.__a and x[4] == self.__s:
                return True
        return False

    def cekidkaryawan(self,a):
        self.a = a
        query = "SELECT idkaryawan FROM `karyawan` WHERE namakaryawan = '{}' ".format(self.a)
        result = self.executeSelectOne(query)
        return result[0]

    def ceknamakaryawan(self, usernama, sandikaryawan):
        self.__usernama = usernama
        self.__sandikaryawan = sandikaryawan
        query = "SELECT namakaryawan FROM `karyawan` WHERE usernamekaryawan = '{}' AND passkaryawan = '{}' ".format(self.__usernama,self.__sandikaryawan)
        result = self.executeSelectOne(query)
        return result[0]

    def show(self):
        query = "SELECT idkaryawan,namakaryawan,gaji,tahun_masuk FROM karyawan"
        resultt = self.executeSelect(query)
        kasir = [[]]
        tab = tt.Texttable(0)
        for x in resultt:
            kasir.append([x[0],x[1],int(x[2])])
        tab.add_rows(kasir)
        tab.header(['ID Karyawan', 'Nama Karyawan', 'Gaji Karyawan', 'Tahun Awal Bekerja'])
        tab.set_cols_align(['c','c','c','c'])
        tab.set_cols_dtype(['a','a','a','a'])
        print(tab.draw())

    def insert(self,usernamekaryawan, passkaryawan, namakaryawan, alamat, gaji, tahun_masuk):
        query = "INSERT INTO karyawan (usernamekaryawan, passkaryawan, namakaryawan, alamat, gaji, tahun_masuk) \
            VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')"
        query = query % (usernamekaryawan, passkaryawan, namakaryawan, alamat, gaji, tahun_masuk)
        self.execute(query)

    def update(self):
        pilihid = str(input("\nPilih Id Karyawan => "))
        nama = str(input("\nMasukkan Nama Karyawan Baru => "))
        alamat = str(input("\nMasukkan Alamat Baru => "))
        gaji = int(input("\nMasukkan Alamat Baru => "))
        tahun = int(input("\nMasukkan Alamat Baru => "))
        query = "UPDATE karyawan SET namakaryawan = '{}', alamat = '{}', gaji= '{}', tahun_masuk= '{}' , WHERE idkaryawan = '{}'".format(nama,alamat,gaji,tahun,pilihid)
        self.execute(query)
        return("\nData Berhasil Diubah")

    def updatepass(self):
        pilihid = int(input("\nPilih Id Karyawan => "))
        username = str(input("\nMasukkan Username Baru => "))
        password = str(getpass.getpass("\nMasukkan Password Baru => "))
        query1= "UPDATE karyawan SET usernamekaryawan = '{}', passkaryawan = '{}' WHERE idkaryawan = '{}'".format(username,password,pilihid)
        self.execute(query1)
        return("\nData Berhasil Diubah")

    def delete(self):
        pilihid = int(input("\nPilih Id Karyawan => "))
        query = "DELETE FROM `karyawan` WHERE idkaryawan = '{}'".format(pilihid)
        self.execute(query)
        print("\nData Berhasil Dihapus")

# ky= dataKaryawan()
# usernama = 'pp'
# passs = '123'
# nama = 'ppp'
# alamatt = "ok"
# gaji = "20"
# tahun = "22"
# ky.insert(usernama, passs, nama, alamatt, gaji, tahun)
# ky.delete()
# print(ky)
