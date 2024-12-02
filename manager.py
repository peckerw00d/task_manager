from storage import TaskStorage
from task import Task


class TaskManager:
    def __init__(self, tasks=None, storage=None):
        self.storage = storage if storage else TaskStorage()
        self.tasks = tasks if tasks is not None else []
        self._id_counter = 1
        if self.tasks:
            self._id_counter = max(task.id for task in self.tasks) + 1

    def add_task(self, task: Task):
        if not task.title or not task.category:
            print("Задача должна иметь заголовок и категорию.")
            return
        task.id = self._id_counter
        self.tasks.append(task)
        self._id_counter += 1
        print(f'Задача "{task.title}" успешно добавлена!')

    def view_tasks(self):
        for task in self.tasks:
            print(task.__dict__)

    def filter_tasks(self, condition):
        return [task.__dict__ for task in self.tasks if condition(task)]

    def view_tasks_by_category(self, category: str):
        filtered_tasks = self.filter_tasks(lambda task: task.category == category)
        for task in filtered_tasks:
            print(task)

    def view_tasks_by_status(self, status: bool):
        filtered_tasks = self.filter_tasks(lambda task: task.status == status)
        for task in filtered_tasks:
            print(task)

    def view_tasks_by_keywords(self, keyword: str):
        filtered_tasks = self.filter_tasks(lambda task: task.keyword == keyword)
        for task in filtered_tasks:
            print(task)

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
                print(f'Задача "{task.title} отмечена как выполненная!"')
                return
        print(print(f'Задача "{task.title}" не найдена.'))

    def delete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)

    def delete_tasks_by_category(self, category: str):
        inintal_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.category != category]
        deleted_count = inintal_count - len(self.tasks)
        print(f'Удалено {deleted_count} задач категории "{category}".')
