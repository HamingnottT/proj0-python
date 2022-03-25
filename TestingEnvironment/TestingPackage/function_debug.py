# from . import connection
# import connection

print("="*48 + "\nfunction_debug.py running\n" + "="*48)

# ------------------------------------------------------------------------------

# def string_interpolation():
#     n1 = "String"
#     n2 = "Interpolation"

#     # f-string method - works well and very Scala-like
#     print(f"{n1} {n2} using the f-string method.")

# ------------------------------------------------------------------------------

# cursor = connection.cursor

# # query function defined
# def sign_in_query(input_user_name, input_password):
#     cursor.execute(f"SELECT cl_user, cl_pass FROM project0.sql_admin WHERE cl_user = '{input_user_name}' AND cl_pass = '{input_password}'")
#     for x in cursor:
#         print(x)
#     cursor.close()

# print("\nQuery output:\n")

# # function called with variables assigned
# sign_in_query("HamingnottT","NotMyPassword")

# ------------------------------------------------------------------------------

# /!\ handles the limitation of variables not carrying over to other functions and modules
# an temporary access log is created recording the current user of the session
# the log is read and split at delimiter to create a list
# the indexes of the list are the user and password akin to the sign-in function
# after closing the program the log list will be deleted to prevent clutter

import os
# import shutil

name = "HamingnottT"
password = "NotMyPassword"

access_log_formatter = f"{name},{password}"

access_logs = open(r"!Logs/AccessLogs.txt","w+")

access_logs.writelines(access_log_formatter)

access_logs.seek(0)

print(access_logs.read())

access_logs.seek(0)

access_log_list = (access_logs.read()).split(",")

print(access_log_list[0])

access_logs.close()

os.remove("!Logs/AccessLogs.txt")


