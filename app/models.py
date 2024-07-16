from random import randint as rint

class Task:
    def __init__(self, description, deadline=None, id=rint(0, 100), completed=False):
        self.description = description
        self.deadline = deadline
        self.id = id
        self.completed = completed

    def display(self): # This method is called when you print an object
        name = self.__class__.__name__
        description = self.description
        deadline = self.deadline
        return f"{name}({description} | {deadline} | {self.id} | {self.completed})"
    
class Menu:
    def __init__(self):
        self.options = {
            "1": "New task",
            "2": "View tasks",
            "3": "Edit task",
            "4": "Exit"
        }
        self.choice = None

    def start(self):


    def get_choice(self):
        self.choice = int(input("Enter your choice: "))
        return self.choice
    
    def display(self):
        print("Welcome to Dutify, a terminal based to do list application.\n\n Menu:")
        for opt in self.options:
            print(opt)
        for key, value in self.options.items():
            print(f"{key}: {value}")