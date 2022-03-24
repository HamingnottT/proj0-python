import mysql.connector
# import re # /?\ imports regex

print("="*48 + "\nmysql_connection.py running\n" + "="*48)

mysql_conn = ""

# mysql_conn = mysql.connector.connect(
#   host="localhost",
#   # url = "jdbc:project0://localhost:3306/mysql", # /!\ from Scala - jdbc may not work when called /!\
#   user="root",
#   password="RiffRaff68#$",
#   database="project0"
# )

# Try-Except in case of issues
try:
  mysql_conn = mysql.connector.connect(
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
mycursor = mysql_conn.cursor()

# DEBUG: shows the table to validate whether db loaded or not
# mycursor.execute("DESCRIBE sql_admin")
# for x in mycursor:
#   print(x)

# mycursor.execute("SELECT * FROM project0.sql_admin")

# print(mysql_conn)

print("="*48 + "\nmysql_connection.py ended\n" + "="*48)