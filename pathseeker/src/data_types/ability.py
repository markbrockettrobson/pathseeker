import cerberus.validator as validator
import json
import string
import typing
import hypothesis.strategies as strategies

from pathseeker.interface.data_types.i_ability import IAbility
from pathseeker.src.common.data_type_base import DataTypeBase
from pathseeker.src.common.to_string_formatter import ToStringFormatter


class Ability(IAbility, DataTypeBase):
    __SCHEMA = {"Ability": {"type": "dict", "schema": {"name": {"type": "string"}, "short name": {"type": "string"}}}}
    __VALIDATOR = validator.Validator(schema=__SCHEMA, allow_unknown=False, require_al=True)

    def __init__(self, name: str, short_name: str):
        self.__name = name
        self.__short_name = short_name

    @classmethod
    def build_from_json_dict(cls, json_dict: typing.Dict):
        pass

    @property
    def name(self) -> str:
        return self.__name

    @property
    def short_name(self) -> str:
        return self.__short_name

    def __str__(self) -> str:
        return ToStringFormatter.to_string(class_name=Ability.__name__, name=self.__name, short_name=self.__short_name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, type(self)):
            return self.name == other.name and self.short_name == other.short_name
        return False

    def __hash__(self):
        return hash((self.__name, self.__short_name))

    def __copy__(self):
        return Ability(name=self.__name, short_name=self.__short_name)

    def __deepcopy__(self):
        return self.__copy__()

    @staticmethod
    @strategies.composite
    def strategy(
        draw,
        alphabet: str = string.ascii_letters,
        min_name_length: int = 1,
        max_name_length: int = 10,
        min_short_name_length: int = 1,
        max_short_name_length: int = 10,
    ):
        name = draw(strategies.text(alphabet=alphabet, min_size=min_name_length, max_size=max_name_length))
        short_name = draw(
            strategies.text(alphabet=alphabet, min_size=min_short_name_length, max_size=max_short_name_length)
        )
        return Ability(name=name, short_name=short_name)

    def to_property_dict(self) -> typing.Dict:
        return {"name": self.__name, "short name": self.__short_name}

    def to_json_dict(self) -> typing.Dict:
        return {self.__name__: {"name": self.__name, "short name": self.__short_name}}

    def to_json_string(self) -> str:
        return json.dumps(self.to_json_dict())

    @staticmethod
    def validate_json(json_dictionary: typing.Dict[str, typing.Any]) -> bool:
        return Ability.__VALIDATOR.validated(json_dictionary)
