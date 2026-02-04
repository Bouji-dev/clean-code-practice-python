import json


class TodoItem:
    def __init__(self, task: str, done: bool = False):
        self._task = task.strip()
        self._done = done

    def mark_as_done(self):
        self._done = True

    def is_done(self) -> bool:
        return self._done

    @property
    def task(self) -> str:
        return self._task

    def __str__(self) -> str:
        status = "✅ Done" if self._done else "⏳ Pending"
        return f"{self._task} - {status}"


def load_todos() -> list[TodoItem]:
    try:
        with open("todos.json", "r") as file:
            data = json.load(file)
            return [TodoItem(item["task"], item["done"]) for item in data]
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return []


def save_todos(todos: list[TodoItem]):
    data = [{"task": t.task, "done": t.is_done()} for t in todos]
    with open("todos.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def display_todos(todos: list[TodoItem]):
    if not todos:
        print("No tasks yet!")
        return

    for index, todo in enumerate(todos):
        print(f"{index}: {todo}")


def add_task(todos: list[TodoItem]):
    task = input("Enter new task: ").strip()
    if task:
        todos.append(TodoItem(task))
        print("Task added!")
    else:
        print("Task cannot be empty.")


def delete_task(todos: list[TodoItem]):
    try:
        index = int(input("Enter task index to delete: "))
        removed = todos.pop(index)
        print(f"Deleted: {removed.task}")
    except (ValueError, IndexError):
        print("Invalid index!")


def mark_done(todos: list[TodoItem]):
    try:
        index = int(input("Enter task index to mark done: "))
        todos[index].mark_as_done()
        print("Marked as done!")
    except (ValueError, IndexError):
        print("Invalid index!")

def main():
    todos = load_todos()
    while True:
        prompt = (
            "\n1: Add    | 2: Show   | "
            "3: Delete | 4: Done   | "
            "5: Exit → "
        )
        command = input(prompt).strip()
        
        if command == "1":
            add_task(todos)
        elif command == "2":
            display_todos(todos)
        elif command == "3":
            delete_task(todos)
        elif command == "4":
            mark_done(todos)
        elif command == "5":
            save_todos(todos)
            print("Goodbye!")
            break
        else:
            print("Invalid command!")


if __name__ == "__main__":
    main()
