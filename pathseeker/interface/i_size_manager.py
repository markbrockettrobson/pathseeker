import abc

import pathseeker.interface.i_size as i_size


class ISizeManager(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def name_to_size(name: str) -> i_size.ISize:
        pass

    @staticmethod
    @abc.abstractmethod
    def short_name_to_size(short_name: str) -> i_size.ISize:
        pass
