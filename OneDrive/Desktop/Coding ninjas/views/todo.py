class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

# Create an instance of the ToDoList
todo_list = ToDoList()

while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. Display tasks")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.add_task(task)
        print("Task added successfully.")

    elif choice == "2":
        task = input("Enter the task to remove: ")
        if task in todo_list.tasks:
            todo_list.remove_task(task)
            print("Task removed successfully.")
        else:
            print("Task not found.")

    elif choice == "3":
        todo_list.display_tasks()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")