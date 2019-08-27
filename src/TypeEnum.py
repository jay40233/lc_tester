from enum import Enum


class DataType(Enum):
    UNKNOWN = 0
    LIST_OF_LIST = 1
    LIST = 2
    STRING = 3
    INTEGER = 4
    FLOAT = 5
    TREE = 6
    LINKED_LIST = 7


class ResultType(Enum):
    ERROR = -1
    PASSED = 0
    FAILED = 1
    SKIPPED = 2
