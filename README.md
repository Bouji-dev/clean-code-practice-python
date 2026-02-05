# clean-code-practice-python
This repository is my hands-on practice of Clean Code principles taught by Robert C. Martin (Uncle Bob).
We start with a dirty, messy command-line TODO application and refactor it day by day to apply:
- Meaningful Names
- Small & Focused Functions
- Proper Comments
- Consistent Formatting
- Objects & Data Structures
- Robust Error Handling
- SOLID Principles

Great for junior/mid Python developers preparing for interviews or wanting to improve code quality.
Feel free to fork, star, or use as reference! 🚀 

# Clean Code TODO App

## Description
A simple command-line TODO list manager to practice Clean Code principles from Uncle Bob's book. Built in Python.


## Day 1: Meaningful Names

### Features
- Add tasks
- Show tasks
- Delete tasks
- Mark tasks as done
- Persistent storage in JSON file

### Progress
- Improved naming for better readability (replaced short/meaningless names like d, c, i with descriptive names like todos, command, index)

### Key Notes
- Meaningful names are the most important factor in making code self-explanatory
- Names should reveal intent — avoid single-letter variables unless in very local scopes
- Good naming reduces the need for comments and makes debugging easier


## Day 2: Functions

### Features
- Add tasks
- Show tasks with status
- Delete tasks
- Mark tasks as done
- Persistent storage in JSON file

### Progress
- Refactored main() into small, single-responsibility functions
- Applied Stepdown Rule (high-level functions first, details lower)
- Fixed bug in display_todos with safe key access (.get())

### Key Notes
- Functions should be small — ideally <20 lines, often 4–10 lines
- Each function should do one thing (Single Responsibility at function level)
- Follow the Stepdown Rule: read code from top to bottom like a newspaper
- Avoid functions with many parameters — prefer 0–1, max 2


## Day 3: Comments

### Features
- Add tasks
- Show tasks with status
- Delete tasks
- Mark tasks as done
- Persistent storage in JSON file

### Progress
- Reviewed all code and removed unnecessary/redundant comments
- Focused on self-documenting code through better naming and structure

### Key Notes
- Comments are a failure — they indicate code wasn't expressive enough
- Good code needs very few comments; prefer better names and structure
- Only keep comments for "why" (intent, business rule, non-obvious decision)
- Never write comments that repeat what the code does
- Avoid commented-out code and change logs in source — use git instead


## Day 4: Formatting

### Features
- Add tasks
- Show tasks with status
- Delete tasks
- Mark tasks as done
- Persistent storage in JSON file

### Progress
- Applied consistent vertical & horizontal spacing
- Improved prompt readability with multi-line string
- Added json indent=2 for readable output file
- Ensured consistent indentation and operator spacing

### Key Notes
- Formatting is about communication and first impression
- Vertical openness between concepts, density within related lines
- Use tools like black for automatic, opinionated formatting
- Consistency within a team is more important than which style is chosen
- Keep line length reasonable (80–120 characters)


## Day 5: Objects and Data Structures

### Features
- Add tasks
- Show tasks with status
- Delete tasks
- Mark tasks as done
- Persistent storage in JSON file

### Progress
- Introduced TodoItem class as proper Object (encapsulated data + behavior)
- Separated concerns: data persistence vs domain behavior
- Updated load/save/display/mark functions to work with TodoItem objects

### Key Notes
- Data Structures expose data and have little/no behavior
- Objects expose behavior and hide data (encapsulation)
- Avoid Anemic Domain Model (models with only getters/setters)
- Use simple data classes (dataclass/dict) for DTOs and transfer
- Put meaningful behavior inside classes when it belongs to the domain


## Day 6: Error Handling

### Features
- Add tasks
- Show tasks with status
- Delete tasks
- Mark tasks as done
- Persistent storage in JSON file

### Progress
- Added custom TodoIndexError for invalid indices
- Improved error handling in load/save with specific exceptions
- Fail-fast + better messages in delete/mark operations

### Key Notes
- Use exceptions only for truly exceptional cases — not for normal control flow
- Never return or pass None if you can avoid it
- Provide meaningful context in exception messages
- Prefer specific except clauses over bare except
- Fail fast: validate inputs as early as possible