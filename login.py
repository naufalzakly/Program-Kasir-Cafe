import sqlite3
import dbConnect


class loginakun:
    
    def __init__(self, Username, Password):
        pass
    def info(self):
        pass

class loginKaryawan (loginakun):
    def __init__ (self, Username, Password):
        self.Username = Username
        self.Password = Password

    def info(self):
        return "Username: {}\nPassword: {}".format(self.Username,self.Password)

class loginOwner (loginakun):
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

    def info(self):
        return "Username : {}\nPassword: {} ".format(self.Username,self.Password)