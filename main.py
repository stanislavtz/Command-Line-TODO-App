def display_todos(todos_list):
    for index, task in enumerate(todos_list):
        print(f"{index+1} - {task.strip()}")


def read_file_lines(file_path):
    with open(file_path, "r") as file_to_read:
        texts_list = file_to_read.readlines()
    return texts_list


def write_file_lines(file_path, todos_list):
    with open(file_path, "w") as file_to_write:
        file_to_write.writelines(todos_list)


def add_line(file_path, line):
    with open(file_path, "a") as file_to_append:
        file_to_append.write(line)


while True:
    user_input = input("Type add, show, edit, complete or exit: ")

    match user_input.lower():
        case "add":
            todo = input("Enter todo: ")
            todo = todo.capitalize() + "\n"
            add_line("files/todos.txt", todo)

        case "show" | "display":
            try:
                todos = read_file_lines("files/todos.txt")
                if len(todos) > 0:
                    display_todos(todos)
                else:
                    print("No tasks available!")
            except FileNotFoundError:
                print("File Not Found!")

        case "edit":
            try:
                todos = read_file_lines("files/todos.txt")
            except FileNotFoundError:
                print("File Not Found!")
            else:
                try:
                    num_index = int(input("Which todo number do you want to edit? "))
                    if 0 < num_index < len(todos) + 1:
                        new_todo = input(f"Edit todo {num_index} - {todos[num_index - 1].strip()} with new task: ")
                        num_index -= 1
                        todos[num_index] = new_todo.capitalize() + "\n"
                        write_file_lines("files/todos.txt", todos)
                    else:
                        print("Invalid number!")
                except ValueError:
                    print("Invalid input!")

        case "complete":
            try:
                todos = read_file_lines("files/todos.txt")
            except FileNotFoundError:
                print("File Not Found!")
            else:
                try:
                    num_index = int(input("Which number todo task is complete? "))
                    if 0 < num_index < len(todos) + 1:
                        num_index -= 1
                        todos.pop(num_index)
                        write_file_lines("files/todos.txt", todos)
                    else:
                        print("No such a task in todos list!")
                except ValueError:
                    print("Invalid input!")

        case "exit":
            break

        case _:
            print("Invalid input!")

print("Bye!")