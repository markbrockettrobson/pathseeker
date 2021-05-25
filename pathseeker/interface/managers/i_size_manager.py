import abc

from pathseeker.src.data_types.size import Size


class ISizeManager(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def name_to_size(name: str) -> Size:
        pass

    @staticmethod
    @abc.abstractmethod
    def short_name_to_size(short_name: str) -> Size:
        pass
