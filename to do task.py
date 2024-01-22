import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task.completed else "Pending"
            print(f"{i}. {task.description} (Due: {task.due_date}) - {status}")

    # Add methods for marking tasks as completed and deleting tasks

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description},{task.due_date},{task.completed}\n")

    def load_from_file(self, filename):
        self.tasks = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    description, due_date, completed = line.strip().split(',')
                    task = Task(description, due_date)
                    task.completed = bool(completed)
                    self.tasks.append(task)
        except FileNotFoundError:
            print("No previous data found. Starting with an empty to-do list.")

# Example usage:
todo_list = ToDoList()

# Add tasks
todo_list.add_task("Finish project", "2023-01-15")
todo_list.add_task("Prepare for presentation", "2023-01-20")

# View tasks
todo_list.view_tasks()

# Save to file
todo_list.save_to_file("todo.txt")

# Load from file
todo_list.load_from_file("todo.txt")

# View tasks again
todo_list.view_tasks()
