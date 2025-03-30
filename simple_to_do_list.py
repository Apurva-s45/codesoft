# Simple To-Do List Application
def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def main():
    tasks = []
    while True:
        print("\nMenu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                remove_task(tasks)
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a number!")

if __name__ == "__main__":
    main()
