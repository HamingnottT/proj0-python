# Main entry point into application

print("="*48 + "\nmain.py running\n" + "="*48)

if __name__ == "__main__":

    print("="*48 + "\nmain_test.py running\n" + "="*48)
    
    access_logs = open(r"!Logs/AccessLogs.txt","w+")
    
    from LoggerPackage import main_menu

    main_menu.sign_in()

    access_logs.close()