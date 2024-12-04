from manager import TaskManager
from ui import display_menu
import actions

# список с названиями всех доступных действий  
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
    "Завершение работы",
]


def main():
    with TaskManager() as manager:
        menu_actions = dict(enumerate(ACTIONS, start=1))
        while True:
            display_menu(menu_actions)
            choice = int(input("\nВыберите номер дейсвтия: "))

            if choice == 1:
                actions.add_task(manager)

            elif choice == 2:
                actions.view_tasks(manager.tasks)

            elif choice == 3:
                actions.view_tasks_by_category(manager)

            elif choice == 4:
                actions.view_tasks_by_status(manager)

            elif choice == 5:
                actions.view_tasks_by_keywords(manager)

            elif choice == 6:
                actions.edit_task(manager)

            elif choice == 7:
                actions.complete_task(manager)

            elif choice == 8:
                actions.delete_task(manager)

            elif choice == 9:
                actions.delete_task_by_category(manager)

            elif choice == 10:
                break

            else:
                print("Неверный выбор. Пожалуйста, введите номер действия из меню.")


if __name__ == "__main__":
    main()
