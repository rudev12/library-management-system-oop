import time
def admin(username,password):
    username_0 = "adminrudev12"
    password_1 ="rudev12"
    if username == username_0 and password == password_1:
       print("Welcome back,Admin!")
       return True 
    else:
        print("Authentication Failed!")
        return False

def front_desk(username,password):
    username_0 ="deskrudev12"
    password_1 ="rudev123"
    if username == username_0 and password == password_1:
        print("Welcome back!")
        return True  
    else:
        print("Authentication Failed!")
        return False

def login():
    while True:
        print("======= Login =======")
        print(" 1.Login As Admin")
        print(" 2.Login As Front Desk\n")

        choice = input("Enter Choice: ")

        if choice == "1":
            max_attempts = 5
            attempts = 0
            while attempts < max_attempts:
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                if admin(username,password):
                    return "admin"
                else:
                    attempts +=1
                    remaining_attempts = max_attempts -  attempts

                    if attempts == 3:
                        lock_time = 30
                        print("3 Attempts Failde. Security Lockout  Active!")

                        for sec in range(lock_time,0,-1):
                            print(f"Try Again In {sec} seconds...",end="\r")
                            time.sleep(1)

                    if remaining_attempts > 0:
                        print(f"Attempts remaining:{remaining_attempts}\n")
                    else:
                        print("Too Many Failed Attempts, Your Account is Blocked!")

        elif choice =="2":
            max_attempts = 5
            attempts = 0
            while attempts < max_attempts:
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                if front_desk(username,password):
                    return "front_desk"
                else:
                    attempts +=1
                    remaining_attempts =  max_attempts - attempts
                    if attempts == 3:
                        lock_time = 30 
                        print("3 Attempts Failde. Security Lockout  Active!")

                        for sec in range(lock_time,0,-1):
                            print(f"Try Again In {sec} seconds...",end="\r")
                            time.sleep(1)
                if remaining_attempts > 0:
                    print(f"Attempts remainig:{remaining_attempts}\n")
                else:
                    print("Too Many Failed Attempts, Your Account is Blocked!")
        else:
            print("Invalid Input!")
