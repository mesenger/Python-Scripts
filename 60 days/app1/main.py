#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%c")
print(now)

while True:
    # Get user action
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action.replace("add", "", 1).strip() + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos_arg=todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip()
            print(f"{index + 1}. {todo}")

    elif user_action.startswith("edit"):
        try:
            number = user_action.replace("edit", "",1).strip()
            number = int(number) - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos_arg=todos)

        except ValueError:
            print("Your command was not understood. Please enter a number.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = user_action.replace("complete", "",1).strip()

            todos = functions.get_todos()
            
            number = int(number) - 1
            todos.pop(number)
            for index, todo in enumerate(todos):
                print(f"{index + 1}. {todo.strip()}")

            functions.write_todos(todos_arg=todos)

            message = f"Todo #{number + 1} has been completed."
            print(message)
        except IndexError:
            print("There is no todo with that number.")
            continue

    elif user_action.startswith("exit") or user_action.startswith("q"):
        break
    else:
        print("Invalid action")

print("Goodbye!")