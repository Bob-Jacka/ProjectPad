from typing import Protocol


class Storage_protocol(Protocol):
    """
    Storage protocol for file or database storage
    """

    def save(self, project) -> None:
        """
        Save current project in storage
        :param project: current project
        :return: None
        """
        pass

    def delete(self, project) -> None:
        """
        Delete current project from storage
        :param project: current project
        :return: None
        """
        pass

    def update(self, project) -> None:
        """
        Update current project
        :param project: which project to update
        :return: None
        """
        pass

    def load(self):
        """
        Load all projects
        :return: dict with entities
        """
        pass
