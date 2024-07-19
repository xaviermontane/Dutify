from os import system as sys
from .models import Task, Menu

task_list = []

# Menu selection logic
while Menu(True):
    call = Menu(...) # Placeholder for menu object
    if Menu(1, ..., 1):
        call.start_menu()
        name = input("Task name: ")
        deadline = float(input("Deadline: "))
        task_id = int(input("ID: "))
        task_list.append(Task(name, deadline, task_id))
    elif Menu(1, ..., 2):
        Task.display(...)
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
            selection = int(input("\nInvalid input! Please select a valid option: "))

# Display tasks
def display_tasks():
    for task in task_list:
        print(task.display())