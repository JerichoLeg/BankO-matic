import sqlite3
with sqlite3.connect("Registration.db") as db:
    cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user(userID INTEGER PRIMARY KEY, username VARCHAR(20) NOT NULL,
Name VARCHAR(20) NOT NULL, Password VARCHAR(20) NOT NULL);''')

cursor.execute("""INSERT INTO user(username,Name,Password)VALUES("test_User","John Gascon","password")""")
db.commit()


def newUser():
    found = 0
    while found == 0:
        username = input("Please Enter a username: ")
        with sqlite3.connect("Registration.db") as db:
            cursor = db.cursor()
            finduser = ("SELECT * FROM user WHERE username = ?")
            cursor.execute(finduser,[(username)])
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
        insertData = '''INSERT INTO user(username, Name, Password) VALUES(?,?,?)'''
        cursor.execute(insertData, [username, Name, Password])
        db.commit()



newUser()
cursor.execute("SELECT *  FROM user;")
print(cursor.fetchall())
