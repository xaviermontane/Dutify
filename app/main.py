from os import system as sys
from models import Task, Menu
from database import Database

db = Database()
task = Task()
call = Menu()

def login(user, pswd):
    f = open("app/credentials.txt", "r")
    if user == "guest" and pswd == "guest":
        print(f"Login successful! Welcome, {user}.")
    elif user == f.readline() and pswd == f.readline():
        print(f"Login successful! Welcome, {user}.")
    else:
        print("Invalid credentials. Please try again.")
    f.close()

# Menu selection logic
while True:
    try:
        db.connect()
        db.create_table()
    except Exception as e:
        print(f"Error connecting to database services: {e}")
        break

    if call.start_menu() == True:
        user = input("Enter your username: ")
        pswd = input("Enter your password: ")
        login(user, pswd)
    else:
        print("Invalid status")
        break

    selection = call.get_selection()
    if selection == 1:
        db.add_task(task)
    elif selection == 2:
        db.list_tasks()
    elif selection == 3:
        call.pause_menu() # pause state
        if selection == 1:
            pass # settings.exe()
        elif selection == 2:
            pass # save.exe()
        elif selection == 3:
            sys.exit()
        else:
            pass
    elif selection == 4:
        prompt = input("Are you sure you want to exit? (Y/N): ")
        if prompt.upper() == "Y":
            sys.exit()
        elif prompt.upper() == "N":
            continue
        else:
            print("Invalid input! Please enter 'Y' or 'N'")
            continue
    else:
        print("Invalid input! Please select a valid option.")
        continue

# Search bar equivalent
def database_search():
    pass