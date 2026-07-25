from enum import Enum

local_projects_place: str = 'projects'

VERSION: str = '1.0.0'


class Priority(str, Enum):
    """
    Project priority, how fast should project be made
    """
    HIGH = 'High'
    MEDIUM = 'Medium'
    Low = 'Low'


class Project_status(str, Enum):
    """
    Which status project has
    """
    IDEA = 'IDEA'
    PLANNED = 'PLANNED'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'
    ON_HOLD = 'ON_HOLD'


class Project_domain(str, Enum):
    FINTECH = 'FINTECH'
    DATA = 'DATA'
    IoT = 'IoT'
    WEB = 'WEB'
