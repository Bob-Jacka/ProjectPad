"""
Some enhancement to existing project
"""
from dataclasses import dataclass

from core.entities.projects_entities.Project_entity import Project_entity


@dataclass(init=True, frozen=True)
class Enhancement(Project_entity):
    description: str
    created_at: str
