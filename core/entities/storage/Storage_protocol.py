from typing import Protocol


class Storage_protocol(Protocol):
    """
    Storage protocol for file or database storage
    """

    def save(self, project):
        pass

    def delete(self, project):
        pass

    def find(self, project_name: str):
        pass

    def update(self, project_name: str):
        pass

    def load(self):
        pass
