import abc

from pathseeker.interface.data_types.i_size import ISize


class ISizeManager(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def name_to_size(name: str) -> ISize:
        pass

    @staticmethod
    @abc.abstractmethod
    def short_name_to_size(short_name: str) -> ISize:
        pass
