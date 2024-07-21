from os import system as sys
from .models import Task, Menu

global task_list

# Menu selection logic
while Menu(True):
    call = Menu(...) # Placeholder for menu object
    if Menu(1, ..., 1):
        call.start_menu()
        name = input("Task name: ")
        deadline = float(input("Deadline (MM.DD.YY): "))
        task_id = int(input("ID (default is randint): "))
        task_list.append(Task.display(name, deadline, task_id))
    elif Menu(1, ..., 2):
        Task.display()
    elif Menu(1, ..., 3):
        Menu(status=2)
        continue
    elif Menu(1, ..., 4):
            exit()

    if Menu(status=2):
        call.pause_menu()
        if Menu(..., ..., 1):
            #settings.exe()
            pass
        if Menu(..., ..., 2):
            #save.exe()
            pass
        if Menu(..., ..., 3):
            sys.exit()
        else:
            selection = int(input("\nInvalid input! Please select a valid option: ")

# Display tasks
def display_tasks():
    display_all = input("Would you like to display all tasks? (y/n): ")
    if display_all.lower() == "y":
        display_all = True
    elif display_all.lower() == "n":
        display_all = False
        id_query = input("Enter the task ID to be found: ")
        for x in task_list:
            if x.task_id == id_query:
                print(Task.display(x))
            else:
                print("Task not found!")
    else:
        print("Invalid input! Please enter 'y' or 'n'")
        display_tasks()

# Display func might be redundant 