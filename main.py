def display_todos(todos_list):
    for ind, task in enumerate(todos_list):
        task_num = ind + 1
        print(f"{task_num} - {task.strip()}")


def read_file_lines(file_path):
    try:
        with open(file_path, "r") as file_to_read:
            texts_list = file_to_read.readlines()
        return texts_list
    except FileNotFoundError:
        print("File Not Found!")
        return []


def write_file_lines(file_path, todos_list):
    with open(file_path, "w") as file_to_write:
        file_to_write.writelines(todos_list)


def add_line(file_path, line):
    with open(file_path, "a") as file_to_append:
        file_to_append.write(line)


def print_no_tasks():
    print("No tasks available!")


FILE_PATH = "files/todos.txt"

while True:
    user_input = input("Type add, show, edit, complete or exit: ")

    match user_input.lower():
        case "add":
            todo = input("Enter todo: ")
            formatted_todo = todo.capitalize() + "\n"
            add_line(FILE_PATH, formatted_todo)

        case "show" | "display":
            todos = read_file_lines(FILE_PATH)
            formatted_todos = [todo.strip("\n") for todo in todos]
            if todos:
                display_todos(formatted_todos)
            else:
                print_no_tasks()

        case "edit":
            todos = read_file_lines(FILE_PATH)

            if todos:
                try:
                    task_number = int(input("Which todo number do you want to edit? "))
                    if 0 < task_number < len(todos) + 1:
                        index = task_number - 1
                        current_task = todos[index].strip("\n")
                        new_todo = input(f"Edit todo {task_number} - {current_task}: with new task: ")
                        todos[index] = new_todo.capitalize() + "\n"
                        write_file_lines(FILE_PATH, todos)
                    else:
                        print("Invalid number!")
                except ValueError:
                    print("Invalid input!")
            else:
                print_no_tasks()

        case "complete":
            todos = read_file_lines(FILE_PATH)

            if todos:
                try:
                    task_number = int(input("Which number todo task is complete? "))
                    if 0 < task_number < len(todos) + 1:
                        index = task_number - 1
                        todos.pop(index)
                        write_file_lines(FILE_PATH, todos)
                    else:
                        print("No such a task in todos list!")
                except ValueError:
                    print("Invalid input!")
            else:
                print_no_tasks()

        case "exit":
            break

        case _:
            print("Invalid input!")

print("Bye!")