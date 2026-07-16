from typing import Protocol


class Storage(Protocol):
    """
    Storage protocol
    """

    def save_project(self, project):
        pass

    def delete_project(self, project):
        pass

    def find_project(self, project_name: str):
        pass
