"""
Just note about project
"""
from dataclasses import dataclass

from core.entities.projects_entities.IProject_entity import IProject_entity


@dataclass(init=True, frozen=True)
class Note(IProject_entity):
    pass
