FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """Write the todo items list in the text files."""
    with open(filepath,'w') as file:
        file.write(todos_arg)

if __name__  == "__main__":
    todos = get_todos()