import datetime
from dataclasses import dataclass

from core.data.Data import Priority, Project_status, Project_domain


@dataclass(init=True, frozen=True)
class Project:
    # main project fields
    title: str  # name of the project
    language: str  # what computer language used for project
    description: str  # project description with details
    project_priority: Priority
    status: Project_status
    project_domain: Project_domain

    # additional fields:
    git_url: str
    last_updated: datetime.date
    created_at: datetime.date

    # qa things:
    has_auto_tests: bool
