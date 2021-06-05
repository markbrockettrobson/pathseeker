from abc import ABCMeta, abstractmethod
from logging import Logger
from typing import Optional


class ILoggingManager(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_logger(logger_name: str) -> Logger:
        pass

    @staticmethod
    @abstractmethod
    def get_child_logger(logger_name: str, parent_logger: Optional[Logger]) -> Logger:
        pass
