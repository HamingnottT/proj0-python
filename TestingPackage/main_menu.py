import re
import os
from TestingPackage import connection, sql_queries
from TestingPackage import sub_menus

print("="*48 + "\nmain_menu.py running\n" + "="*48)

print("-"*48)
print("\nHello, This is my first programming project that will log your website sign-in data for easy recall."
"\n\nWARNING: Authentication required before proceeding - please sign in.\n")
print("-"*48)

def sign_in():
    # sign_in = False

    # sign_in_attempts = 0
    # while sign_in_attempts < 3:

    # input_user_name = input("Username: ")
    # input_password = input("Password: ")

    input_user_name = "HamingnottT"
    input_password = "NotMyPassword"
    
    try:
        (name, password) = sql_queries.sign_in_query(input_user_name, input_password)
    except UnboundLocalError:
        print("\nUsername or Password entered does not match any records. Please try again:\n")
        return sign_in()
    finally:
        pass
    
    if input_user_name == str(name) and input_password == str(password):
        print("-"*48)
        print(f"\nWelcome in {name}!\n")

        # creates a temporary log to store username and password to resuse in other functions and modules
        access_log_formatter = f"{name},{password}"
        access_logs = open(r"!Logs/AccessLogs.txt","w+")
        access_logs.writelines(access_log_formatter)
        access_logs.close()

        main_menu()
    else:
        print(f"{str(name)} and {str(password)} are the outputs of the tuple")

    
    
def main_menu():

    def main_options():
        print("What information are you looking for today?\n\n"
            "1 = Websites \n"
            "2 = Usernames & Passwords \n"
            "3 = Email \n"
            "0 = Cancel & Exit \n")

    main_options()
    option = int(input("Input here: "))

    while option != 0:
        if option == 1:
            sub_menus.websites()  
        elif option == 2:
            sub_menus.user()   
        elif option == 3:
            sub_menus.email()  
        else:
            print("\nInvalid response, please try again.\n")

        print("\n")
        main_options()
        option = int(input("Input here: "))
    
    print("\nEnding program. . .\n")
    os.remove("!Logs/AccessLogs.txt")

if __name__ == '__main__':
    print("Calling main_menu.py")
    sign_in()