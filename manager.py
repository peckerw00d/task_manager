from storage import TaskStorage
from task import Task


class TaskManager:
    def __init__(self, tasks=None, storage=None):
        self.storage = storage if storage else TaskStorage()
        self.tasks = tasks if tasks is not None else []
        self._id_counter = 1
        if self.tasks:
            self._id_counter = max(task.id for task in self.tasks) + 1

    def __enter__(self):
        self.storage.load_tasks()
        self.tasks = self.storage.tasks
        if self.tasks:
            self._id_counter = max(task.id for task in self.tasks) + 1
        else:
            self._id_counter = 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.storage.tasks = self.tasks
        self.storage.save_tasks()

    def add_task(self, task: Task):
        if not task.title or not task.category:
            print("Задача должна иметь заголовок и категорию.")
            return
        task.id = self._id_counter
        self.tasks.append(task)
        self._id_counter += 1
        print(f'Задача "{task.title}" успешно добавлена!')

    def view_tasks(self):
        return self.tasks

    def filter_tasks(self, condition):
        return [task for task in self.tasks if condition(task)]

    def view_tasks_by_category(self, category: str):
        return self.filter_tasks(lambda task: task.category == category)

    def view_tasks_by_status(self, status: bool):
        return self.filter_tasks(lambda task: task.status == status)

    def view_tasks_by_keywords(self, keyword: str):
        return self.filter_tasks(
            lambda task: keyword.lower() in task.title.lower()
            or keyword in task.description.lower()
        )

    def edit_task(self, task_id: int, **kwargs):
        for task in self.tasks:
            if task.id == task_id:
                for key, value in kwargs.items():
                    setattr(task, key, value)
                print(f'Задача "{task.title}" успешно отредактирована.')
                return
        print(f"Задача с id {task_id} не найдена.")

    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.status = True
                print(f'Задача "{task.title}" отмечена как выполненная.')
                return
        print(f"Задача с id {task_id} не найдена.")

    def delete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Задача с id {task_id} удалена.")
                return
        print(f"Задача с id {task_id} не найдена.")

    def delete_tasks_by_category(self, category: str):
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.category != category]
        deleted_count = initial_count - len(self.tasks)
        print(f'Удалено {deleted_count} задач категории "{category}".')