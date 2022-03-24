# from . import sql_queries
import sql_queries
# from . import function_debug

print("="*48 + "\nmain_menu.py running\n" + "="*48)

# /!\ Need to find a way to connect query to the assigned variable sign_in_query
# returns type 'None' which is keeping me from passing the if statement
def sign_in():
    
    print("\nHello, This is my first programming project that will log your website sign-in data for easy recall."
    "\nWARNING: Authentication required before proceeding - please sign in.\n")

    # input_user_name = input("Username: ")
    # input_password = input("Password: ")

    input_user_name = "HamingnottT"
    input_password = "NotMyPassword"
    
    try:
        (name, password) = sql_queries.sign_in_query(input_user_name, input_password)
    except UnboundLocalError:
        print("Username or Password entered does not match any records.")
        return
    finally:
        pass
    
    if input_user_name == str(name) and input_password == str(password):
        print(f"\nWelcome in {name}!\n") # validation only - pending function call
    else:
        print(f"{str(name)} and {str(password)} are the outputs of the tuple")

