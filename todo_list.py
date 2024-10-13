# todo_list.py
# This script implements a simple command-line to-do list application in Python.
# Users can add tasks, view tasks, mark them as done, and delete tasks.

# Initialize an empty list to store the tasks
tasks = []

# Function to display the tasks
def display_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task['done'] else "✗"  # Show ✓ if done, ✗ if not done
            print(f"{index}. [{status}] {task['task']}")

# Function to add a task
def add_task(task):
    tasks.append({"task": task, "done": False})  # Add task as a dictionary with 'done' status as False
    print(f"Task added: {task}")

# Function to mark a task as done
def mark_task_done(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True  # Update the task's done status to True
        print(f"Task '{tasks[index]['task']}' marked as done.")
    else:
        print(f"No task found at index {index}.")

# Function to delete a task
def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)  # Remove the task from the list
        print(f"Task '{removed_task['task']}' deleted.")
    else:
        print(f"No task found at index {index}.")

# Main function to run the application
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            display_tasks()  # Show current tasks
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)  # Add a new task
        elif choice == '3':
            index = int(input("Enter the task number to mark as done: ")) - 1
            mark_task_done(index)  # Mark task as done
        elif choice == '4':
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(index)  # Delete the specified task
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break  # Exit the loop and end the application
        else:
            print("Invalid option. Please select a valid number (1-5).")

# Entry point of the script
if __name__ == "__main__":
    main()

'''
Summary of Features:
--------------------
1. **View Tasks**: Displays the current list of tasks with their completion status.
2. **Add Task**: Allows the user to add a new task to the to-do list.
3. **Mark Task as Done**: Lets the user mark a specified task as completed.
4. **Delete Task**: Provides functionality to remove a task from the list.
5. **Exit**: Ends the application.

Usage:
------
To run the application, execute the script in a Python environment. 
Follow the on-screen instructions to manage your to-do list.
'''
