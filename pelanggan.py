import sqlite3
from dbConnect import connect
import getpass
import texttable as tt


class dataPelanggan(connect):
    def cekNama(self,a):
        self.a = a
        self.query = "SELECT namapelanggan FROM pelanggan WHERE namapelanggan = '{}'".format(self.a)
        self.res = self.executeSelectOne(self.query)
        return self.res

    def cekid(self,a):
        self.a = a
        self.query = "SELECT idpelanggan FROM pelanggan WHERE namapelanggan = '{}' ".format(self.a)
        self.res = self.executeSelectOne(self.query)
        return self.res[0]

    def show(self):
        query = "SELECT * FROM pelanggan"
        self.res = self.executeSelect(query)
        tab = tt.Texttable()
        pembeli = [[]]
        for x in self.res:
            pembeli.append([x[0],x[1]])
        tab.add_rows(pembeli)
        tab.set_cols_align(['c','c'])
        tab.set_cols_dtype(['a','a'])
        tab.header(['ID pelanggan', 'Nama pelanggan'])
        print(tab.draw())

    def insert(self,a):
        self.__a = a
        self.query = "INSERT INTO pelanggan(namapelanggan) VALUES('{}')".format(self.__a)
        self.execute(self.query)
        print("Berhasil memasukkan data")

    def update(self):
        self.show()
        pilihid = str(input("\nPilih Id Pembeli => "))
        query = ("SELECT idpembeli,namapembeli,telepon,alamat FROM `pembeli` WHERE idpembeli = '{}'".format(pilihid))
        self.__res = self.executeSelectOne(query)
        print("\nId pelanggan \t\t= '{}' \nNama pelanggan \t\t= '{}'".format(self.__res[0],self.__res[1]))
        nama = str(input("\nMasukkan Nama Pembeli => "))
        self.__query = "UPDATE pelanggan SET namapelanggan= '{}' WHERE idpelanggan = '{}'".format(nama,pilihid)
        self.execute(self.__query)
        print("\nData Pembeli Berhasil Diubah")

    def delete(self):
        self.show()
        pilihid = str(input("\nPilih Id pelanggan => "))
        self.__query = "DELETE FROM pelanggan WHERE idpelanggan = '{}'".format(pilihid)
        self.execute(self.__query)
        print("\nData Berhasil Dihapus")