from solution_optimized import TodoApp

app = TodoApp()
app.add_task("Write code")
app.add_task("Test app")
app.mark_done(0)

assert len(app.pending_tasks()) == 1
print("Todo app tests passed")
