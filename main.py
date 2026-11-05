def display_todos(todos_list):
    for index, task in enumerate(todos_list):
        index += 1
        print(f"{index} - {task.strip()}")


while True:
    user_input = input("Type add, show, edit, complete or exit: ")

    match user_input.lower():
        case "add":
            with open("files/todos.txt", "a") as file:
                todo = input("Enter todo: ")
                file.write(todo.capitalize() + "\n")

        case "show" | "display":
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            display_todos(todos)

        case "edit":
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            try:
                num = int(input("Which todo number do you want to edit? "))
                if 0 < num < len(todos) + 1:
                    new_todo = input(f"Edit todo {num} - {todos[num-1].strip()} with new task: ")
                    num -= 1
                    todos[num] = new_todo.capitalize() + "\n"
                    with open("files/todos.txt", "w") as file:
                        file.writelines(todos)
                else:
                    print("Invalid number!")
            except ValueError:
                print("Invalid input!")

        case "complete":
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            try:
                num = int(input("Which number todo task is complete? "))
                if 0 < num < len(todos) + 1:
                    num -= 1
                    todos.pop(num)

                    with open("files/todos.txt", "w") as file:
                        file.writelines(todos)
                else:
                    print("No such a task in todos list!")
            except ValueError:
                print("Invalid input!")

        case "exit":
            break

        case _:
            print("Invalid input!")

print("Bye!")