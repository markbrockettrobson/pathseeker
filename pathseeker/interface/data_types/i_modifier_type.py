import abc

from pathseeker.interface.common.i_data_type import IDataType


class IModifierType(IDataType, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def short_name(self) -> str:
        pass
