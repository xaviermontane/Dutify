from random import randint as rint

class Task:
    def __init__(self, description, deadline=None, id=rint(0, 100), completed=False):
        self.description = description
        self.deadline = deadline
        self.id = int(id)
        self.completed = completed

    def __str__(self): # This method is called when you print an object
        name = self.__class__.__name__
        description = self.description
        deadline = float(self.deadline)
        return f"{name}({description} | {deadline} | {self.id} | {self.completed})"