import json

def load_todos():
    try:
        with open('todos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open('todos.json', 'w') as file:
        json.dump(todos, file)

def display_todos(todos):
    if not todos:
        print('No tasks yet!')
        return
    for index, item in enumerate(todos):
        status = 'Done' if item['done'] else 'Pending'
        print(f'{index}: {item['task']} - {status}')

def add_task(todos):
    task = input('Enter new task: ').strip()
    if task:
        todos.append({'task': task, 'done': False})
        print('Task added!')
    else:
        print('Task cannot be empty.')

def delete_task(todos):
    try:
        index = int(input("Enter task index to delete: "))
        removed = todos.pop(index)
        print(f"Deleted: {removed['task']}")
    except (ValueError, IndexError):
        print("Invalid index!")

def mark_done(todos):
    try:
        index = int(input("Enter task index to mark done: "))
        todos[index]['done'] = True
        print("Marked as done!")
    except (ValueError, IndexError):
        print("Invalid index!")

def main():
    todos = load_todos()
    while True:
        command = input("\n1: Add | 2: Show | 3: Delete | 4: Done | 5: Exit → ").strip()
        if command == '1':
            add_task(todos)
        elif command == '2':
            display_todos(todos)
        elif command == '3':
            delete_task(todos)
        elif command == '4':
            mark_done(todos)
        elif command == '5':
            save_todos(todos)
            print("Goodbye!")
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()        
