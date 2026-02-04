import json


def load_todos():
    try:
        with open('todos.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]


def save_todos(todos):
    with open('todos.json', 'w') as file:
        json.dump(todos, file, indent=2)


def main():
    todos = load_todos()

    while True:
        command = input("\n1: Add | 2: Show | 3: Delete | 4: Done | 5: Exit → ").strip()
        
        if command == '1':
            
            pass
        
        save_todos(todos)