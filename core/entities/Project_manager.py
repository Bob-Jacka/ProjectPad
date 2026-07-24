"""
Truly Project Manager for your projects
"""
from typing import Optional

from core.entities.projects_entities.Idea import Idea
from core.entities.projects_entities.Project import Project
from core.entities.storage.Database_controller import Database_controller
from core.entities.storage.File_controller import File_controller


def create_project(title: str, description: Optional[str], languages: list[str], priority, domain):
    """
    Factory method for creating project in this project;
    :param languages: project language (languages)
    :param title: project title (name)
    :param description: guess what
    :param priority: project priority
    :param domain: which domain
    :return: Created project
    """
    return Project(title=title,
                   description=description,
                   language=languages,
                   project_priority=priority,
                   project_domain=domain,
                   last_updated=Project.current_time(),
                   created_at=Project.current_time())


def create_idea(title: str, description: str):
    return Idea(title=title, description=description)


class Project_manager:
    class Storage:
        file_controller: File_controller
        db_controller: Database_controller

        def __init__(self):
            self.file_controller = File_controller()
            self.db_controller = None

        def save_project(self, project):
            self.file_controller.save(project)
            if self.db_controller:
                self.db_controller.save(project)

        def project_count(self):
            pass

        def load_project(self):
            self.file_controller.load()  # TODO continue from this next time
            if self.db_controller:
                self.db_controller.load()

        def delete_project(self, project):
            self.file_controller.delete(project)
            if self.db_controller:
                self.db_controller.delete(project)

        def find_project(self, project_name: str):
            self.file_controller.find(project_name)
            if self.db_controller:
                self.db_controller.find(project_name)

        def update_project(self, project_name: str):
            self.file_controller.update(project_name)
            if self.db_controller:
                self.db_controller.update(project_name)

    storage: Storage
    projects: dict[str, Project | Idea]

    def __init__(self, logger):
        self.projects = dict()
        self.storage = Project_manager.Storage()
        self.local_logger = logger

    def change_project(self, project_name: str):
        self.local_logger.log('Update project run')
        self.storage.update_project(project_name)

    def add_project_or_idea(self, project):
        """
        Save project in inner storage and database
        :param project: project object to add
        :return: None
        """
        self.local_logger.log('Save project run started')
        self.storage.save_project(project)
        self.projects[project.title] = project
        self.local_logger.log('Save project run ended')

    def delete_project(self, project):
        self.local_logger.log('Delete project run started')
        self.storage.delete_project(project)
        self.local_logger.log('Delete project run ended')

    def find_project(self, project_name: str):
        self.local_logger.log('Find project run started')
        self.storage.find_project(project_name)
        self.local_logger.log('Find project run ended')

    def get_all_projects(self) -> list[dict[str, str]]:
        self.local_logger.log('All project select started')
        self.storage.find_project()
        self.local_logger.log('All project select ended')

    def load_projects(self):
        self.local_logger.log('Load projects started')
        self.storage.load_project()
        self.local_logger.log('Load projects ended')
