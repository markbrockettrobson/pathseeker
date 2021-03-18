import abc
import typing

from pathseeker.interface.data_types.i_modifier_type import IModifierType
from pathseeker.interface.common.i_data_type import IDataType

GenericType = typing.TypeVar("GenericType")


class IModifier(typing.Generic[GenericType], IDataType, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def modifier_value(self) -> GenericType:
        pass

    @property
    @abc.abstractmethod
    def type(self) -> IModifierType:
        pass
