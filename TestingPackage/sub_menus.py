from unicodedata import name
from TestingPackage import sql_queries

print("="*48 + "\nsub_menu.py running\n" + "="*48)

def websites():
    name = "HamingnottT"

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
            pass
            
        elif option == 2:
            pass
            
        elif option == 3:
            print("\n")
            sql_queries.get_all_websites()
            print(f"\nReturned all websites from database under {name}. Returning to menu. . .")
        
        elif option == 4:
            pass
        
        elif option == 5:
            pass
            
        else:
            print("\nInvalid response, please try again.\n")

        print("\n")
        sub_options()
        option = int(input("Input here: "))

    # end of function returns to main screen
    print("-"*48 + "\nWelcome back to the main screen:\n" + "-"*48)



if __name__ == '__main__':
    print("Calling sub_menu.py")