import json

# Create an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task():
    task_name = input("Enter the task name: ")
    task_priority = int(input("Enter the task priority (1-5): "))
    task_due_date = input("Enter the due date (YYYY-MM-DD): ")
    
    task = {"name": task_name, "priority": task_priority, "due_date": task_due_date, "completed": False}
    todo_list.append(task)
    print("Task added successfully!")

# Function to mark a task as complete
def complete_task():
    task_name = input("Enter the task name to mark as complete: ")
    found = False
    
    for task in todo_list:
        if task['name'] == task_name:
            task['completed'] = True
            found = True
            print("Task marked as complete!")
            break
    
    if not found:
        print("Task not found.")

# Function to edit the priority of a task
def edit_priority():
    task_name = input("Enter the task name to edit priority: ")
    found = False
    
    for task in todo_list:
        if task['name'] == task_name:
            new_priority = int(input("Enter the new priority (1-5): "))
            task['priority'] = new_priority
            found = True
            print("Priority updated successfully!")
            break
    
    if not found:
        print("Task not found.")

# Function to edit the due date of a task
def edit_due_date():
    task_name = input("Enter the task name to edit due date: ")
    found = False
    
    for task in todo_list:
        if task['name'] == task_name:
            new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
            task['due_date'] = new_due_date
            found = True
            print("Due date updated successfully!")
            break
    
    if not found:
        print("Task not found.")

# Function to view the to-do list sorted by priority and due date
def view_todo_list():
    if len(todo_list) == 0:
        print("The to-do list is empty.")
    else:
        sorted_list = sorted(todo_list, key=lambda x: (x['priority'] or 99, x['due_date'] or "9999-12-31"))
        print("To-Do List:")
        for task in sorted_list:
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{status} Task: {task['name']}, Priority: {task['priority']}, Due Date: {task['due_date']}")

# Function to remove a task from the to-do list
def remove_task():
    task_name = input("Enter the task name to remove: ")
    found = False
    
    for task in todo_list:
        if task['name'] == task_name:
            todo_list.remove(task)
            found = True
            print("Task removed successfully!")
            break
    
    if not found:
        print("Task not found.")

# Function to save the to-do list to a file
def save_todo_list():
    file_name = input("Enter the file name to save the to-do list: ")
    
    try:
        with open(file_name, 'w') as file:
            json.dump(todo_list, file)
        print("To-do list saved successfully!")
    except IOError:
        print("An error occurred while saving the file.")

# Function to load the to-do list from a file
def load_todo_list():
    file_name = input("Enter the file name to load the to-do list: ")
    
    try:
        with open(file_name, 'r') as file:
            todo_list.clear()
            todo_list.extend(json.load(file))
        print("To-do list loaded successfully!")
    except IOError:
        print("An error occurred while loading the file.")

# Main program loop
while True:
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Edit Priority")
    print("4. Edit Due Date")
    print("5. View To-Do List")
    print("6. Remove Task")
    print("7. Save To-Do List")
    print("8. Load To-Do List")
    print("9. Quit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        complete_task()
    elif choice == "3":
        edit_priority()
    elif choice == "4":
        edit_due_date()
    elif choice == "5":
        view_todo_list()
    elif choice == "6":
        remove_task()
    elif choice == "7":
        save_todo_list()
    elif choice == "8":
        load_todo_list()
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")