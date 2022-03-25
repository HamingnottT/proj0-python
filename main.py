# Main entry point into application

print("="*48 + "\nmain.py running\n" + "="*48)

if __name__ == "__main__":
    print("="*48 + "\nmain_test.py running\n" + "="*48)
    from LoggerPackage import main_menu
    main_menu.sign_in()