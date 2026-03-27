# Reflection – Mini Project 2

## Overview

This project is a Football Player Database System developed in Python. The aim of the project was to demonstrate my understanding of key concepts from lectures and workshops 7–11, including Object-Oriented Programming (OOP), Regular Expressions, File I/O, Testing, and the use of libraries.

Throughout development, I transformed an initial basic program that used multiple lists into a more advanced, structured application using classes, validation, and persistent data storage.

---

## Development Process

I began with a simple procedural program that stored player data in separate lists (names, positions, nationalities, values). While this worked, it was inefficient and difficult to manage.

I then refactored the code into an Object-Oriented design:
- Created a `Person` base class
- Extended it with a `Player` class
- Built a `FootballSystem` class to manage application logic

This significantly improved code readability, scalability, and maintainability.

I also added a menu-driven CLI system to allow user interaction with features such as adding players, searching, filtering, and creating a starting lineup.

---

## Regular Expressions

I used Regular Expressions in a `Utils` class to validate user input:
- Player names (letters and spaces only)
- Positions (restricted to valid football positions like ST, CAM, RW)
- Values (numeric and positive)

This ensured data integrity and prevented invalid inputs from breaking the system.

---

## Object-Oriented Programming (OOP)

- **Encapsulation:** Player data is stored within objects
- **Inheritance:** `Player` inherits from `Person`
- **Methods:** Functions like `is_world_class()` define behaviour

This structure made the program more modular and easier to extend.

---

## File I/O

I implemented file handling using CSV files:
- Player data is saved using `csv.DictWriter`
- Data is loaded using `csv.DictReader`

This allows the system to persist data between runs, making it more realistic and practical.

---

## Testing

I created a `run_tests()` function to test key components:
- Input validation functions (regex)
- Player methods (e.g., world-class check)
- File saving functionality

These tests ensure that core features work correctly and help identify bugs early.

---

## Libraries

I used built-in Python libraries:
- `re` for Regular Expressions
- `csv` for file handling

Additionally, I created a custom `Utils` class which acts as a reusable internal library for validation functions.

---

## Challenges and Problem Solving

One of the main challenges was converting my original list-based system into an object-oriented structure. This required rethinking how data was stored and accessed.

Another challenge was implementing validation using regex, as I had to ensure patterns correctly matched valid inputs without being too restrictive.

I solved these issues through testing, debugging, and gradually refactoring my code.

---

## Above and Beyond

To extend beyond the basic requirements, I:
- Built a full CLI menu system
- Added a “one-on-one” player comparison feature
- Implemented a starting lineup system
- Improved code structure and readability

These features demonstrate additional effort and understanding beyond the core requirements.

---

## Conclusion

This project has helped me develop a deeper understanding of Python programming concepts, especially OOP and data validation. Refactoring my original code into a structured system was particularly valuable, as it highlighted the importance of good design.

If I were to continue this project, I would consider adding a graphical user interface (GUI) and more advanced statistics or data analysis features.

---