import sqlite3 as sql

class Database:
    def connect(self):
        self.con = sql.connect("tasks.db")
        self.cur = self.con.cursor()
        self.table()

    def table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS tasks(id INT, description STR, deadline FLOAT, status BOOL)")
        res = self.cur.execute("SELECT id FROM sqlite_master")
        print(f"Table created: {res.fetchone()}")

    def add_task(self, task):
        self.cur.execute("""
                    INSERT INTO tasks VALUES
                        (?, ?, ?, ?)
        """, (task.id, task.description, task.deadline, task.status)) # This will insert the task into the table
        res = self.con.commit()
        # print(f"Task added: {res.fetchone()}")

    def edit_task(self, task):
        self.cur.execute("""
                    UPDATE tasks
                    SET description = ?, deadline = ?, status = ?
                    WHERE id = ?
        
        """, (task.description, task.deadline, task.status, task.id))
        res = self.con.commit()
        # print(f"Task updated: {res.fetchone()}")

    def remove_task(self, task_id):
        self.cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        res = self.con.commit()
        # print(f"Task removed: {res.fetchone()}")
    
    """
    def list_tasks(self):
        self.cur.execute("SELECT * FROM tasks")
        rows = self.cur.fetchall()
        tasks = [Task(id=row[0], description=row[1], deadline=row[2], completed=row[3]) for row in rows]
        return tasks
    """

    def close(self):
        self.con.close()
        print("Connection closed, see you space cowboy...")