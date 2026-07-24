"""
Project to create
"""

import datetime
from dataclasses import dataclass

from core.data.Data import Priority, Project_status, Project_domain


@dataclass(init=True, frozen=True)
class Project:
    # main project fields
    title: str  # name of the project
    description: str | None  # project description with details
    language: list[str]  # what computer language used for project
    project_priority: Priority
    project_domain: Project_domain

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
            case Project_status.IDEA:
                return 0
            case Project_status.PLANNED:
                return 1
            case Project_status.IN_PROGRESS:
                return 2
            case Project_status.DONE:
                return 3
            case Project_status.ON_HOLD:
                return 4
            case _:
                raise Exception(f'Unknown project status: "{status}", implement it first')

    @staticmethod
    def current_time() -> str:
        """
        Utility function for updating time for project
        :return: current datetime
        """
        return datetime.datetime.now().__str__()
