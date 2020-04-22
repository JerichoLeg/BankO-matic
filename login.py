import sqlite3

    def login():
        while True:
            username = input("Username: ")
            password = input("Password: ")
            with sqlite3.connect("accounts.db") as db:
                cursor = db.cursor()
            find_user =("SELECT * FROM user WHERE username = ? AND password = ?")
            cursor.execute(find_user,[(username),(password)])
            results = cursor.fetchfall()
            
            if results:
                for x in results:
                    print("Welcome " + x[2])
                    
                break
            
            else:
                print("Username and password not recognised")
                again = input("Do you want to try again?(y/n): ")
                #THis part papalitan natin ng GUI so maybe mababago na dito part
                if again.lower() == 'n':
                    print("Good day")
                    time.sleep(1)
                break
login()