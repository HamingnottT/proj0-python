# import logging
# # from TestingPackage import *
# # from TestingPackage import connection    # imports connection.py from folder TestingPackage
# from TestingPackage import *
# # from TestingPackage import sql_queries

# print("="*48 + "\nmain_test.py running\n" + "="*48)

# main_menu

# print("="*48 + "\nmain_test.py ended\n" + "="*48)

if __name__ == "__main__":

    print("="*48 + "\nmain_test.py running\n" + "="*48)
    
    from TestingPackage import main_menu

    main_menu.sign_in()