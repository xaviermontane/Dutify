from os import system as sys
from models import Task, Menu
from database import Database

db = Database()
task = Task()
call = Menu()

def login(user, pswd):
    with open("app/credentials.txt", "r") as f:
        for line in f:
            usr, pwd = line.split(", ")
            if user.strip() == usr.strip() and pwd.strip() == pswd.strip(): 
                print(f"Login successful! Welcome, {user}.")
                return
        if user == "guest" and pswd == "guest":
            print(f"Login successful! Welcome, {user}.")
        else:
            print("Invalid credentials. Please try again.")

# Search bar equivalent
# def database_search():
#     pass

try:
    db.connect()
    db.create_table()
except Exception as e:
    print(f"Error connecting to database services: {e}")
    sys.exit()

# Login logic
call.start_menu(True)

if call.login == True:
    user = input("Enter your username: ")
    pswd = input("Enter your password: ")
    login(user, pswd)
elif call.login == False:
    new_account = input("Do you want to login to a new account? (Y/N): ")
    if new_account.upper() == "Y":
        user = input("New username: ")
        pswd = input("New password: ")
        with open("app/credentials.txt", "a") as f:
            f.write(f"{user}, {pswd}\n")
            login(user, pswd)
            print("User account created successfully!")
    elif new_account.upper() == "N":
        login("guest", "guest")
        print("No user account was created. You are logged in as a guest.")
else:
    login("guest", "guest")
    print("You are logged in as a guest.")

# Menu selection logic
while call.status > 0:
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