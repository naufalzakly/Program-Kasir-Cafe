from karyawan import dataKaryawan
from menu import dataMenu
from transaksi import dataTransaksi
from pelanggan import dataPelanggan
from owner import dataOwner
from datetime import datetime
import getpass
from control import transaksikaryawan

class Sistem:
    namakaryawan = ""
    def otentifikasi(self):
        print("\n====== Selamat Datang Di Program Kasir Coffie Toffie======")
        print("Pilih Menu")
        print("1. Login \n2. Signup \n3. Keluar ")
        masuk = int(input("Input Di sini: "))
        if masuk == 1 :
            self.login()
        elif masuk == 2:
            self.signup()
        elif masuk == 3:
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("Input salah. Coba input lagi")
            self.otentifikasi()

    def validasiOwner(self):
        a = dataOwner()
        if a.validasi() == None :
            print ("\n!!!!!! Peringatan !!!!!!")
            print ("Program Ini Tidak Mempunyai Admin.")
            print ("Anda Harus Sign up Menjadi Admin Terlebih Dahulu.")
            print ("1. Signup \n2. Keluar")
            masuk = int(input("Input Di sini: "))
            if masuk == 1:
                self.signupOwner()
            elif masuk == 2:
                print("\n====== Terima Kasih Telah Menggunakan ======")
            else:
                print("Input salah, Coba lagi")
                self.validasiOwner()
        else:
            self.otentifikasi()

    def login(self):
        print("\n=================")
        print("Login Sebagai Apa?")
        print("1. Owner \n2. Karyawan \n3. Menu Utama")
        masuk = int(input("Input Di Sini: "))
        if masuk == 1:
            self.masukOwner()
        elif masuk == 2:
            self.masukKaryawan()
        elif masuk == 3:
            self.otentifikasi()
        else:
            print("Input salah, Coba lagi")
            self.login()

    def signup(self):
        a = dataOwner()
        print("\n=================")
        print("Signup Sebagai Apa?")
        print("1. Ownern \n2. Karyawan \n3. Menu Utama")
        masuk = int(input("Input Di Sini: "))
        if masuk == 1:
            if a.validasi() == None:
                self.signupOwner()
            else:
                print("\nProgram Ini Sudah Memiliki Owner")
                self.signup()
        elif masuk == 2:
            print("Masuk sign up Karyawan")
            self.signupkaryawan()
        elif masuk == 3:
            self.otentifikasi()
        else:
            print("\nInput salah, Coba lagi")
            self.signup()

    def signupOwner(self):
        a = dataOwner()
        b = str(input("Masukkan Nama Owner: "))
        c = str(input("Masukkan Username: "))
        d = str(getpass.getpass("Masukkan Password:"))
        e = str(input("Masukkan Alamat: "))
        f = str(input("Masukkan no Telelpon Anda: "))
        a.insert(b,c,d,e,f)
        print("Selamat Anda Menjadi Owner")
        self.otentifikasi()

    def signupkaryawan(self):
        a = dataKaryawan()
        b = str(input("Masukkan Username: "))
        c = str(input("Masukkan Nama Anda: "))
        d = str(input("Masukkan Alamat Anda: "))
        e = str(getpass.getpass("Masukkan Password=> "))
        a.insert(b,c,d,e)
        print("Selamat Anda Terdaftar Menjadi karyawan")
        self.otentifikasi()

    def masukOwner(self):
        w = dataOwner()
        b = str(input("Masukkan username: "))
        c = str(getpass.getpass("Masukkan Password: "))
        i = 0
        if w.validasipass(b,c) == True:
            self.menuUtama()
        else:
            print("\n!!!! Sepertinya Input Anda Salah. Coba Lagi!!!!!")
            while i<=3 and w.validasipass(b,c) == False:
                b = str(input("Masukkan username: "))
                c = str(getpass.getpass("Masukkan Password: "))
                if w.validasipass(b,c) == True:
                    self.menuUtama()
                else:
                    i += 1 
                    if i > 3:
                        print()
                    else:
                        print("\n!!!! Coba Lagi !!!!!")
            if w.validasipass(b,c) == False:
                print("\n!!!! Sepertinya Anda Lupa Username Dan Password. Coba Ingat Terlebih Dahulu !!!!")
                print("\n!!!! Atau Lakukan Reset Akun Anda Di Database !!!!")

    def masukKaryawan(self):
        w = dataKaryawan()
        self.usernamekaryawan = str(input("Masukkan username: "))
        self.passwordkaryawan = str(getpass.getpass("Masukkan Password: "))
        i = 0
        if w.validasipass(self.usernamekaryawan,self.passwordkaryawan) == True:
            self.cekkaryawan(self.usernamekaryawan,self.passwordkaryawan)
        else:
            print("\n!!!! Sepertinya Input Anda Salah. Coba Lagi !!!!!")
            while i<=3 and w.validasipass(self.usernamekaryawan,self.passwordkaryawan) == False:
                self.usernamekaryawan = str(input("Masukkan username: "))
                self.passwordkaryawan = str(getpass.getpass("Masukkan Password: "))
                if w.validasipass(self.usernamekaryawan,self.passwordkaryawan) == True:
                    self.cekkaryawan(self.usernamekaryawan,self.passwordkaryawan)
                else:
                    i += 1 
                    if i > 3:
                        print()
                    else:
                        print("\n!!!! Coba Lagi !!!!!")
            if w.validasipass(self.usernamekaryawan,self.passwordkaryawan) == False:
                print("\n!!!!Sepertinya Anda Lupa Username Dan Password. Atau Anda Belum Terdaftar Di Program ini!!!!")
                print("\n!!!!Jika Anda Belum Terdaftar, Segera Sign Up Dan Hubungi Admin Program Ini!!!!")
                self.masukKaryawan()
    def cekkaryawan(self,a,b):
        self.a = a
        self.b = b
        f = dataKaryawan()
        self.namakaryawan = f.ceknamakaryawan(self.a,self.b)
        self.menuKaryawan(self.namakaryawan)

    def menuUtama(self):
        print("\n====== Menu Utama ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Menu Karyawan \n2. Daftar Menu \n3. Daftar Pelanggan")
        print("4. Daftar Transaksi \n5. Recovery Admin \n6. Keluar")
        masuk = int(input("Input Di Sini: "))
        if masuk == 1:
            self.adminKaryawan()
        elif masuk == 2:
            self.adminMenu()
        elif masuk == 3:
            self.adminPelanggan()
        elif masuk == 4:
            self.adminTransaksi()
        elif masuk == 5:
            self.recoverAdmin()
        elif masuk == 6:
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.menuUtama()

    def adminKaryawan(self):
        k = dataKaryawan()
        print("\n====== Menu Manipulasi Karyawan ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Daftar Karyawan \n2. Tambah Data Karyawan\n3. Ubah Data Karyawan \n4. Hapus Data Karyawan")
        print("5. Main Menu \n6. Keluar")
        masuk = int(input("\nInput Di Sini: "))
        if masuk == 1:
            k.show()
            self.adminKaryawan()
        elif masuk == 2:
            a = str(input("\nMasukkan Nama Kasir: "))
            b = str(input("\nMasukkan NIK => "))
            c = str(input("\nMasukkan Username Sementara: "))
            d = str(getpass.getpass("\nMasukkan Password Sementara: "))
            k.insert(a,b,c,d)
            k.show()
            self.adminKaryawan()
        elif masuk == 3:
            print("\nPilih Ubah Data")
            print("\n1. Ubah Biodata \n2. Reset Username Dan Password \n3. Return")
            pilihan = int(input("\nInput Di Sini: "))
            if pilihan == 1:
                k.update()
                self.adminKaryawan()
            elif pilihan == 2:
                k.updatepass()
                self.adminKaryawan()
            else:
                self.adminKaryawan()
        elif masuk == 4:
            k.delete()
            self.adminKaryawan()
        elif masuk == 5:
            self.menuUtama()
        elif masuk == 6:
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.adminKaryawan()

    def adminMenu(self):
        p = dataMenu()
        print("\n====== Menu Manipulasi Produk ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Daftar Menu \n2. Tambah Menu\n3. Ubah Data Menu \n4. Hapus Data Menu")
        print("5. Main Menu \n6. Keluar")
        masuk = int(input("Input Di Sini: "))
        if masuk == 1:
            p.show()
            self.adminMenu()
        elif masuk == 2:
            a = str(input("Masukkan Nama Menu: "))
            b = str(input("Masukkan Harga Per Buah: "))
            p.insert(a,b)
            p.show()
            self.adminMenu()
        elif masuk == 3:
            p.updateall()
            self.adminMenu()
        elif masuk == 4:
            p.delete()
            self.adminMenu()
        elif masuk == 5:
            self.menuUtama()
        elif masuk == 6:
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.adminMenu()

    def adminPelanggan(self):
        c = dataPelanggan()
        print("\n====== Menu Manipulasi Pelanggan ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Daftar Pelanggan \n2. Hapus Data Pelanggan \n3. Ubah Data Pelanggan")
        print("4. Main Menu \n5. Keluar")
        masuk = int(input("Input Di Sini: "))
        if masuk == 1:
            c.show()
            self.adminPelanggan()
        elif masuk == 2:
            c.delete()
            self.adminPelanggan()
        elif masuk == 3:
            c.update()
            self.adminPelanggan()
        elif masuk == 4:
            self.menuUtama()
        elif masuk == 5:
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.adminPelanggan()

    def adminTransaksi(self):
        t = dataTransaksi()
        print("\n====== Menu Manipulasi Pelanggan ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Lihat Riwayat Transaksi")
        print("3. Main Menu \n4. Keluar")
        masuk = int(input("Input Di Sini: "))
        if masuk == 1:
            t.show()
            self.adminTransaksi()
        elif masuk == 2:
            print("\nData Akan Dihapus Semua. Anda Yakin?")
            print("\n1. Ya \n2. Tidak")
            pilih = int(input("\nInput Di Sini: "))
            if pilih == 1:
                t.delete()
                self.adminTransaksi()
            else:
                self.adminTransaksi()
        elif masuk == 3:
            self.menuUtama()
        elif masuk == 4:
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.adminTransaksi()

    def recoverAdmin(self):
        m = dataOwner()
        print("\nReset Akun Admin?")
        print("1. Ya \n2. Tidak")
        masuk = int(input("\n Input Di Sini: "))
        if masuk == 1:
            m.updateakun()
            self.menuUtama()
        else:
            self.menuUtama()

    def menuKaryawan(self,a):
        self.a = a
        print("\n====== Menu Utama Kasir ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Transaksi \n2. Lihat Daftar Menu \n3. Keluar")
        masuk = int(input("Input Di Sini: "))
        if masuk == 1:
            self.lakukanTransaksi(self.a)
        elif masuk == 2:
            self.lihatMenu(self.a)
        elif masuk == 3:
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.menuKaryawan(self.a)

    def lakukanTransaksi(self,a):
        self.a = a
        d1 = transaksikaryawan()
        d2 = dataPelanggan()
        nama = str(input("\nMasukkan Nama Pelanggan: "))
        print(d2.cekNama(nama))
        if d2.cekNama(nama) == None:
            d1.namaTransaksi(nama(self.a))
            d1.doTransaksi()
        else:
            d1.tempNama(nama,self.a)
            d1.doTransaksi()
        self.menuKaryawan(self.a)
    
    def lihatMenu(self,a):
        self.a = a
        b = dataMenu()
        b.show()
        print("Menu")
        print("\n1. Kembali Menu Utama")
        masuk = int(input("Input Di Sini => "))
        if masuk == 1:
            self.menuKaryawan(self.a)
        else:
            print("\nInput salah, Coba lagi\n")
            self.lihatMenu(self.a)

p1 = Sistem()
p1.otentifikasi()