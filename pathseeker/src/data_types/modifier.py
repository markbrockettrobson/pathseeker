import string
import typing

import hypothesis.strategies as strategies

from pathseeker.interface.data_types.i_modifier_type import IModifierType
from pathseeker.src.common.data_type_base import DataTypeBase

GenericType = typing.TypeVar("GenericType")


class Modifier(typing.Generic[GenericType], DataTypeBase):
    def __init__(self, name: str, modifier_value: GenericType, modifier_type: IModifierType):
        self.__name = name
        self.__modifier_value = modifier_value
        self.__modifier_type = modifier_type

    @property
    def name(self) -> str:
        return self.__name

    @property
    def modifier_value(self) -> GenericType:
        return self.__modifier_value

    @property
    def type(self) -> IModifierType:
        return self.__modifier_type


@strategies.composite
def modifier(
    draw,
    alphabet: str = string.ascii_letters,
    min_name_length: int = 1,
    max_name_length: int = 10,
    min_value: int = -5,
    max_value: int = 5,
):
    name = draw(strategies.text(alphabet=alphabet, min_size=min_name_length, max_size=max_name_length))
    modifier_type = draw(strategies.text(alphabet=alphabet, min_size=min_name_length, max_size=max_name_length))
    value = draw(strategies.integers(min_value=min_value, max_value=max_value))
    return Modifier(name=name, modifier_type=modifier_type, modifier_value=value)
