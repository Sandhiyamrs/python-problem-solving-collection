class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str):
        self.tasks.append({"title": title, "done": False})

    def mark_done(self, index: int):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index")
        self.tasks[index]["done"] = True

    def pending_tasks(self):
        return [t for t in self.tasks if not t["done"]]
