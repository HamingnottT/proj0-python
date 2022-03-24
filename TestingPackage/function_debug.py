# from . import connection
import connection

print("="*48 + "\nfunction_debug.py running\n" + "="*48)

# ------------------------------------------------------------------------------

# def string_interpolation():
#     n1 = "String"
#     n2 = "Interpolation"

#     # f-string method - works well and very Scala-like
#     print(f"{n1} {n2} using the f-string method.")

# ------------------------------------------------------------------------------

cursor = connection.cursor

# query function defined
def sign_in_query(input_user_name, input_password):
    cursor.execute(f"SELECT cl_user, cl_pass FROM project0.sql_admin WHERE cl_user = '{input_user_name}' AND cl_pass = '{input_password}'")
    for x in cursor:
        print(x)
    cursor.close()

print("\nQuery output:\n")

# function called with variables assigned
sign_in_query("HamingnottT","NotMyPassword")
