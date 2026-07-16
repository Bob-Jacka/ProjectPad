from enum import Enum


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
    PLANNED = 'Planned'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    ON_HOLD = 'On hold'


class Project_domain(str, Enum):
    FINTECH = 'fintech'
    DATA = 'data'
    IoT = 'iot'
    WEB = 'web'
