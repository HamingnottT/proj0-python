# from . import connection
# from . import main_menu
from TestingPackage import connection

print("="*48 + "\nsql_queries.py running\n" + "="*48)

# "public" variable cursor
cursor = connection.cursor

TESTusername = "HamingnottT"

def sign_in_query(input_user_name, input_password):
    cursor.execute(f"SELECT cl_user, cl_pass FROM project0.sql_admin WHERE cl_user = '{input_user_name}' AND cl_pass = '{input_password}'")
    for x in cursor:
        name = x[0]
        password = x[1]
    return(name, password)

def debug_select_all():
    cursor.execute("SELECT * FROM project0.sql_admin")
    for x in cursor:
        print(x)

def get_all_websites():
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}'")
    for x in cursor:
        print(x)

# R
def get_Certain_Website():
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}' AND website = '{userInput4Website}'")
    for x in cursor:
        print(x)


# U
# /!\ this function has multiple queries and I need to find a way to handle both separately and on-demand
def update_website():
    # var updateWebUsername - 
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}' AND website = '{inputWebsite4User}'")
    for x in cursor:
        print(x)
    
    updateSite = ""

    # updates website name based on variable updateSite - most likely this variable will be moved to another file
    cursor.execute(f"UPDATE sql_user SET website = '{updateSite}' WHERE website = '{inputWebsite4User}''")
    for x in cursor:
        print(x)

    # var postUpdate
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}' AND website = '{updateSite}';")
    for x in cursor:
        print(x)

# D
def del_website():
    # try:
    
    # except:
    
    # finally:
    #     pass

    pass

# R
def get_all_user():
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}' AND username = '{input4User}'")
    for x in cursor:
        print(x)

# U
# /!\ this function has multiple queries and I need to find a way to handle both separately and on-demand
def update_user():

    #  var inputWebsite4User - What website are you looking for?
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}' AND website = '{inputWebsite4User}'")
    for x in cursor:
        print(x)
    
    # var webUpdateUser - What username are you using now?
    cursor.execute(f"UPDATE sql_user SET username = '{webUpdateUser}' WHERE website = '{inputWebsite4User}'")
    for x in cursor:
        print(x)
    
    # returns list with update
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}' AND username = '{webUpdateUser}'")
    for x in cursor:
        print(x)

# U
def update_pass():
    # var InputWebsite4Pass - What website are you looking for?
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}' AND website = '{inputWebsite4Pass}'")
    for x in cursor:
        print(x)

    # var webUpdatePassword - What password are you using now?
    cursor.execute(f"UPDATE sql_user SET password = '{webUpdatePassword}' WHERE website = '{inputWebsite4Pass}'")
    for x in cursor:
        print(x)
    
    # returns list with update
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}' AND password = '{webUpdatePassword}'")
    for x in cursor:
        print(x)
    
# R
def get_email():
    # var inputWebsite4email - What email address are you looking for?
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}' AND email = '{inputWebsite4email}'")
    for x in cursor:
        print(x)

# U
def update_email():
    # var inputWebsite4email - What email address are you looking for?
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}' AND website = '{inputWebsite4email}'")
    for x in cursor:
        print(x)
    
    # var webUpdateEmail = readLine("\nWhat password are you using now? ")
    cursor.execute(f"UPDATE sql_user SET email = '{webUpdateEmail}' WHERE website = '{inputWebsite4email}'")
    for x in cursor:
        print(x)

    # returns list with update
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{TESTusername}' AND email = '{webUpdateEmail}'")
    for x in cursor:
        print(x)

# print("="*48 + "\nsql_queries.py ended\n" + "="*48)