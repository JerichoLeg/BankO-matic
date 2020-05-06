##################
#John Alfred Gascon
#CpE106L-B3
##################

# Objectives
# Create LogIN system
# Create path way LogIN to Registration Using from * import *
# Classes and Objevtives


import sqlite3

class LogIn():

    def __init__(self):
        with sqlite3.connect('Registration.db') as self.db:
            self.cursor = self.db.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user(userID INTEGER PRIMARY KEY, FirstName VARCHAR(20) NOT NULL,
           LastName VARCHAR(20) NOT NULL,UserName VARCHAR(20) NOt NULL, Password VARCHAR(20) NOT NULL);''')
        Con = self.db.fetchone()

        self.cursor.execute("""INSERT INTO user(FName,LName,UserName, Password)VALUES("John","Gascon","User_Testing",
           "password")""")

        self.UserName = ""
        self.LastName = ""

        self.db.commit()

    def login(self):
        while True:
            username = input("Username: ")
            password = input("Password: ")
            with sqlite3.connect('Registration.db') as db:
                cursor = db.cursor()
            find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
            cursor.execute(find_user, [(username), (password)])
            results = cursor.fetchfall()

            if results:
                for x in results:
                    print("Welcome " + x[2])

                break
            else:
                print("Username and password not recognised")
                break

    def dbClose(self):
        self.db.close()