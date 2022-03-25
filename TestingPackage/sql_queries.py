# from . import connection
# from . import main_menu
from TestingPackage import connection

print("="*48 + "\nsql_queries.py running\n" + "="*48)

# "public" variable cursor
cursor = connection.cursor
conn = connection.conn

# opens the access log created in main_menu.sign_in(), and recreates a list(not tuple) for use in this function

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
    access_logs = open(r"!Logs/AccessLogs.txt","r")
    access_logs.seek(0)
    access_log_list = (access_logs.read()).split(",")
    name = access_log_list[0]
    password = access_log_list[1]
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}'")
    for x in cursor:
        print(x)
    access_logs.close()

# R
def get_Certain_Website():
    access_logs = open(r"!Logs/AccessLogs.txt","r")
    access_logs.seek(0)
    access_log_list = (access_logs.read()).split(",")
    name = access_log_list[0]
    password = access_log_list[1]
    userInput4Website = str(input("\nWhat website are you looking for? "))
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}' AND website = '{userInput4Website}'")
    for x in cursor:
        print(x)
    access_logs.close()

# U
# /!\ this function has multiple queries and I need to find a way to handle both separately and on-demand
def update_website():
    access_logs = open(r"!Logs/AccessLogs.txt","r")
    access_logs.seek(0)
    access_log_list = (access_logs.read()).split(",")
    name = access_log_list[0]
    password = access_log_list[1]
    # var updateWebUsername - 
    inputWebsite4User = str(input("\nWhat website are you looking for? "))
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}' AND website = '{inputWebsite4User}'")
    for x in cursor:
        print(x)
    
    updateSite = str(input("\nUpdate site here: "))

    # updates website name based on variable updateSite - most likely this variable will be moved to another file
    cursor.execute(f"UPDATE sql_user SET website = '{updateSite}' WHERE website = '{inputWebsite4User}'")
    conn.commit()
    for x in cursor:
        print(x)

    # var postUpdate
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}' AND website = '{updateSite}'")
    for x in cursor:
        print(x)
    access_logs.close()

# D
def del_website():
    # access_logs = open(r"!Logs/AccessLogs.txt","r")
    # access_logs.seek(0)
    # access_log_list = (access_logs.read()).split(",")
    # name = access_log_list[0]
    # password = access_log_list[1]
    # try:
        
    
    # except:
    
    # finally:
    
    # access_logs.close()
    pass

# R
def get_all_user():
    access_logs = open(r"!Logs/AccessLogs.txt","r")
    access_logs.seek(0)
    access_log_list = (access_logs.read()).split(",")
    name = access_log_list[0]
    password = access_log_list[1]
    input4User = str(input("What username are you looking for? "))
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}' AND username = '{input4User}'")
    for x in cursor:
        print(x)
    access_logs.close()

# U
# /!\ this function has multiple queries and I need to find a way to handle both separately and on-demand
def update_user():
    access_logs = open(r"!Logs/AccessLogs.txt","r")
    access_logs.seek(0)
    access_log_list = (access_logs.read()).split(",")
    name = access_log_list[0]
    password = access_log_list[1]
    inputWebsite4User = str(input("What Website are you looking for? "))
    #  var inputWebsite4User - What website are you looking for?
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}' AND website = '{inputWebsite4User}'")
    for x in cursor:
        print(x)
    
    webUpdateUser = str(input("\nWhat username are you using now? "))
    # var webUpdateUser - What username are you using now?
    cursor.execute(f"UPDATE sql_user SET username = '{webUpdateUser}' WHERE website = '{inputWebsite4User}'")
    conn.commit()
    for x in cursor:
        print(x)
    
    # returns list with update
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}' AND username = '{webUpdateUser}'")
    for x in cursor:
        print(x)
    access_logs.close()

# U
def update_pass():
    access_logs = open(r"!Logs/AccessLogs.txt","r")
    access_logs.seek(0)
    access_log_list = (access_logs.read()).split(",")
    name = access_log_list[0]
    password = access_log_list[1]
    inputWebsite4Pass = str(input("What Website are you looking for? "))
    # var InputWebsite4Pass - What website are you looking for?
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}' AND website = '{inputWebsite4Pass}'")
    for x in cursor:
        print(x)

    webUpdatePassword = str(input("\nWhat password are you using now? "))
    # var webUpdatePassword - What password are you using now?
    cursor.execute(f"UPDATE sql_user SET password = '{webUpdatePassword}' WHERE website = '{inputWebsite4Pass}'")
    conn.commit()
    for x in cursor:
        print(x)
    
    # returns list with update
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}' AND password = '{webUpdatePassword}'")
    for x in cursor:
        print(x)
    access_logs.close()
    
# R
def get_email():
    access_logs = open(r"!Logs/AccessLogs.txt","r")
    access_logs.seek(0)
    access_log_list = (access_logs.read()).split(",")
    name = access_log_list[0]
    password = access_log_list[1]
    inputWebsite4email = str(input("What email address are you looking for? "))
    # var inputWebsite4email - What email address are you looking for?
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}' AND email = '{inputWebsite4email}'")
    for x in cursor:
        print(x)
    access_logs.close()

# U
def update_email():
    access_logs = open(r"!Logs/AccessLogs.txt","r")
    access_logs.seek(0)
    access_log_list = (access_logs.read()).split(",")
    name = access_log_list[0]
    password = access_log_list[1]
    inputWebsite4email = str(input("What email address are you looking for? "))
    # var inputWebsite4email - What email address are you looking for?
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}' AND website = '{inputWebsite4email}'")
    for x in cursor:
        print(x)
    
    webUpdateEmail = str(input("\nWhat password are you using now? "))
    # var webUpdateEmail = readLine("\nWhat password are you using now? ")
    cursor.execute(f"UPDATE sql_user SET email = '{webUpdateEmail}' WHERE website = '{inputWebsite4email}'")
    conn.commit()
    for x in cursor:
        print(x)

    # returns list with update
    cursor.execute(f"SELECT website, username, password, email FROM project0.sql_user WHERE cl_user = '{name}' AND email = '{webUpdateEmail}'")
    for x in cursor:
        print(x)
    access_logs.close()

# print("="*48 + "\nsql_queries.py ended\n" + "="*48)
