"""
Truly Project Manager for your projects
"""
from random import randint
from typing import Optional

from core.entities.projects_entities.Enhancement import Enhancement
from core.entities.projects_entities.IProject_entity import IProject_entity
from core.entities.projects_entities.Idea import Idea
from core.entities.projects_entities.Note import Note
from core.entities.projects_entities.Project import Project
from core.entities.storage.Database_controller import Database_controller
from core.entities.storage.File_controller import File_controller
from core.entities.storage.Kafka_controller import Kafka_controller
from core.entities.storage.Redis_controller import Redis_controller


def create_project(title: str, description: Optional[str], languages: list[str], priority, domains):
    """
    Factory method for creating projects in this project;
    :param languages: project language (languages)
    :param title: project title (name)
    :param description: guess what
    :param priority: project priority
    :param domains: which domain
    :return: Created project
    """
    return Project(title=title,
                   description=description,
                   languages=languages,
                   project_priority=priority,
                   project_domains=domains,
                   last_updated=Project.current_time(),
                   created_at=Project.current_time())


def create_idea(title: str, description: str):
    return Idea(title=title, description=description)


def create_note():
    return Note()


def create_enhancement(description: str, created_at):
    return Enhancement(description=description, created_at=created_at)


class Entity_manager:
    """
    Control all entities
    """

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

        def load_projects(self) -> dict[str, Project]:
            return self.file_controller.load()  # TODO get both objects and compare them on last time update
            if self.db_controller:
                self.db_controller.load()

        def delete_project(self, project_title):
            self.file_controller.delete(project_title)
            if self.db_controller:
                self.db_controller.delete(project_title)

        def update_project(self, project):
            self.file_controller.update(project)
            if self.db_controller:
                self.db_controller.update(project)

    kafka_controller: Kafka_controller = None
    cache_controller: Redis_controller | None
    storage: Storage
    projects: dict[str, IProject_entity]

    def __init__(self, logger):
        self.projects = dict()
        self.storage = Entity_manager.Storage()
        self.cache_controller = Redis_controller()
        self.local_logger = logger

    def change_project(self, project: Project):
        """
        Fully rewrite project with new entity
        :param project: project to write above the old
        :return: None
        """
        self.local_logger.log('Update project run started')
        if self.cache_controller.contains(project):
            pass
        else:
            self.storage.update_project(project)
        self.local_logger.log('Update project run ended')

    def add_project_or_idea(self, entity):
        """
        Save project in inner storage and database
        :param entity: project object to add
        :return: None
        """
        self.local_logger.log('Save project run started')
        self.projects[entity.title] = entity
        self.cache_controller.save_entity(entity)
        self.local_logger.log('Save project run ended')

    def delete_project(self, project_title):
        """
        Delete project from storage
        :param project_title: name of the project to delete
        :return: None
        """
        self.local_logger.log('Delete project run started')
        self.storage.delete_project(project_title)
        self.local_logger.log('Delete project run ended')

    def find_project(self, project_name: str):
        """
        Find project in storages
        :param project_name:
        :return:
        """
        self.local_logger.log('Find project run started')
        self.local_logger.log('Find project run ended')
        return self.projects.get(project_name)

    def get_all_projects(self) -> list[dict[str, str]]:
        """
        Get all projects from storage and return them
        :return: projects
        """
        to_return: list[dict[str, str]] = list()
        self.local_logger.log('All project select started')
        for project_title, project in self.projects.items():
            to_return.append({"id": f'{randint(1, 10)}', "title": project_title, "column_id": Project.convert_to_column_id(project.status)})
        self.local_logger.log('All project select ended')
        return to_return

    def load_projects(self):
        """
        Load projects from storage
        :return: None
        """
        self.local_logger.log('Load projects started')
        self.projects = self.storage.load_projects()
        self.local_logger.log('Load projects ended')

    def real_save(self):
        for entity in self.projects:
            self.storage.save_project(entity)
