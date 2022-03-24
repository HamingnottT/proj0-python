# from . import sql_queries
from typing import Tuple
import sql_queries
# from . import function_debug

print("="*48 + "\nmain_menu.py running\n" + "="*48)

# /!\ Need to find a way to connect query to the assigned variable sign_in_query
# returns type 'None' which is keeping me from passing the if statement
def sign_in():
    print("\nHello, This is my first programming project that will log your website sign-in data for easy recall."
    "\nWARNING: Authentication required before proceeding - please sign in.\n")

    input_user_name = input("Username: ")
    input_password = input("Password: ")
    
    sign_in_res = sql_queries.sign_in_query(input_user_name, input_password)

    # debug print out to show type
    print(sign_in_res)

    # /!\ returns TypeError: 'NoneType' object is not subscriptable
    # because the output of the query thru the cursor is a Tuple
    # I created an if conditional to try to match user input to the respective index
    if input_user_name == sign_in_res [0] & input_password == sign_in_res[1]:
        print("Success!")
    else:
        print(f"{sign_in_res[0]} and {sign_in_res[1]} are the outputs of the tuple")

sign_in()