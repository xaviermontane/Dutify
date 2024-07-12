print("Welcome to Dutify, a terminal based to do list application.\n")
menu = [
    "1. New task", "2. View tasks", "3. Edit task", "4. Exit"
    ]

# Display menu options
for opt in menu(): 
    print(menu[opt])

menu = True
selection = int(input("What would you like to do?: "))  # Try to catch errors for invalid input

task_list = []

# Functions
def newTask(task): # idk…
    pass

# Menu selection logic
while menu is True:
    if selection == 1:
        task = input("New task: ")
        task_list.append(task)
    if selection == 2:
        for x in task_list():
            print(task_list[x])
    if selection == 3:
        selection = str(input("Which task would you like to edit?: "))
        control = print("The following are allowed:\n1. Rename  2. Description  3. Deadline  4.  Move  5. View info  \")
    if selection == 4:
        exit()
    else:
        print("Wrong value! Try again...")
        continue