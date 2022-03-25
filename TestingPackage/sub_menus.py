from TestingPackage import sql_queries

print("="*48 + "\nsub_menu.py running\n" + "="*48)

def websites():
    # opens the access log created in main_menu.sign_in(), and recreates a list(not tuple) for use in this function
    access_logs = open(r"!Logs/AccessLogs.txt","r")
    access_logs.seek(0)
    access_log_list = (access_logs.read()).split(",")

    name = access_log_list[0]
    password = access_log_list[1]

    print("\n" + "-"*48 + "\n")
    def sub_options():
        print("Website option selected. Please input one of the numbers into the field below:\n\n"
                "1 = Add Website to Database \n"
                "2 = Find a Specific Website \n"
                "3 = Get All Websites \n"
                "4 = Edit Website Name \n"
                "5 = Delete Website Info \n"
                "0 = Exit To Main Menu \n")

    sub_options()
    option = int(input("Input here: "))

    while option != 0:
        if option == 1:
            sql_queries.create_website()
        elif option == 2:
            sql_queries.get_Certain_Website()
        elif option == 3:
            print("\n")
            sql_queries.get_all_websites()
            print(f"\nReturned all websites from database under user {name}. Returning to menu. . .")
        elif option == 4:
            sql_queries.update_website()
        elif option == 5:
            sql_queries.del_website() 
        else:
            print("\nInvalid response, please try again.\n")

        print("\n")
        sub_options()
        option = int(input("Input here: "))

    access_logs.close()

    # end of function returns to main screen
    print("-"*48 + "\nWelcome back to the main screen:\n" + "-"*48)

def user():
    # opens the access log created in main_menu.sign_in(), and recreates a list(not tuple) for use in this function
    access_logs = open(r"!Logs/AccessLogs.txt","r")
    access_logs.seek(0)
    access_log_list = (access_logs.read()).split(",")

    name = access_log_list[0]
    password = access_log_list[1]

    print("\n" + "-"*48 + "\n")
    def sub_options():
        print("Usernames & Passwords option selected. Please input one of the numbers into the field below:\n\n"
                "1 = Update Username of a Website \n"
                "2 = Find Websites by Username \n"
                "3 = Update a Password \n"
                "4 = Go to Websites  \n"
                "0 = Exit To Main Menu \n")
    
    sub_options()
    option = int(input("Input here: "))

    while option != 0:
        if option == 1:
            sql_queries.update_user()
        elif option == 2:
            sql_queries.get_all_user()   
        elif option == 3:
            sql_queries.update_pass()
        elif option == 4:
            websites()
        else:
            print("\nInvalid response, please try again.\n")

        print("\n")
        sub_options()
        option = int(input("Input here: "))

    access_logs.close()

    # end of function returns to main screen
    print("-"*48 + "\nWelcome back to the main screen:\n" + "-"*48)

def email():
    # opens the access log created in main_menu.sign_in(), and recreates a list(not tuple) for use in this function
    access_logs = open(r"!Logs/AccessLogs.txt","r")
    access_logs.seek(0)
    access_log_list = (access_logs.read()).split(",")

    name = access_log_list[0]
    password = access_log_list[1]

    print("\n" + "-"*48 + "\n")
    def sub_options():
        print("Email option selected. Please input one of the numbers into the field below:\n\n"
                "1 = Get websites With Target Email \n"
                "2 = Update Email of a Website \n"
                "3 = Go to Usernames & Passwords \n"
                "4 = Go to Websites  \n"
                "0 = Exit To Main Menu \n")
    
    sub_options()
    option = int(input("Input here: "))

    while option != 0:
        if option == 1:
            sql_queries.get_email()
        elif option == 2:
            sql_queries.update_email()  
        elif option == 3:
            user()
        elif option == 4:
            websites()
        else:
            print("\nInvalid response, please try again.\n")

        print("\n")
        sub_options()
        option = int(input("Input here: "))

    access_logs.close()

    # end of function returns to main screen
    print("-"*48 + "\nWelcome back to the main screen:\n" + "-"*48)


if __name__ == '__main__':
    print("Calling sub_menu.py")