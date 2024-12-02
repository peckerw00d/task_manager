from dataclasses import dataclass
from enum import Enum
from datetime import date



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
    due_date: date = None
    priority: Priority = Priority.low
    status: bool = False
