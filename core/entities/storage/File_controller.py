import os
from os.path import exists
from pathlib import Path


class File_controller:
    start_directory: str

    def __init__(self):
        self.start_directory = Path().parent.absolute().as_posix()
        if not exists(self.path_to_projects()):
            os.mkdir(self.path_to_projects())

    def save_project(self, project):
        pass

    def delete_project(self, project):
        pass

    def find_project(self, project_name: str):
        pass

    def path_to_projects(self):
        return self.start_directory + os.sep + 'projects'
