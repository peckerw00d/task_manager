from dataclasses import dataclass, field
from enum import Enum
import json
from unicodedata import category
from uuid import UUID, uuid4
from datetime import date, datetime

from httpx import delete


class Priority(Enum):
    low = "Низкий"
    medium = "Средний"
    high = "Высокий"


@dataclass
class Task:
    id: int = None
    title: str = None
    description: str = None
    category: str = None
    due_date: str = None
    priority: Priority = Priority.low
    status: bool = False


class TaskManager:
    def __init__(self, tasks=None, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = tasks if tasks is not None else []
        self._id_counter = 1
        if self.tasks:
            self._id_counter = max(task.id for task in self.tasks) + 1

    def add_task(self, task: Task):
        task.id = self._id_counter
        self.tasks.append(task)
        self._id_counter += 1
        print(f'Задача "{task.title}" успешно добавлена!')

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def view_tasks_by_category(self, category: str):
        filtered_tasks = [task for task in self.tasks if task.category == category]
        for task in filtered_tasks:
            print(task)

    def view_tasks_by_status(self, status: bool):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        for task in filtered_tasks:
            print(task)

    def view_tasks_by_keywords(self, keyword: str):
        filtered_tasks = [
            task
            for task in self.tasks
            if keyword in task.title or keyword in task.description
        ]
        print(filtered_tasks)

    def edit_task(self, task_id: int, **kwargs):
        for task in self.tasks:
            if task.id == task_id:
                for key, value in kwargs.items():
                    setattr(task, key, value)
                print(f'Задача "{task.title}" успешно добавлена!')
                return
        print(print(f'Задача "{task.title}" не найдена.'))

    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.status = True
                print(f'Задача "{task.title} отмечена как выполненная!"')
                return
        print(print(f'Задача "{task.title}" не найдена.'))

    def delete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)

    def delete_tasks_by_category(self, category: str):
        self.tasks = [task for task in self.tasks if task.category != category]

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                self.tasks = []
                Task._id_counter = 0
                for task_dict in data:
                    priority = Priority[task_dict["priority"]]
                    due_date = (
                        date.fromisoformat(task_dict["due_date"])
                        if task_dict["due_date"]
                        else None
                    )
                    task = Task(
                        id=task_dict["id"],
                        title=task_dict["title"],
                        description=task_dict["description"],
                        category=task_dict["category"],
                        due_date=due_date,
                        priority=priority,
                        status=task_dict["status"],
                    )
                    self.tasks.append(task)
                    if task.id > self._id_counter:
                        self._id_counter = task.id
                self._id_counter += 1
            print("Задачи успешно загружены из файла.")
        except FileNotFoundError:
            print("Файл не найден. Нет задач для загрузки.")
        except json.JSONDecodeError:
            print("Ошибка при загрузке задач из файла.")

    def save_tasks(self):
        try:
            data = []
            for task in self.tasks:
                task_dict = {
                    "id": task.id,
                    "title": task.title,
                    "description": task.description,
                    "category": task.category,
                    "due_date": task.due_date.isoformat() if task.due_date else None,
                    "priority": task.priority.name,
                    "status": task.status,
                }
                data.append(task_dict)
            with open(self.file_name, "w") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print("Задачи успешно сохранены в файл.")
        except IOError:
            print("Ошибка при сохранении задач в файл.")
