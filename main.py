import json

def main():
    try:
        with open('todos.json', 'r') as file:
            todos = json.load(file)
    except FileNotFoundError:
        todos = []
    while True:
        command = input("1: add, 2: show, 3: delete, 4: mark done, 5: exit ")
        if command == '1':
            task = input("Enter task: ")
            todos.append({"task": task, "done": False})
        elif command == '2':
            for index, item in enumerate(todos):
                status = 'done' if item['done'] else 'pending'
                print(f"{index}: {item['task']} - {status}")
        elif command == '3':
            index = int(input("Enter index to delete: "))
            del todos[index]
        elif command == '4':
            index = int(input("Enter index to mark done: "))
            todos[index]['done'] = True
        elif command == '5':
            with open('todos.json', 'w') as file:
                json.dump(todos, file)
            break

main()