"""
Truly Project Manager for your projects
"""
from core.entities.File_controller import File_controller


class Project_manager:
    file_controller: File_controller

    def __init__(self, logger):
        self.file_controller = File_controller()
        self.local_logger = logger

    def update_project(self):
        pass

    def save_project(self, project):
        self.local_logger.log('Save project run')
        self.file_controller.save_project()

    def delete_project(self, project):
        self.local_logger.log('Delete project run')
        self.file_controller.delete_project()

    def find_project(self, project_name: str):
        self.local_logger.log('Find project run')
        self.file_controller.find_project()
