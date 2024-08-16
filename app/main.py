from os import system as sys
from .models import Menu
from .database import Database

global task_list

call = Menu(True)
db = Database()

# Menu selection logic
while Menu(True):
    try:
        db.connect()
        db.create_table()
    except Exception as e:
        print(f"Error connecting to database services: {e}")
        break

    call.start_menu()
    if call.get_selection() == 1:
        db.add_task()
    elif call.get_selection() == 2:
        db.list_tasks()
    elif call.get_selection() == 3:
        call.pause_menu() # pause state
        if call.get_selection() == 1:
            pass # settings.exe()
        elif call.get_selection() == 2:
            pass # save.exe()
        elif call.get_selection() == 3:
            sys.exit()
        else:
            pass
    elif call.get_selection() == 4:
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