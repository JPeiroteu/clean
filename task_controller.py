"""
This module defines classes for managing tasks and projects.
"""


class Task:
    """
    Represents a Task with attributes for name, due date, priority, and completion status.
    """

    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return (
            f"Task: {self.name} ({status}) - Due Date: {self.due_date}, "
            f"Priority: {self.priority}"
        )


class Project:
    """
    Represents a Project with attributes for name and a list of tasks.
    """

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_t(self, task):
        self.tasks.remove(task)

    def __str__(a):
        return f"Project: {a.name}"


class ProjectManager:
    """
    Represents a Project Manager that manages a list of projects.
    """

    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def remove_project(self, project):
        self.projects.remove(project)

    def get_project_by_name(self, name):
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def __str__(self):
        project_list = "\n".join(str(project) for project in self.projects)
        return f"Project Manager\nProjects:\n{project_list}"


if __name__ == "__main__":
    project_manager = ProjectManager()

    while True:
        print("1. Add Project")
        print("2. Add Task to Project")
        print("3. Edit Task")
        print("4. Mark Task as Completed")
        print("5. Remove Task from Project")
        print("6. Remove Project")
        print("7. View Projects and Tasks")
        print("0. Exit")

        option = input("Enter your option: ")

        if option == "1":
            project_name = input("Enter Project Name: ")
            project = Project(project_name)
            project_manager.add_project(project)
            print(f"Project '{project_name}' added.\n")

        elif option == "2":
            project_name = input("Enter Project Name: ")
            project = project_manager.get_project_by_name(project_name)
            if project:
                task_name = input("Enter Task Name: ")
                due_date = input("Enter Task Due Date: ")
                priority = input("Enter Task Priority: ")
                status = input("Enter Task Status (Completed/Pending): ")
                task = Task(task_name, due_date, priority)
                if status.lower() == "completed":
                    task.mark_as_completed()
                project.add_task(task)
                print(
                    f"Task '{task_name}' added to Project '{project_name}'.\n")
            else:
                print(f"Project '{project_name}' not found.\n")

        elif option == "3":
            project_name = input("Enter Project Name: ")
            project = project_manager.get_project_by_name(project_name)
            if project:
                task_name = input("Enter Task Name: ")
                for task in project.tasks:
                    if task.name == task_name:
                        new_name = input("Enter New Task Name: ")
                        due_date = input("Enter New Task Due Date: ")
                        priority = input("Enter New Task Priority: ")
                        status = input(
                            "Enter New Task Status (Completed/Pending): ")
                        task.name = new_name
                        task.due_date = due_date
                        task.priority = priority
                        task.completed = (
                            status.lower() == "completed")
                        print(f"Task '{task_name}' edited.\n")
                        break
                else:
                    print(
                        f"Task '{task_name}' not found in Project '{project_name}'.\n")
            else:
                print(f"Project '{project_name}' not found.\n")

        elif option == "4":
            project_name = input("Enter Project Name: ")
            project = project_manager.get_project_by_name(project_name)
            if project:
                task_name = input("Enter Task Name: ")
                for task in project.tasks:
                    if task.name == task_name:
                        task.mark_as_completed()
                        print(f"Task '{task_name}' marked as completed.\n")
                        break
                else:
                    print(
                        f"Task '{task_name}' not found in Project '{project_name}'.\n")
            else:
                print(f"Project '{project_name}' not found.\n")

        elif option == "5":
            project_name = input("Enter Project Name: ")
            project = project_manager.get_project_by_name(project_name)
            if project:
                task_name = input("Enter Task Name: ")
                for task in project.tasks:
                    if task.name == task_name:
                        project.remove_task(task)
                        print(
                            f"Task '{task_name}' removed from Project '{project_name}'.\n")
                        break
                else:
                    print(
                        f"Task '{task_name}' not found in Project '{project_name}'.\n")
            else:
                print(f"Project '{project_name}' not found.\n")

        elif option == "6":
            project_name = input("Enter Project Name: ")
            project = project_manager.get_project_by_name(project_name)
            if project:
                project_manager.remove_project(project)
                print(f"Project '{project_name}' removed.\n")
            else:
                print(f"Project '{project_name}' not found.\n")

        elif option == "7":
            for project in project_manager.projects:
                print(project)
                for task in project.tasks:
                    print(task)
                print()

        elif option == "0":
            break

        else:
            print("Invalid choice. Please try again.\n")
