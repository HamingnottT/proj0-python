# This python file is used for testing SQL queries
# def main():

import mysql.connector
  # import re # /?\ imports regex

print("="*48 + "\nsql_conn_test.py running\n" + "="*48)

conn = ""

# mysql_conn = mysql.connector.connect(
#   host="localhost",
#   # url = "jdbc:project0://localhost:3306/mysql", # /!\ from Scala - jdbc may not work when called /!\
#   user="root",
#   password="RiffRaff68#$",
#   database="project0"
# )

# Try-Except in case of issues
try:
  conn = mysql.connector.connect(
    host="localhost",
    # url = "jdbc:project0://localhost:3306/mysql", # /!\ from Scala - jdbc may not work when called /!\
    user="root",
    password="RiffRaff68#$",
    database="project0"
  )
except AttributeError:
  print(AttributeError)
except ConnectionError:
  print(ConnectionError)
finally:
  pass

# creates a cursor to iterate thru table
cursor = conn.cursor()

# Query test here:
# print("\n")

# print("="*48 + "\nsql_conn_test.py ended\n" + "="*48)

# pass

# if __name__ == "__main__":

# # DEBUG: shows the table to validate whether db loaded or not
#   main()