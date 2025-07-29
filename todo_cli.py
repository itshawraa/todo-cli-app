todo_list = []

while True:
    print("\nYour To-Do List:")
    for idx, task in enumerate(todo_list, 1):
        print(f"{idx}. {task}")

    print("\nOptions:\n1. Add Task\n2. Delete Task\n3. Display List\n4. Quit")

    user_choice = input("Choose an option (1-4): ")

    if user_choice == "1":
        new_task = input("Enter the task to add: ")
        todo_list.append(new_task)
        print("Task added.")

    elif user_choice == "2":
        if not todo_list:
            print("Your list is empty.")
            continue
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(todo_list):
                deleted = todo_list.pop(task_number - 1)
                print(f"Task '{deleted}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif user_choice == "3":
        if not todo_list:
            print("Your list is empty.")
        else:
            print("Current To-Do List:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")

    elif user_choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
