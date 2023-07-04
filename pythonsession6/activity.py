class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def get_description(self):
        return self.description

    def is_completed(self):
        return self.completed

    def mark_as_completed(self):
        self.completed = True


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("To-do list is empty")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task.is_completed() else "Pending"
                print(f"{index}. {task.get_description()} - {status}")

    def task_complete(self, task_index):
        task = self.tasks[task_index]
        task.mark_as_completed()


task1 = Task("Buy groceries")
task2 = Task("Do laundry")
todoList = TodoList()
todoList.add_task(task1)
todoList.add_task(task2)
todoList.display_tasks()
todoList.task_complete(1)
todoList.display_tasks()


























