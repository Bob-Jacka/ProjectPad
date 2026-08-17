"""
Some enhancement to existing project
"""
from dataclasses import dataclass

from core.entities.projects_entities.IProject_entity import IProject_entity


@dataclass(init=True, frozen=True)
class Enhancement(IProject_entity):
    description: str
    created_at: str
