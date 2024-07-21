from random import randint as rint

class Task:
    def __init__(self, name, deadline=None, task_id=rint(0, 100), completed=False, list={}):
        self.name = name
        self.deadline = deadline
        self.task_id = task_id
        self.completed = completed
        self.list = list

    def display(self, task, task_id=None): # This method is called when you print an object
        display_all = input("Would you like to display all tasks? (y/n): ")
        if display_all.lower() == "y":
            self.list[self.task_id] = {
                "description": self.description,
                "deadline": self.deadline,
                "completed": self.completed
            }

    
class Menu:
    def __init__(self, status, options={}, selection=None):
        self.status = status
        self.options = options
        self.selection = selection

    def start_menu(self):
        self.status = Menu(status=1)
        print("Welcome to Dutify, a terminal based to do list application.\n\n Menu:\n")
        self.display()
        self.get_selection()

    def pause_menu(self):
        self.status = Menu(status=2)
        print("Menu:\n")
        self.display()
        self.get_selection()

    def display(self):
        if Menu(status=1):
            self.options = {
                1: "Add a task",
                2: "View tasks",
                3: "Pause",
                4: "Exit"
            }
        elif Menu(status=2):
            self.options = {
                1: "Settings",
                2: "Save",
                3: "Exit"
            }
        for opt in self.options:
            print(opt)

    def get_selection(self):
        selection = int(input("\nSelect an option: "))
        self.selection = selection
        return selection