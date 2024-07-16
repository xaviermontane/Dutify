from models import *

Menu.start(self)


global menu
menu = True
selection = int(input("\nWhat would you like to do?: "))  # Try to catch errors for invalid input
task_list = []


# Menu selection logic
while menu:
    if selection == 1:
        task = Task(input("Enter task description: "), input("Enter task deadline: "))
        task_list.append(task)
        print("Task added!")
    elif selection == 2:
        for task in task_list:
            print(task)
    elif selection == 3:
        task_id = int(input("Enter task ID to remove: "))
        for task in task_list:
            if task.id == task_id:
                task_list.remove(task)
                print("Task removed!")
                break
        else:
            print("Task not found!")
    elif selection == 4:
        print("Goodbye!")
        menu = False
    else:
        print("Invalid selection!")
    selection = int(input("\nWhat would you like to do?: "))