import abc

from pathseeker.interface.common.i_data_type import IDataType


class ISize(IDataType, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def short_name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def space(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def tall_reach(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def long_reach(self) -> int:
        pass
