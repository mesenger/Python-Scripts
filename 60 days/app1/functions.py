FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Returns a list of todos from a file
     
    Args:
        filepath (str): The path to the file to read.
        
    Returns:
        list: A list of todos.
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes a list of todos to a file

    Args:
        todos_arg (list): A list of todos.
        filepath (str): The path to the file to write.
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
