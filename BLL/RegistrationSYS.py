##################
# John Alfred Gascon
# CpE106L-B3
##################

# Objectives
# Create Registration system
# Create path way LogIN to Registration Using from * import *
# Classes and Objevtives

import sqlite3


class Register:
    def __init__(self):
        with sqlite3.connect('Registration.db') as self.db:
            self.cursor = self.db.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user(userID INTEGER PRIMARY KEY, FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,UserName VARCHAR(20) NOt NULL, Password VARCHAR(20) NOT NULL);''')
        Con = self.db.fetchone()

        self.cursor.execute("""INSERT INTO user(FName,LName,UserName, Password)VALUES("John","Gascon","User_Testing",
    "password")""")
        self.db.commit()

    def newUser(self):
        found = 0
        while found == 0:
            UserName = input("Please Enter a username: ")
            with sqlite3.connect('Registration.db') as db:
                cursor = db.cursor()
                finduser = "SELECT * FROM user WHERE UserName = ?"
                cursor.execute(finduser, [(UserName)])
            if cursor.fetchall():
                print("That username already Exist! Please Try Again")
            else:
                found = 1

    def EndDB(self):
        self.db.close()
