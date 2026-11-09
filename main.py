from modules import functions
import time

FILE_PATH = "files/todos.txt"

now = time.strftime("%d/%b/%Y %H:%M:%S")
print(f"It is {now}")


while True:
    user_input = input("Type add, show, edit, complete or exit: ").strip().lower()

    match user_input:
        case "add":
            todo = input("Enter todo: ")
            formatted_todo = todo.capitalize() + "\n"
            functions.add_todo(FILE_PATH, formatted_todo)

        case "show" | "display":
            todos = functions.get_todos(FILE_PATH)
            formatted_todos = [todo.strip("\n") for todo in todos]
            if todos:
                functions.display_todos(formatted_todos)
            else:
                functions.print_no_todos()

        case "edit":
            todos = functions.get_todos(FILE_PATH)

            if todos:
                while True:
                    try:
                        todo_number = int(input("Which todo number do you want to edit? "))
                        index = todo_number - 1
                        current_todo = todos[index].strip("\n")

                        new_todo = input(f"Edit todo {todo_number} - {current_todo} with new todo: ")
                        if new_todo.lower() == "cancel":
                            break

                        todos[index] = new_todo.capitalize() + "\n"

                        functions.save_todos(FILE_PATH, todos)

                        print(f"Todo {current_todo} updated with {new_todo} todo! ")
                        break
                    except ValueError:
                        print("Invalid input!")
                    except IndexError:
                        print("Invalid number!")

            else:
                functions.print_no_todos()

        case "complete":
            todos = functions.get_todos(FILE_PATH)

            if todos:
                while True:
                    try:
                        todo_number = int(input("Which todo number is completed? "))
                        index = todo_number - 1
                        todo_to_complete = todos.pop(index).strip("\n")

                        functions.save_todos(FILE_PATH, todos)

                        print(f"Todo {todo_number} - {todo_to_complete} is completed! ")
                        break
                    except ValueError:
                        print("Invalid input!")
                    except IndexError:
                        print("No such a todo in todos list!")
            else:
                functions.print_no_todos()

        case "exit":
            break

        case _:
            print("Invalid input!")

print("Bye!")
