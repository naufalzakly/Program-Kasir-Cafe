import sqlite3
from dbConnect import connect
from karyawan import dataKaryawan
from menu import dataMenu
from transaksi import dataTransaksi
from pelanggan import dataPelanggan
from owner import dataOwner
from datetime import datetime
import getpass
import texttable as tt


class transaksiKasir:
    nama = ""
    namakaryawan = ""
    def namaTransaksi(self):
        self.nama = None
        self.namakaryawan = None
        self.nama = str(input("Input Di Sini => "))
        r = dataPelanggan()
        r.insert(self.nama)


    def tempNama(self,a,b):
        self.nama = a
        self.namakaryawan = b

    def doTransaksi(self):
        get = dataMenu()
        flag = False
        listMenu = []
        listKuantitas = []
        listHarga = []
        while flag == False:
            get.show()
            menu = int(input("Masukkan ID Menu Yang Ingin Dibeli => "))
            listMenu.append(dataMenu)
            kuantitas = int(input("Jumlah yang ingin dipesan => "))
            listKuantitas.append(kuantitas)
            if menu == 1:
                harga = kuantitas * get.getHarga(menu)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = int(input("\nMasukkan Input Di Sini => "))
                if masuk == 1:
                    flag = False
                else:
                    flag = True
            elif menu == 2:
                harga = kuantitas * get.getHarga(menu)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = int(input("\nMasukkan Input Di Sini => "))
                if masuk == 1:
                    flag = False
                else:
                    flag = True
            elif menu == 3:
                harga = kuantitas * get.getHarga(menu)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = int(input("\nMasukkan Input Di Sini => "))
                if masuk == 1:
                    flag = False
                else:
                    flag = True
            elif menu == 4:
                harga = kuantitas * get.getHarga(menu)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = int(input("\nMasukkan Input Di Sini => "))
                if masuk == 1:
                    flag = False
                else:
                    flag = True
            elif menu == 5:
                harga = kuantitas * get.getHarga(menu)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = int(input("\nMasukkan Input Di Sini => "))
                if masuk == 1:
                    flag = False
                else:
                    flag = True
            elif menu == 6:
                harga = kuantitas * get.getHarga(menu)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = int(input("\nMasukkan Input Di Sini => "))
                if masuk == 1:
                    flag = False
                else:
                    flag = True
            elif menu == 7:
                harga = kuantitas * get.getHarga(menu)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = int(input("\nMasukkan Input Di Sini => "))
                if masuk == 1:
                    flag = False
                else:
                    flag = True
            else:
                flag = True

        namaMenu = []
        totalHarga = 0
        kembalian = 0
        data1 = dataPelanggan()
        data2 = dataKaryawan()
        data3 = dataTransaksi()
        idpelanggan = data1.cekid(self.nama)
        idkaryawan = data2.cekidkaryawan(self.namakaryawan)

        for i in range(len(listMenu)):
            daftar = str(get.namaMenu(listMenu[i]))
            namaMenu.append(daftar)

        for i in range(len(listHarga)):
            totalHarga += listHarga[i]

        print("\nTotal Keseluruhan Harga Adalah => ", totalHarga)

        bayar = int(input("\nBerapa Uang Yang dibayar? => "))

        kembalian = bayar - totalHarga
        now = datetime.now()
        formatted_date = now.strftime('%d-%m-%Y %H:%M:%S')

        if kembalian >= 0 :
            print("\n================ STRUK PESANAN ====================")
            print("Tanggal Dan Waktu : ", formatted_date) 
            print("Atas Nama : ", self.nama)
            print("Dengan Operator Kasir :", self.namakaryawan)
            print("Nama Produk \t|| Jumlah Pesanan || Jumlah Harga Per Pesan")
            print("--------------------------------------------------")
            for i in range(len(namaMenu)):
                print(namaMenu[i],"\t\t", listKuantitas[i],"\t\t", listHarga[i])
            print("--------------------------------------------------")
            print("Total Harga : \t\t\t\t", totalHarga)
            print("Kembalian : \t\t\t\t", kembalian)
            for i in range(len(listMenu)):
                data3.insert(idkaryawan,listMenu[i],idpelanggan,listKuantitas[i],listHarga[i])
            print("Terima Kasih, Silahkan kembali lagi")

        else:
            print("Maaf, Anda Tidak Bisa Melanjutkan Pembelian")