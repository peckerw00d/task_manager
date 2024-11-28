from dataclasses import dataclass, field
from enum import Enum
from uuid import UUID, uuid4
from datetime import date, datetime


class Priority(Enum):
    low = "Низкий"
    medium = "Средний"
    high = "Высокий"


@dataclass
class Task:
    id: int = field(default_factory=lambda: Task._next_id())
    title: str = None
    description: str = None
    category: str = None
    due_count: str = None
    priority: Priority = Priority.low
    status: bool = False

    _id_counter: int = field(default=0, init=False, repr=False, compare=False)

    @classmethod
    def _next_id(cls):
        cls._id_counter += 1
        return cls._id_counter

