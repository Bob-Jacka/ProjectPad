import os
from os.path import exists
from pathlib import Path
from typing import Any

from core.data import Data


class File_controller:
    local_save_path: str

    def __init__(self):
        self.local_save_path = Path().parent.absolute().as_posix()
        if not exists(self.path_to_projects()):
            os.mkdir(self.path_to_projects())

    def save(self, project):
        with open(self.path_to_projects() + os.sep + project.title, 'w+') as project_file:
            project_file.write(f'project name: {project.title}\n')
            project_file.write(f'description: {'None' if project.description == '' else project.description}\n')
            project_file.write(f'languages: {project.language}\n')
            project_file.write(f'domains: {project.project_domain}\n')
            project_file.write(f'status: {project.status}\n')
            project_file.write(f'priority: {project.project_priority}\n')
            project_file.write(f'created at: {project.created_at}\n')
            project_file.write(f'last time updated: {project.last_updated}\n')

    def load(self, project):
        project: Any

        with open(self.path_to_projects() + os.sep + project.title, 'w+') as project_file:
            for line in project_file:
                pass

            project_file.write(f'Project name: {project.title}\n')
            project_file.write(f'\tdescription: {'None' if project.description == '' else project.description}\n')
            project_file.write(f'\tlanguages: {project.language}\n')
            project_file.write(f'\tdomains: {project.project_domain}\n')
            project_file.write(f'\tstatus: {project.status}\n')
            project_file.write(f'\tpriority: {project.project_priority}\n')
            project_file.write(f'\tcreated at: {project.created_at}\n')
            project_file.write(f'\tlast time updated: {project.last_updated}\n')

    def delete(self, project_title):
        pass

    def find(self, project_name: str):
        pass

    def update(self, project_name: str):
        pass

    def path_to_projects(self):
        return self.local_save_path + os.sep + Data.local_projects_place
