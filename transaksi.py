import sqlite3
from dbConnect import connect
import getpass
import texttable as tt
from datetime import datetime

class dataTransaksi(connect):
    def show(self):
        query = ("SELECT namakaryawan, namamenu namapembeli, kuantitas, totalharga, tanggaltransaksi FROM transaksi JOIN pelanggan ON pelanggan.idpelanggan = transaksi.idpelanggan JOIN karyawan ON karyawan.idkaryawan = transaksi.idkaryawan JOIN menu ON menu.idmenu = transaksi.idmenu ORDER BY tanggaltransaksi DESC")
        self.res = self.executeSelect(query)
        tab = tt.Texttable()
        transak = [[]]
        for x in self.res:
            transak.append([x[0],x[1],x[2],x[3],x[4],x[5]])
        tab.add_rows(transak)
        tab.set_cols_align(['c','c','c','c','c','c'])
        tab.header(['Nama Karyawan', 'Nama Menu', 'Nama Pelanggan', 'Kuantitas', 'Total Harga', 'Tanggal'])
        print(tab.draw())

    def insert(self,a,b,c,d,e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.query = "INSERT INTO transaksi(idkaryawan, idmenu, idpelanggan, kuantitas, totalharga) VALUES('{}', '{}', '{}', '{}', '{}')".format(self.a,self.b,self.c,self.d,self.e)
        self.execute(self.query)

    def delete(self):
        print("\nData Mulai Untuk Dihapus")
        query = ("DELETE FROM `transaksi`")
        self.execute(query)
        print("\nData Berhasil Dihapus Semua")