# Clean Code Refactoring

This is a repository containing an old project that I originally created some time ago. Recently, I decided to revisit the project and apply the principles of clean code through refactoring to improve its overall quality, readability, and maintainability.

<br>

## About the Project

The project is a task management application written in Python. It allows users to add projects, add tasks to projects, edit tasks, mark tasks as completed, remove tasks from projects, remove projects, and view the list of projects and tasks.

<br>

## Refactoring Process

During the refactoring process, I focused on identifying and addressing code smells and potential quality issues present in the original code. Some of the improvements made include:

- Improved naming conventions for variables, functions, and classes to make the code more self-explanatory and easier to understand.
- Created separate classes (`Project`, `Task`, and `ProjectManager`) to encapsulate data and behavior, adhering to the Single Responsibility Principle (SRP).
- Eliminated code duplication and introduced helper functions to handle repetitive tasks, enhancing code readability and maintainability.
- Reorganized the code structure to make it more logical and easier to navigate.
- Used string constants to improve readability and simplify logic where needed.

<br>

## Pylint Results

<img width="971" alt="Screenshot 2023-07-30 at 14 16 59" src="https://github.com/JPeiroteu/clean/assets/79811891/9de05b1a-4ab9-41b9-ad5d-a4068b69d245"><br><br>

## Running the Application

To run the application, execute the `task_controller.py` file. The application will prompt you with a menu of options to manage projects and tasks.

<br>

## Conclusion

The process of refactoring and applying clean code principles to this project has resulted in a more organized, readable, and maintainable codebase. By following clean code practices, the application is now better equipped to handle future updates and improvements.

Explore the code and the associated `test_task_controller.py` file to see the improvements made during the refactoring process.
