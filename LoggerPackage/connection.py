# This module establishes the MySQL connection to the database

import mysql.connector
  # import re # /?\ imports regex

print("="*48 + "\nsql_conn_test.py running\n" + "="*48)

conn = ""

# Try-Except in case of issues
try:
  conn = mysql.connector.connect(
    host="localhost",
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
print("\n")

print("="*48 + "\nsql_conn_test.py ended\n" + "="*48)