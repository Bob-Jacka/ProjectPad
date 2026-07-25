"""
Sometimes you have got an insight, that's the idea
"""

from dataclasses import dataclass

from core.entities.projects_entities.Project_entity import Project_entity


@dataclass(init=True, frozen=True)
class Idea(Project_entity):
    title: str   # name of the project
    description: str  # project description with details
