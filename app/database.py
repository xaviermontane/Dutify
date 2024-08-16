import sqlite3
from app.models import Task

# task = Task(None)   # Task object call

class Database:
    def connect(self):
        self.con = sqlite3.connect("dutify.db")

    def create_table(self):
        self.con.execute("CREATE TABLE IF NOT EXISTS tasks (tid INTEGER PRIMARY KEY, name TEXT, deadline DATE, complete BOOLEAN)")

    def add_task(self, task):
        cur = self.con.cursor()
        cur.execute("INSERT INTO tasks(tid, name, deadline, complete) VALUES (?,?,?,?)", (task.name, task.tid, task.deadline, task.complete))
        task.id = cur.lastrowid
        self.con.commit()

    def list_tasks(self):
        cur = self.con.cursor()
        cur.execute("SELECT tid, description FROM tasks")
        rows = cur.fetchall()
        tasks = [Task(name=row[1]) for row in rows]
        for i, task in enumerate(tasks):
            task.tid = rows[i][0]
        return tasks

    def remove_task(self, tid):
        cur = self.con.cursor()
        cur.execute("DELETE FROM tasks WHERE tid = ?", (tid))
        self.con.commit()

    def close(self):
        self.con.close()