"""
Unit tests for the task_controller module
"""

import unittest
from task_controller import Task, Project, ProjectManager

class TestTaskController(unittest.TestCase):
    def setUp(self):
        # Initialization of test data
        self.project_manager = ProjectManager()

        # Adding projects and tasks for testing
        project1 = Project("Project 1")
        project1.add_task(Task("Task 1", "2023-12-31", "High"))
        self.project_manager.add_project(project1)

        project2 = Project("Project 2")
        project2.add_task(Task("Task 2", "2023-11-30", "Medium"))
        self.project_manager.add_project(project2)

    def test_add_project(self):
        self.project_manager.add_project(Project("Project 3"))
        projects = [p.name for p in self.project_manager.projects]
        self.assertIn("Project 3", projects)

    def test_add_task(self):
        self.project_manager.add_project(Project("Project 3"))
        project3 = self.project_manager.get_project_by_name("Project 3")
        project3.add_task(Task("Task 3", "2023-10-31", "Low"))
        tasks = [t.name for t in project3.tasks]
        self.assertIn("Task 3", tasks)

    def test_edit_task(self):
        project1 = self.project_manager.get_project_by_name("Project 1")
        task = project1.tasks[0]
        task.b = "Edited Task"
        task.c = "2023-12-30"
        task.d = "Low"
        self.assertEqual(task.b, "Edited Task")
        self.assertEqual(task.c, "2023-12-30")
        self.assertEqual(task.d, "Low")

    def test_mark_task_as_completed(self):
        project2 = self.project_manager.get_project_by_name("Project 2")
        task = project2.tasks[0]
        task.mark_as_completed()
        self.assertTrue(task.completed)

    def test_remove_task(self):
        project1 = self.project_manager.get_project_by_name("Project 1")
        task = project1.tasks[0]
        project1.remove_t(task)
        tasks = [t.b for t in project1.tasks]
        self.assertNotIn("Task 1", tasks)

    def test_remove_project(self):
        project1 = self.project_manager.get_project_by_name("Project 1")
        self.project_manager.remove_project(project1)
        projects = [p.name for p in self.project_manager.projects]
        self.assertNotIn("Project 1", projects)

if __name__ == '__main__':
    unittest.main()
