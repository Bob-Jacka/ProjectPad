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

    def save(self, project) -> None:
        with open(self.path_to_projects() + os.sep + project.title, 'w+') as project_file:
            project_file.write(f'title: {project.title}\n')
            project_file.write(f'description: {'None' if project.description == '' else project.description}\n')
            project_file.write(f'languages: {project.languages}\n')
            project_file.write(f'project_domains: {project.project_domains}\n')
            project_file.write(f'status: {project.status.value}\n')
            project_file.write(f'project_priority: {project.project_priority}\n')
            project_file.write(f'created_at: {project.created_at}\n')
            project_file.write(f'last_updated: {project.last_updated}\n')

    def load(self) -> dict[str, Any]:
        from core.entities.projects_entities.Project import Project
        projects: dict[str, Project] = dict()

        projects_titles: list[str] = os.listdir(self.path_to_projects() + os.sep)

        for project_title in projects_titles:
            result = {}
            pairs: list[str] = open(self.path_to_projects() + os.sep + project_title, 'r').readlines()
            for pair in pairs:
                key, value = pair.split(":", 1)
                key = key.strip()
                value = value.strip()
                result[key] = value

            project: Project = Project(**result)
            projects[project.title] = project
        return projects

    def delete(self, project_title):
        pass

    def update(self, project):
        pass

    def path_to_projects(self):
        return self.local_save_path + os.sep + Data.local_projects_place
