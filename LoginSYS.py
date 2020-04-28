##################
#John Alfred Gascon
#CpE106L-B3
##################

# Objectives
# Create LogIN system
# Create path way LogIN to Registration Using from * import *
# Classes and Objevtives
# Last Updated 28/04/2020


import sqlite3



class LogIn():

    def __init__(self, UserName, Password):
        self.UserName = UserName
        self.Password = Password

    def login(self):
        while True:
            username = input("Username: ")
            password = input("Password: ")
            with sqlite3.connect("Registration.db") as db:
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

    # def Registration_Button(self):
    # while False:
