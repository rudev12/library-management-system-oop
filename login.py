
def admin(username,password):
    username_0 = "adminrudev12"
    password_1 ="rudev12"
    if username == username_0 and password == password_1:
       print("Welcome back,Admin!")
       return True 
    else:
        print("Authentication Failed")
        return False

def front_desk(username,password):
    username_0 ="deskrudev12"
    password_1 ="rudev123"
    if username == username_0 and password == password_1:
        print("Welcome back!")
        return True  
    else:
        print("Authentication Failed")
        return False

def login():
    while True:
        print("======= Login =======")
        print(" 1.Login As Admin")
        print(" 2.Login As Front Desk\n")

        choice = input("Enter Choice: ")

        if choice == "1":
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            if admin(username,password):
                return "admin"

        elif choice =="2":
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            if front_desk(username,password):
                return "front_desk"
        else:
            print("Invalid Input!")
