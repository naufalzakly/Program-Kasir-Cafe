import sqlite3
import dbConnect
from login import loginakun
from model import Cafe
from model import Menu
from model import Karyawan
from model import Nota
from model import Ownerr



class main:
    def __init__(self):
        print ("========== SELAMAT DATANG DI Coffie Toffie ==========")

    def mainmenu(self):
        print ("=========== Silahkan Login Sebagai ==========")
        print ("========== 1. Owner", "2. Karyawan ==========")
        print ("=============== 3. Keluar ===================")
        inputan = int(input("Masukan Pilihan : "))
        if  inputan == 1:
            Owner = loginakun(input("Username: "), input("Password: "))
            Owner.info()
            print("===== Anda Login Sebagai Owner =====")
            self.menuowner()
        elif  inputan == 2:
            loginKaryawan = loginakun(input("Username: "), input("Password: "))
            loginKaryawan.info()
            print("===== Anda Login Sebagai Karyawan =====")
            self.menukaryawan()
        elif  inputan == 3:
            exit()
        else:
            print('Anda Salah input')
            self.mainmenu()
            
    def menuowner(self):
        print("\n")
        print ("===================== Masukkan Pilihan Kamu ===================")
        print ("============== 1. Info Cafe", "2. Info Karyawan ===============")
        print ("========== 3. Info Owner", "4. Riwayat Pemesanan ==============")
        print ("=================== 5. Kembali Menu Login =====================")
        inputan = int(input("Masukan Pilihan : "))
        if inputan == 1:
            cafe1 = Cafe()
            print (cafe1.getDataCafe())
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuowner()
        elif inputan == 2:
            karyawan1 = Karyawan()
            print (karyawan1.getDataKaryawan())
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuowner()
        elif inputan == 3:
            owner1 = Ownerr()
            print(owner1.getDataOwner())
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuowner()
        elif inputan == 4:
            riwayat1 = Nota()
            print(riwayat1.getDataNota())
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuowner()
        elif inputan == 5:
            self.mainmenu()
        else:
            print("Anda salah input, kembali lagi ke owner")
            self.menuowner()
        
    def menukaryawan(self):
        global uang
        global kembalian
        global totalsemua
        global jumlah_pesanan
        print("\n")
        print ("===================== Masukkan Pilihan Kamu ===================")
        print ("================== 1. Info Cafe", "2. Info Menu ===============")
        print ("============== 3. Pemesanan", "4. Riwayat Pemesanan ===========")
        print ("==================== 6. Kembali ke Menu Login =================")
        inputan = int(input("Masukan Pilihan : "))
        if inputan == 1:
            cafe1 = Cafe()
            print (cafe1.getDataCafe())
            print("Program selesai, kembali ke menu sebelumnya")
            self.menukaryawan()
        elif inputan == 2:
            menuAll = Menu()
            print(menuAll.getDataMenu())
            print("Program selesai, kembali ke menu sebelumnya")
            self.menukaryawan()
        elif inputan == 3:
            totalsemua=0
            print('\nSilahkan Melakukan Pemesanan:')
            nomor = input('Masukkan nomor: ')
            nama_pemesan = input('Masukkan Nama Pelanggan: ')
            nama_karyawan = input("Masukan nama Karyawan")
            nama_menu = input('Masukkan Menu yang dipesan: ')
            jumlah_pesanan = int(input('Anda Mau Memesan berapa? '))
            harga = int(input('Masukkan harga Menu: '))
            totalsemua = jumlah_pesanan * harga
            uang=int(input("Uang Tunai Pembeli: Rp."))
            kembalian=int(uang-totalsemua)
            nota1 = Nota()
            nota1.setDataNota(nomor, nama_pemesan, nama_menu, harga, nama_karyawan)
            print(nota1)
            print("=================================")
            print("======= S T R U K   B E L I =====")
            print("=================================")
            print("#Nama Menu :",nama_menu,"              #")
            print("#Tagihan : Rp.",totalsemua,"           #")
            print("#Uang : Rp.",uang,"              #")
            print("#Kembalian : Rp.",kembalian,"          #")
            print("=================================")
            print("=================================")
            
            print("Program selesai, kembali ke menu sebelumnya")
            self.menukaryawan()
        elif inputan == 4:
            riwayat1 = Nota()
            print(riwayat1.getDataNota())
            print("Program selesai, kembali ke menu sebelumnya")
            self.menukaryawan()
        elif inputan == 6:
            self.mainmenu()
        else:
            print("Anda salah input, kembali lagi ke menu karyawan ")
            self.menukaryawan()    
        

main = main()
main.mainmenu()

