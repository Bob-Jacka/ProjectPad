"""
Sometimes you have got an insight, that's the idea
"""

from dataclasses import dataclass

from core.entities.projects_entities.IProject_entity import IProject_entity


@dataclass(init=True, frozen=True)
class Idea(IProject_entity):
    title: str   # name of the project
    description: str  # project description with details
