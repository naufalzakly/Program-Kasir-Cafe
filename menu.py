import sqlite3
from dbConnect import connect
import getpass
import texttable as tt

class dataMenu(connect):
    def getHarga(self,a):
        self.a = a
        self.query = "SELECT hargaMenu FROM Menu WHERE idMenu= '{}' ".format(self.a)
        self.res = self.executeSelectOne(self.query)
        return int(self.res[0])

    def namaMenu(self,b):
        self.b = b
        self.query = "SELECT namaMenu FROM `produk` WHERE idMenu= '{}' ".format(self.b)
        self.res = self.executeSelectOne(self.query)
        return self.res[0]

    def show(self):
        query = ("SELECT * FROM Menu")
        self.res = self.executeSelect(query)
        tab = tt.Texttable()
        produk = [[]]
        for x in self.res:
            produk.append([x[0],x[1],x[2]])
        tab.add_rows(produk)
        tab.set_cols_align(['c','c','c'])
        tab.header(['ID Produk', 'Nama Produk', 'Harga'])
        print(tab.draw())

    def insert(self, namamenu, hargamenu):
        query = "INSERT INTO karyawan (namamenu, hargamenu) \
            VALUES (\'%s\', \'%s\')"
        query = query % (namamenu, hargamenu)
        self.execute(query)
        print("Data Berhasil Ditambahkan")

    def updateHarga(self):
        self.show()
        pilihid = str(input("\nPilih Id Produk => "))
        query = "SELECT idmenu,namamenu,hargamenu FROM menu WHERE idmenu = '{}'".format(pilihid)
        self.__res = self.executeSelectOne(query)
        print("\nId Menu \t\t= '{}' \nNama Menu \t\t= '{}' \nHarga Menu \t\t= '{}'".format(self.__res[0],self.__res[1],self.__res[2]))
        harga = str(input("\nMasukkan Harga Baru => "))
        self.__query = "UPDATE menu SET hargamenu = '{}' WHERE idmenu= '{}'".format(harga,pilihid)
        self.execute(self.__query)
        print("\nHarga Berhasil Diubah")

    def updateNama(self):
        self.show()
        pilihid = str(input("\nPilih Id Produk => "))
        query = "SELECT idmenu,namamenu,hargamenu FROM menu WHERE idmenu = '{}'".format(pilihid)
        self.__res = self.executeSelectOne(query)
        print("\nId Menu \t\t= '{}' \nNama Menu \t\t= '{}' \nHarga Menu \t\t= '{}'".format(self.__res[0],self.__res[1],self.__res[2]))
        nama = str(input("\nMasukkan Nama Menu Baru => "))
        self.query = "UPDATE menu SET namamenu= '{}' WHERE idmneu = '{}'".format(nama,pilihid)
        self.execute(self.query)
        print("\nNama Menu Berhasil Diubah")

    def updateall(self):
        self.show()
        pilihid = str(input("\nPilih Id Produk => "))
        query = "SELECT idmenu,namamenu,hargamenu FROM menu WHERE idmenu = '{}'".format(pilihid)
        self.__res = self.executeSelectOne(query)
        print("\nId Menu \t\t= '{}' \nNama Menu \t\t= '{}' \nHarga Menu \t\t= '{}'".format(self.__res[0],self.__res[1],self.__res[2]))
        nama = str(input("\nMasukkan Nama Produk Baru => "))
        harga = str(input("\nMasukkan Harga Baru => "))
        self.__query = "UPDATE `produk` SET namabarang = '{}', hargabarang = '{}' WHERE idbarang = '{}'".format(nama,harga,pilihid)
        self.execute(self.__query)
        print("\nData Produk Berhasil Diubah")

    def delete(self):
        self.show()
        pilihid = str(input("\nPilih Id Produk => "))
        self.__query = "DELETE FROM `produk` WHERE idbarang = '{}'".format(pilihid)
        self.execute(self.__query)
        print("\nData Berhasil Dihapus")
