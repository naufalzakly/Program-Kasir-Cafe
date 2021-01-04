import sqlite3
from dbConnect import connect


class Cafe(connect):
    def getDataCafe(self):
        query = 'SELECT * from cafe '
        result = self.executeSelect(query) #print(result)
        for row in result:
            return"Nama Cafe \tAlamat cafe \t\tContact Person \n{} \t {} \t\t {}".format(row[0],row[1],row[2])
class Menu(connect):
    def getDataMenu(self):
        query = 'SELECT * from menu '
        result = self.executeSelect(query) #print(result)
        print('Nomor \t\tNama Menu \t\tHarga \t\tStock')
        for row in result:
            print(row[0], '\t\t',row[1], '\t\t',row[2], '\t\t',row[3])
class Ownerr(connect):    
    def getDataOwner(self):
        query = 'SELECT * from owner '
        result = self.executeSelect(query) #print(result)
        for row in result:
            return "Nomor \t Nama Owner \t\t Alamat \t\t Contact Person \n{} \t {} \t\t {} \t\t {} ".format(row[0],row[1],row[2],row[3])
class Karyawan(connect): 
    def getDataKaryawan(self):
        query = 'SELECT * from karyawan '
        result = self.executeSelect(query) #print(result)
        print("Nomor \tNama Karyawan \t\tAlamat \t\tGaji \t\tTahun Masuk")
        for row in result:
            print(row[0], '\t\t',row[1], '\t\t',row[2], '\t\t',row[3], '\t\t',row[4])
class Nota(connect):
            
    def setDataNota(self, nomor, nama_pemesan, nama_menu, harga, nama_karyawan):
        self.query = 'INSERT INTO nota(nomor, nama_pemesan, nama_menu, harga, nama_karyawan) \
            VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'
        self.query = self.query % (nomor, nama_pemesan, nama_menu, harga, nama_karyawan)
        print('self.query:  ', self.query)
        self.executeInsert(self.query)
    def getDataNota(self):
        query = 'SELECT * from nota '
        result = self.executeSelect(query) #print(result)
        print("Nomor \t Nama Pemesan \t\tNama Menu \t\t harga")
        for row in result:
            print(row[0],"\t\t",row[1], "\t\t",row[2], "\t\t",row[3])


# menuAll = Menu()
# menuAll.getDataMenu()

# menu1= Menu()
# nomor = '1'
# nama = 'teh panas'
# harga = '5000'
# stock = '10'
# menu1.setDataMenu(nomor, nama, harga, stock)
# print(menu1)

# list_menu = menu1.getDataMenu()