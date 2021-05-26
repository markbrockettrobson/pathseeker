from abc import ABCMeta, abstractmethod

from pathseeker.src.data_types.size import Size


class ISizeManager(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def name_to_size(name: str) -> Size:
        pass

    @staticmethod
    @abstractmethod
    def short_name_to_size(short_name: str) -> Size:
        pass
