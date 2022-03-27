# This module establishes the MySQL connection to the database

import mysql.connector

# print("="*48 + "\nconnection.py running\n" + "="*48)
print("="*48 + "MySQL attempting to connect" + "="*48)

conn = ""

# input for MySQL connection
host = str(input("Please enter your host name('localhost' if local): "))
user = str(input("Please enter your user name('root' if local): "))
password = str(input("Please enter your password: "))

# Try-Except in case of issues
try:
  conn = mysql.connector.connect(
    host=f"{host}",
    user=f"{user}",
    password=f"{password}",
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