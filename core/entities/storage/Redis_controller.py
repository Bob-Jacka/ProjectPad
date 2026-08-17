"""
Cache controller
"""

from redis import Redis


class Redis_controller:
    """
    Some kind of redis wrapper
    """
    inner_redis: Redis | None

    def __init__(self):
        self.inner_redis = Redis(host='localhost', port=6379, db=0)

    def is_inited(self):
        return self.inner_redis is None

    def save_entity(self, entity):
        self.inner_redis.append(entity.title, entity)

    def save_all(self, entities: list):
        for entity in entities:
            self.inner_redis.append(entity.title, entity)

    def contains(self, project_name):
        """
        Check that entity in cache
        """
        return self.inner_redis.exists(project_name)
