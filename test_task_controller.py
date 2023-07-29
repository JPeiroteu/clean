import unittest
from task_controller import T, P, M

class TestTaskController(unittest.TestCase):
    def setUp(self):
        # Initialization of test data
        self.project_manager = M()

        # Adding projects and tasks for testing
        project1 = P("Project 1")
        project1.add_t(T("Task 1", "2023-12-31", "High"))
        self.project_manager.a_p(project1)

        project2 = P("Project 2")
        project2.add_t(T("Task 2", "2023-11-30", "Medium"))
        self.project_manager.a_p(project2)

    def test_add_project(self):
        self.project_manager.a_p(P("Project 3"))
        projects = [p.b for p in self.project_manager.b]
        self.assertIn("Project 3", projects)

    def test_add_task(self):
        self.project_manager.a_p(P("Project 3"))
        project3 = self.project_manager.gp("Project 3")
        project3.add_t(T("Task 3", "2023-10-31", "Low"))
        tasks = [t.b for t in project3.c]
        self.assertIn("Task 3", tasks)

    def test_edit_task(self):
        project1 = self.project_manager.gp("Project 1")
        project1.c[0].b = "Edited Task"
        project1.c[0].c = "2023-12-30"
        project1.c[0].d = "Low"
        task = project1.c[0]
        self.assertEqual(task.b, "Edited Task")
        self.assertEqual(task.c, "2023-12-30")
        self.assertEqual(task.d, "Low")

    def test_mark_task_as_completed(self):
        project2 = self.project_manager.gp("Project 2")
        project2.c[0].f()
        task = project2.c[0]
        self.assertTrue(task.e)

    def test_remove_task(self):
        project1 = self.project_manager.gp("Project 1")
        project1.remove_t(project1.c[0])
        tasks = [t.b for t in project1.c]
        self.assertNotIn("Task 1", tasks)

    def test_remove_project(self):
        self.project_manager.r_p(self.project_manager.gp("Project 1"))
        projects = [p.b for p in self.project_manager.b]
        self.assertNotIn("Project 1", projects)

if __name__ == '__main__':
    unittest.main()
