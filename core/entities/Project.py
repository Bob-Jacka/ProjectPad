from dataclasses import dataclass
from enum import Enum


class Priority(str, Enum):
    HIGH = 'High'
    MEDIUM = 'Medium'
    Low = 'Low'


@dataclass(init=True, frozen=True)
class Project:
    title: str  # name of the project
    language: str  # what computer language used for project
    project_priority: Priority
