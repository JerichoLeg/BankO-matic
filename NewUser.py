##################
# John Alfred Gascon
# CpE106L-B3
##################

# Objectives
# Create Registration system
# Create path way LogIN to Registration Using from * import *
# Classes and Objevtives
# Last Updated 28/04/2020


import sqlite3


class Register:

    def __init__(self, FirstName, LastName, UserName, Password):
        self.FirstName = FirstName
        self.LastName = LastName
        self.UserName = UserName
        self.Password = Password

    with sqlite3.connect("Registration.db") as db:
        cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user(userID INTEGER PRIMARY KEY, FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,UserName VARCHAR(20) NOt NULL, Password VARCHAR(20) NOT NULL);''')

    cursor.execute(
        """INSERT INTO user(FName,LName,UserName, Password)VALUES("John","Gascon","User_Testing","password")""")
    db.commit()

    def newUser(self):
        found = 0
        while found == 0:
            FName = input("First Name: ")
            LName = input("Last Name: ")
            UserName = input("Please Enter a username: ")
            with sqlite3.connect("Registration.db") as db:
                cursor = db.cursor()
                finduser = "SELECT * FROM user WHERE UserName = ?"
                cursor.execute(finduser, [(UserName)])
            if cursor.fetchall():
                print("That username already Exist! Please Try Again")
            else:
                found = 1

            Password = input("Enter Password: ")
            Password1 = input("Enter Password Again: ")
            while Password != Password1:
                print("Sorry your password does not match at all. Try Again")
            insertData = '''INSERT INTO user(FirstName, LastName, UserName, Password) VALUES(?,?,?)'''
            cursor.execute(insertData, [self.FirstName, self.LastName, self.UserName, self.Password])
            db.commit()

    newUser()
    cursor.execute("SELECT *  FROM user;")
    print(cursor.fetchall())
