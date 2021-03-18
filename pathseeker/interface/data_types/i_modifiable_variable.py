import abc
import typing

from pathseeker.interface.data_types.i_modifier import IModifier
from pathseeker.interface.common.i_data_type import IDataType

GenericType = typing.TypeVar("GenericType")


class IModifiableVariable(typing.Generic[GenericType], IDataType, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_modified_value(self) -> GenericType:
        pass

    @abc.abstractmethod
    def add_modifier(self, modifier: IModifier[GenericType]) -> None:
        pass

    @abc.abstractmethod
    def get_modifier_list(self) -> typing.List[IModifier[GenericType]]:
        pass
