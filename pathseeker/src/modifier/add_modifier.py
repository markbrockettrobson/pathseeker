from typing import TypeVar

from pathseeker.interface.modifier.i_modifier import IModifier
from pathseeker.src.data_types.modifier_type import ModifierType

ModifierValueType = TypeVar("ModifierValueType")


class AddModifier(IModifier):
    def __init__(self, name: str, value: ModifierValueType, modifier_type: ModifierType, priority: int = 0):
        self.__name = name
        self.__value = value
        self.__modifier_type = modifier_type
        self.__priority = priority

    def modify_value(self, base_value: ModifierValueType) -> ModifierValueType:
        return base_value + self.__value

    @property
    def modifier_type(self) -> ModifierType:
        return self.__modifier_type

    @property
    def value(self) -> ModifierValueType:
        return self.__value

    @property
    def name(self) -> str:
        return self.__name

    @property
    def priority(self) -> int:
        return self.__priority
