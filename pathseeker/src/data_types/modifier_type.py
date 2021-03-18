import typing

from pathseeker.interface.data_types.i_modifier_type import IModifierType
from pathseeker.src.common.data_type_base import DataTypeBase


class ModifierType(IModifierType, DataTypeBase):
    def __init__(self, name: str, short_name: str):
        self.__name = name
        self.__short_name = short_name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def short_name(self) -> str:
        return self.__short_name

    @classmethod
    def build_from_json_dict(cls, json_dict: typing.Dict):
        raise NotImplemented()

    def to_property_dict(self) -> typing.Dict:
        raise NotImplemented()

    def to_json_dict(self) -> typing.Dict:
        raise NotImplemented()

    def to_json_string(self) -> str:
        raise NotImplemented()

    @staticmethod
    def validate_json(json_dictionary: typing.Dict[str, typing.Any]) -> bool:
        raise NotImplemented()

    def __str__(self) -> str:
        raise NotImplemented()

    def __eq__(self, other: object) -> bool:
        raise NotImplemented()

    def __hash__(self) -> int:
        raise NotImplemented()

    def __copy__(self):
        raise NotImplemented()

    def __deepcopy__(self):
        raise NotImplemented()

    @staticmethod
    def strategy(draw, **keyword_arguments):
        raise NotImplemented()
