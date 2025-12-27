tasks = []

def add_task(title: str):
    tasks.append({"title": title, "done": False})

def complete_task(index: int):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def list_tasks():
    return tasks


if __name__ == "__main__":
    add_task("Learn Python")
    add_task("Build projects")
    complete_task(0)
    print(list_tasks())
