import json
from typing import List


class TodoIndexError(Exception):
    """Raised when an invalid index is provided for todo operations."""
    pass

class TodoItem:
    def __init__(self, task: str, done: bool = False):
        self._task = task.strip()
        self._done = done

    def mark_as_done(self) -> None:
        self._done = True

    def is_done(self) -> bool:
        return self._done

    @property
    def task(self) -> str:
        return self._task

    def __str__(self) -> str:
        status = "✅ Done" if self._done else "⏳ Pending"
        return f"{self._task} - {status}"


class TodoRepository:
    FILE_PATH = "todos.json"

    @classmethod
    def load(cls) -> List[TodoItem]:
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError("Invalid data format")
                return [TodoItem(item["task"], item["done"]) for item in data]
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"Could not load todos: {e}. Starting empty.")
            return []

    @classmethod
    def save(cls, todos: List[TodoItem]) -> None:
        data = [{"task": t.task, "done": t.is_done()} for t in todos]
        try:
            with open(cls.FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Failed to save todos: {e}")


def display_todos(todos: list[TodoItem]) -> None:
    if not todos:
        print("No tasks yet!")
        return
    for index, todo in enumerate(todos):
        print(f"{index}: {todo}")


def add_task(todos: list[TodoItem]) -> None:
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

def run():
    todos = TodoRepository.load()

    commands = {
        "1": add_task,
        "2": display_todos,
        "3": delete_task,
        "4": mark_done,
        "5": lambda t: "exit",
    }

    while True:
        print("\n1: Add    | 2: Show   | "
            "3: Delete | 4: Done   | "
            "5: Exit → ")
        choice = input('Choise:').strip()

        if choice == "5":
            TodoRepository.save(todos)
            print("Goodbye!")
            break

        action = commands.get(choice)
        if action:
            action(todos)
        else:
            print("Invalid command!")


if __name__ == "__main__":
    run()
