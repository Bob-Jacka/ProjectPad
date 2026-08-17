"""
Project to create
"""

import datetime
from dataclasses import dataclass

from core.data.Data import Priority, Project_status, Project_domain
from core.entities.projects_entities.IProject_entity import IProject_entity


@dataclass(init=True, frozen=True)
class Project(IProject_entity):
    # main project fields
    title: str  # name of the project
    description: str | None  # project description with details
    languages: list[str]  # what computer language used for project
    project_priority: Priority
    project_domains: list[Project_domain]

    # additional fields:
    last_updated: str
    created_at: str

    status: Project_status = Project_status.PLANNED
    git_url: str = ''

    # qa things:
    has_auto_tests: bool = False

    @staticmethod
    def convert_to_column_id(status: Project_status):
        """
        Adapter method for project card dock
        :param status: project status
        :return: column id
        """
        match status:
            case Project_status.IDEA.value:
                return 1
            case Project_status.PLANNED.value:
                return 2
            case Project_status.IN_PROGRESS.value:
                return 3
            case Project_status.DONE.value:
                return 4
            case Project_status.ON_HOLD.value:
                return 5
            case _:
                raise Exception(f'Unknown project status: "{status}", implement it first')

    @staticmethod
    def current_time() -> str:
        """
        Utility function for updating time for project
        :return: current datetime
        """
        return datetime.datetime.now().__str__()
