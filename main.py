import json
from typing import List


class TodoIndexError(Exception):
    """Raised when an invalid index is provided for todo operations."""
    pass

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


def load_todos() -> List[TodoItem]:
    try:
        with open("todos.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("todos.json does not contain a list")
            return [TodoItem(item["task"], item["done"]) for item in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in todos.json: {e}")
    except (KeyError, TypeError) as e:
        raise ValueError(f"Invalid data format in todos.json: {e}")


def save_todos(todos: List[TodoItem]) -> None:
    data = [{"task": t.task, "done": t.is_done()} for t in todos]
    try:
        with open("todos.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving todos: {e}")


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


def delete_task(todos: List[TodoItem]) -> None:
    try:
        index = int(input("Enter task index to delete: "))
        if not 0 <= index < len(todos):
            raise TodoIndexError(f"Index {index} is out of range (0-{len(todos)-1})")
        removed = todos.pop(index)
        print(f"Deleted: {removed.task}")
    except ValueError:
        print("Please enter a valid number.")
    except TodoIndexError as e:
        print(e)


def mark_done(todos: List[TodoItem]) -> None:
    try:
        index = int(input("Enter task index to mark done: "))
        if not 0 <= index < len(todos):
            raise TodoIndexError(f"Index {index} is out of range (0-{len(todos)-1})")
        todos[index].mark_as_done()
        print("Marked as done!")
    except ValueError:
        print("Please enter a valid number.")
    except TodoIndexError as e:
        print(e)

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
