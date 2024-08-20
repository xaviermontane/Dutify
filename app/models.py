from random import randint as rint

class Task:
    def __init__(self, name=str, tid=int, deadline=None, completed=False, list={}):
        self.name = name
        self.tid = tid
        self.deadline = deadline
        self.completed = completed

class Menu:
    def __init__(self, status=None, options=None):
        self.status = status
        self.options = options

    def start_menu(self, login=bool):
        self.status = 1
        self.login = login
        print("\nWelcome to Dutify, a terminal based to do list application.")
        choice = input("Would you like to login to an existing user account? (Y/N): ")
        if choice.upper() == "Y":
            self.login = True
        elif choice.upper() == "N":
            self.login = False
        else:
            while choice.upper() != "Y" and choice.upper() != "N":
                print("Invalid option! Please enter 'Y' or 'N'")
                choice = input("Would you like to login to an existing user account? (Y/N): ")
        self.display()
        return self.get_selection()

    def pause_menu(self):
        self.status = 2
        print("Menu:\n")
        self.display()
        self.get_selection()

    def display(self):
        if self.status == 1:
            self.options = {
                1: "Add a task",
                2: "View tasks",
                3: "Pause",
                4: "Exit"
            }
        elif self.status == 2:
            self.options = {
                1: "Settings",
                2: "Save",
                3: "Exit"
            }
        else:
            print("Invalid status")
    
    def get_selection(self, selection=int):
        try:
            selection = int(input("\nSelect an option: "))
            if selection < 1 or selection > 4:
                raise ValueError
            else:
                return selection
        except ValueError:
            print("Invalid option! Please select a valid option")
            self.get_selection()