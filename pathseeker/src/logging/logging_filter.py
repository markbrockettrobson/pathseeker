from logging import Filter, LogRecord
from typing import Collection


class LevelFilter(Filter):
    def __init__(self, logging_levels_to_allow: Collection[int]):
        super().__init__()
        self._logging_levels = logging_levels_to_allow

    def filter(self, record: LogRecord):
        return record.levelno in self._logging_levels
