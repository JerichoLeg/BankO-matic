#*

#*
import sqlite3
import login

with sqlite3.connect("Registration.db") as db:
    cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user(userID INTEGER PRIMARY KEY, FName VARCHAR(20) NOT NULL,
LName VARCHAR(20) NOT NULL,UserName VARCHAR(20) NOt NULL, Password VARCHAR(20) NOT NULL);''')

cursor.execute("""INSERT INTO user(FName,LName,UserName, Password)VALUES("John","Gascon","User_Testing","password")""")
db.commit()


def newUser():
    found = 0
    while found == 0:
        FName = input("First Name: ")
        LName = input("Last Name: ")
        UserName = input("Please Enter a username: ")
        with sqlite3.connect("Registration.db") as db:
            cursor = db.cursor()
            finduser = "SELECT * FROM user WHERE UserName = ?"
            cursor.execute(finduser,[(UserName)])
        if cursor.fetchall():
            print("That username already Exist! Please Try Again")
        else:
            found = 1

        Name = input("Enter Name: ")
        Password = input("Enter Password: ")
        Password1 = input("Enter Password Again: ")

        while Password != Password1:
            print("Sorry your password does not match at all. Try Again")
            Password = input("Enter Password: ")
            Password1 = input("Enter Password Again: ")
        insertData = '''INSERT INTO user(FName, LName, UserName, Password) VALUES(?,?,?)'''
        cursor.execute(insertData, [FName, LName, UserName, Password])
        db.commit()



newUser()
cursor.execute("SELECT *  FROM user;")
print(cursor.fetchall())

