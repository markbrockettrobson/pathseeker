import typing

from pathseeker.interface.data_types.i_modifier import IModifier
from pathseeker.interface.data_types.i_modifiable_variable import IModifiableVariable
from pathseeker.interface.common.i_data_type import IDataType
from pathseeker.src.common.data_type_base import DataTypeBase

GenericType = typing.TypeVar("GenericType")


class ModifiableVariable(IModifiableVariable, typing.Generic[GenericType], IDataType, DataTypeBase):
    def __init__(self):
        raise NotImplemented()

    def get_modified_value(self) -> GenericType:
        raise NotImplemented()

    def add_modifier(self, modifier: IModifier[GenericType]) -> None:
        raise NotImplemented()

    def get_modifier_list(self) -> typing.List[IModifier[GenericType]]:
        raise NotImplemented()
