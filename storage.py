import json
from datetime import date

from task import Priority, Task


class TaskStorage:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                tasks = []
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
                    tasks.append(task)
                print("Задачи успешно загружены из файла.")
                self.tasks = tasks
                return self
        except FileNotFoundError:
            print("Файл не найден. Нет задач для загрузки.")
            self.tasks = []
            return self
        except json.JSONDecodeError:
            print("Ошибка при загрузке задач из файла.")
            self.tasks = []
            return self

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
