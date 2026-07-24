from redis import Redis


class Redis_controller:
    """
    Some kind of redis wrapper
    """
    inner_redis: Redis

    def __init__(self):
        self.inner_redis = Redis(host='localhost', port=6379, db=0)
