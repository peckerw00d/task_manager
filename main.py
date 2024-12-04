from datetime import date
from typing import List
from manager import TaskManager
from task import Priority, Task


manager = TaskManager()

METHODS = [
    manager.add_task,
    manager.view_tasks,
    manager.view_tasks_by_category,
    manager.view_tasks_by_keywords,
    manager.view_tasks_by_status,
    manager.edit_task,
    manager.complete_task,
    manager.delete_task,
    manager.delete_tasks_by_category,
]

ACTIONS = [
    "Добавление новой задачи",
    "Просмотр всех задач",
    "Просмотр задач по категории",
    "Просмотр задач по статусу",
    "Просмотр задач по ключевому слову",
    "Редактирование задачи",
    "Отметка задачи как выполненной",
    "Удаление задачи",
    "Удаление задач по категории",
    "Завершение работы"
]


def print_task(task: Task):
    print(f"ID: {task.id}")
    print(f"Title: {task.title}")
    print(f"Description: {task.description}")
    print(f"Category: {task.category}")
    print(f"Due Date: {task.due_date}")
    print(f"Priority: {task.priority}")
    print(f"Status: {'Completed' if task.status else 'Not Completed'}")
    print("-" * 30, "\n")


def add_task(manager: TaskManager):
    title = input("Введите заголовок задачи: ")
    desctiption = input("Введите описание задачи: ")
    category = input("Введите название категории задачи: ")
    due_date_str = input(
        "Введите дату выполнения задачи (YYYY-MM-DD) или оставьте поле пустым: "
    )
    if due_date_str:
        due_date = date.fromisoformat(due_date_str)
    else:
        due_date = None
    priority_str = input("Введите приоритет задачи (low, medium, high): ")
    if priority_str in Priority.__members__:
        priority = Priority[priority_str]
    else:
        priority = Priority.low

    task = Task(
        title=title,
        description=desctiption,
        category=category,
        due_date=due_date,
        priority=priority,
    )

    manager.add_task(task)


def view_tasks(tasks: List[Task]):
    if not tasks:
        print("Соответствующие задачи отсутствуют.")
        return
    else:
        for task in tasks:
            print_task(task)


def view_tasks_by_category(manager: TaskManager):
    category = input("Введите категории для фильтрации: ")
    filtered_tasks = manager.view_tasks_by_category(category)
    view_tasks(filtered_tasks)


def view_tasks_by_status(manager: TaskManager):
    status_str = input("Введите статус для фильтрации (True/False): ").lower()
    if status_str == "true":
        status = True
    elif status_str == "false":
        status = False
    else:
        print("Неверный статус.")
        return

    filtered_tasks = manager.view_tasks_by_status(status)
    view_tasks(filtered_tasks)


def view_tasks_by_keywords(manager: TaskManager):
    keyword = input("Введите ключевое слово для поиска: ")
    filtered_tasks = manager.view_tasks_by_keywords(keyword)
    view_tasks(filtered_tasks)


def edit_task(manager: TaskManager):
    task_id = int(input("Введите ID задачи для редактирования: "))

    print("Какое поле вы хотите изменить?\n")
    print("1. Title")
    print("2. Description")
    print("3. Category")
    print("4. Due Date")
    print("5. Priority")
    choice = int(input("Введите номер поля: "))

    if choice == 1:
        new_title = input("Введите новый заголовок: ")
        manager.edit_task(task_id, title=new_title)

    elif choice == 2:
        new_description = input("Введите новое описание: ")
        manager.edit_task(task_id, description=new_description)

    elif choice == 3:
        new_category = input("Введите новую категорию: ")
        manager.edit_task(task_id, category=new_category)

    elif choice == 4:
        new_due_date_str = input(
            "Введите новую дату (YYYY-MM-DD) или оставьте поле пустым: "
        )

        if new_due_date_str:
            new_due_date = date.fromisoformat(new_due_date_str)

        manager.edit_task(task_id, new_due_date=new_due_date)

    elif choice == 5:
        new_priority_str = input("Введите новый приоритет (low, medium, high): ")

        if new_priority_str in Priority.__members__:
            new_priority = Priority[new_priority_str]

        else:
            new_priority = Priority.low

        manager.edit_task(task_id, priority=new_priority)


def complete_task(manager: TaskManager):
    task_id = int(input("Введите ID задачи для завершения: "))
    manager.complete_task(task_id)


def delete_task(manager: TaskManager):
    task_id = int(input("Введите ID задачи для удаления: "))
    manager.delete_task(task_id)


def delete_task_by_category(manager: TaskManager):
    category = input("Введите категорию для удаления задач: ").lower()
    manager.delete_tasks_by_category(category)


def display_menu(menu: dict):
    print("\nМеню:\n")
    for key, value in menu.items():
        print(f"{key}:", value)


def main():
    with TaskManager() as manager:
        actions = dict(enumerate(ACTIONS, start=1))
        while True:
            display_menu(actions)
            choice = int(input("\nВыберите номер дейсвтия: "))

            if choice == 1:
                add_task(manager)

            elif choice == 2:
                view_tasks(manager.tasks)

            elif choice == 3:
                view_tasks_by_category(manager)

            elif choice == 4:
                view_tasks_by_status(manager)

            elif choice == 5:
                view_tasks_by_keywords(manager)

            elif choice == 6:
                edit_task(manager)

            elif choice == 7:
                complete_task(manager)

            elif choice == 8:
                delete_task(manager)

            elif choice == 9:
                delete_task_by_category(manager)

            elif choice == 10:
                break

            else:
                print("Неверный выбор. Пожалуйста, введите номер действия из меню.")


if __name__ == "__main__":
    main()
