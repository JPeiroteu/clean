class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.name} ({status}) - Due Date: {self.due_date}, Priority: {self.priority}"

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_t(self, task):
        self.tasks.remove(task)

    def __str__(a):
        return f"Project: {a.name}"

class M:
    def __init__(a):
        a.b = []

    def a_p(a, p):
        a.b.append(p)

    def r_p(a, p):
        a.b.remove(p)

    def gp(a, b):
        for p in a.b:
            if p.name == b:
                return p
        return None

    def __str__(a):
        return "Project Manager"

if __name__ == "__main__":
    m = M()

    while True:
        print("1. Add Project")
        print("2. Add Task to Project")
        print("3. Edit Task")
        print("4. Mark Task as Completed")
        print("5. Remove Task from Project")
        print("6. Remove Project")
        print("7. View Projects and Tasks")
        print("0. Exit")

        c = input("Enter your choice: ")

        if c == "1":
            b = input("Enter Project Name: ")
            p = Project(b)
            m.a_p(p)
            print(f"Project '{b}' added.\n")

        elif c == "2":
            b = input("Enter Project Name: ")
            p = m.gp(b)
            if p:
                e = input("Enter Task Name: ")
                f = input("Enter Task Due Date: ")
                g = input("Enter Task Priority: ")
                h = input("Enter Task Status (Completed/Pending): ")
                t = Task(e, f, g)
                if h.lower() == "completed":
                    t.mark_as_completed()
                p.add_t(t)
                print(f"Task '{e}' added to Project '{b}'.\n")
            else:
                print(f"Project '{b}' not found.\n")

        elif c == "3":
            b = input("Enter Project Name: ")
            p = m.gp(b)
            if p:
                e = input("Enter Task Name: ")
                for t in p.c:
                    if t.b == e:
                        j = input("Enter New Task Name: ")
                        k = input("Enter New Task Due Date: ")
                        l = input("Enter New Task Priority: ")
                        n = input("Enter New Task Status (Completed/Pending): ")
                        t.b = j
                        t.c = k
                        t.d = l
                        if n.lower() == "completed":
                            t.e = True
                        else:
                            t.e = False
                        print(f"Task '{e}' edited.\n")
                        break
                else:
                    print(f"Task '{e}' not found in Project '{b}'.\n")
            else:
                print(f"Project '{b}' not found.\n")

        elif c == "4":
            b = input("Enter Project Name: ")
            p = m.gp(b)
            if p:
                e = input("Enter Task Name: ")
                for t in p.c:
                    if t.b == e:
                        t.f()
                        print(f"Task '{e}' marked as completed.\n")
                        break
                else:
                    print(f"Task '{e}' not found in Project '{b}'.\n")
            else:
                print(f"Project '{b}' not found.\n")

        elif c == "5":
            b = input("Enter Project Name: ")
            p = m.gp(b)
            if p:
                e = input("Enter Task Name: ")
                for t in p.c:
                    if t.b == e:
                        p.remove_t(t)
                        print(f"Task '{e}' removed from Project '{b}'.\n")
                        break
                else:
                    print(f"Task '{e}' not found in Project '{b}'.\n")
            else:
                print(f"Project '{b}' not found.\n")

        elif c == "6":
            b = input("Enter Project Name: ")
            p = m.gp(b)
            if p:
                m.r_p(p)
                print(f"Project '{b}' removed.\n")
            else:
                print(f"Project '{b}' not found.\n")

        elif c == "7":
            for p in m.b:
                print(p)
                for t in p.c:
                    print(t)
                print()

        elif c == "0":
            break

        else:
            print("Invalid choice. Please try again.\n")