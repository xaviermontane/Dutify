from random import randint as rint

class Task:
    def __init__(self, name, tid=int, deadline=None, completed=False, list={}):
        self.name = name
        self.tid = tid
        self.deadline = deadline
        self.completed = completed

class Menu:
    def __init__(self, status, options={}):
        self.status = status
        self.options = options

    def start_menu(self):
        self.status = 1
        print("Welcome to Dutify, a terminal based to do list application.\n\n Menu:\n")
        self.display()
        self.get_selection()

    def pause_menu(self):
        self.status = 2
        print("Menu:\n")
        self.display()
        self.get_selection()

    def display(self):
        if Menu(1):
            self.options = {
                1: "Add a task",
                2: "View tasks",
                3: "Pause",
                4: "Exit"
            }
        elif Menu(2):
            self.options = {
                1: "Settings",
                2: "Save",
                3: "Exit"
            }
        else:
            print("Invalid status")
    
    def get_selection(self, selection=int):
        selection = input("\nSelect an option: ")
        return selection