from datetime import date
from typing import List
from ui import print_task
from manager import TaskManager
from task import Priority, Task


# функция для добавления новой задачи
def add_task(manager: TaskManager):
    title = input("Введите заголовок задачи: ")
    description = input("Введите описание задачи: ")
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
        description=description,
        category=category,
        due_date=due_date,
        priority=priority,
    )

    manager.add_task(task)


# функция для просмотра задач
def view_tasks(tasks: List[Task]):
    if not tasks:
        print("Соответствующие задачи отсутствуют.")
        return
    else:
        for task in tasks:
            print_task(task)


# функция для просмотра задач по категории
def view_tasks_by_category(manager: TaskManager):
    category = input("Введите категорию для фильтрации: ")
    filtered_tasks = manager.view_tasks_by_category(category)
    view_tasks(filtered_tasks)


# функция для просмотра задач по статусу
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


# функция для просмотра задач по ключевому слову
def view_tasks_by_keywords(manager: TaskManager):
    keyword = input("Введите ключевое слово для поиска: ")
    filtered_tasks = manager.view_tasks_by_keywords(keyword)
    view_tasks(filtered_tasks)


# функция для редактирования задачи
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
        else:
            new_due_date = None
        manager.edit_task(task_id, due_date=new_due_date)
    elif choice == 5:
        new_priority_str = input("Введите новый приоритет (low, medium, high): ")
        if new_priority_str in Priority.__members__:
            new_priority = Priority[new_priority_str]
        else:
            new_priority = Priority.low
        manager.edit_task(task_id, priority=new_priority)


# функция для отметки задачи как выполненной
def complete_task(manager: TaskManager):
    task_id = int(input("Введите ID задачи для завершения: "))
    manager.complete_task(task_id)


# функция для удаления задачи
def delete_task(manager: TaskManager):
    task_id = int(input("Введите ID задачи для удаления: "))
    manager.delete_task(task_id)


# функция для удаления задач по категории
def delete_task_by_category(manager: TaskManager):
    category = input("Введите категорию для удаления задач: ").lower()
    manager.delete_tasks_by_category(category)
