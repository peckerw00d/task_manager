from task import Task


# удобочитаемый вывод задачи в консоль
def print_task(task: Task):
    print(f"ID: {task.id}")
    print(f"Title: {task.title}")
    print(f"Description: {task.description}")
    print(f"Category: {task.category}")
    print(f"Due Date: {task.due_date}")
    print(f"Priority: {task.priority}")
    print(f"Status: {'Completed' if task.status else 'Not Completed'}")
    print("-" * 30, "\n")


# вывод меню возможный действий
def display_menu(menu: dict):
    print("\nМеню:\n")
    for key, value in menu.items():
        print(f"{key}:", value)
