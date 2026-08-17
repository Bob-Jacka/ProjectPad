from core.entities.storage.nosql.Wrapper import Nosql_db_wrapper
from core.entities.storage.nosql.implementation.Mongo import Mongo_impl


class Database_controller:
    """
    Class for noSql database actions
    """
    db_implementation: Nosql_db_wrapper

    def __init__(self):
        self.db_implementation = Mongo_impl('projects')

    def save(self, project):
        pass

    def delete(self, project_title):
        pass

    def update(self, project):
        pass

    def load(self):
        pass
