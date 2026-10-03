from enum import Enum

class SequenceResult(Enum):
    ACCESS_DONE = 0
    PROCESS_FINISHED = 1
    PAGE_FAULT = 2
    NO_MEMORY = 3