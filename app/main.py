from utils import *
from models import Task

start_menu()
menu = True
selection = int(input("\nWhat would you like to do?: "))  # Try to catch errors for invalid input
task_list = []


# Menu selection logic
while menu:
    if selection == 1:
        name = input("Task name/desc: ")
        deadline = float(input("Deadline: "))
        task_id = int(input("ID: "))
        newTask = Task(name, deadline, task_id)
        task_list.append(newTask)
    if selection == 2:
        for i in task_list():
            print(task_list[i])
    if selection == 3:
        pass
    if selection == 4:
        exit()
    else:
        selection = int(input("\nInvalid input! Please select a valid option: "))
        