from enum import Enum

class JobStatus(Enum):
    RUNNING = 1
    ERROR = 2
    FINISHED = 3