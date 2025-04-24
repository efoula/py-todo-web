def parse(user_input):
    """Extract the values split by a comma in a string
    and return the two values via a dictionary.
    """
    # Get the two values in a list
    parts = user_input.split(",")
    
    # Store the two values in variables 
    lower_bound = float(parts[0])
    upper_bound = float(parts[1])
    
    # Inject the values in a dictionary
    return {"lower_bound": lower_bound, "upper_bound": upper_bound}

def count(phrase):
    return phrase.count('.')

def time():
    from datetime import datetime
    return datetime.now()

def get_todos():
    with open('database/todo.txt', 'r') as file:
        todos = file.readlines()
        return todos

def add_todo(todo):
        todos = get_todos()
        todos.append(todo + '\n')
        with open('database/todo.txt', 'w') as file:
            file.writelines(todos)
            file.close()

def remove_todo(todo):
        index = int(todo) - 1
        todos = get_todos()
        todos.pop(index)
        with open('database/todo.txt', 'w') as file:
            file.writelines(todos)
            file.close()

def update_todo(todo, new_todo):
        index = int(todo) - 1
        todos = get_todos()
        todos[index] = new_todo + '\n'
        with open('database/todo.txt', 'w') as file:
            file.writelines(todos)
            file.close()

def update_todo_index(todo, new_todo):
        index = get_todos().index(todo)
        todos = get_todos()
        todos[index] = new_todo + '\n'
        with open('database/todo.txt', 'w') as file:
            file.writelines(todos)
            file.close()

def write_todos(todos):
    with open('database/todo.txt', 'w') as file:
        file.writelines(todos)
        file.close()   

def complete_todo(todo):
    todos = get_todos()
    todos.remove(todo)
    write_todos(todos)   

def count_todo():
    todos = get_todos()
    count = len(todos)
    return count

# def time():
#     return datetime.now().strftime("%H:%M:%S")