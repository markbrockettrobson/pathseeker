import typing
import json

from pathseeker.interface.common.i_data_type import IDataType
from pathseeker.src.common.to_string_formatter import ToStringFormatter
import hypothesis.strategies as strategies


class DataTypeBase:
    TO_STRING_OBJECTS = {str, int, float}

    @staticmethod
    def _is_printable_type(value: object) -> bool:
        if type(value) in DataTypeBase.TO_STRING_OBJECTS:
            return True
        if hasattr(value, "name"):
            return True
        return False

    @staticmethod
    def _to_printable_string(value: object) -> str:
        if type(value) in DataTypeBase.TO_STRING_OBJECTS:
            return str(value)
        if hasattr(value, "name"):
            return value.name
        raise NotImplemented(f'Value of type {type(value)} has no attribute "name".')

    @classmethod
    def build_from_json_dict(cls, json_dict: typing.Dict):
        raise NotImplemented()

    def to_property_dict(self) -> typing.Dict:
        raise NotImplemented()

    def to_json_dict(self) -> typing.Dict:
        raise NotImplemented()

    def to_json_string(self) -> str:
        return json.dumps(self.to_json_dict())

    def __str__(self) -> str:
        return ToStringFormatter.to_string(
            class_name=self.__name__,
            **{
                key: self._to_printable_string(value)
                for key, value in self.to_json_dict().items()
                if self._is_printable_type(value)
            },
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, IDataType):
            return False
        if type(self) != type(other):
            return False
        return self.__hash__() == other.__hash__()

    def __hash__(self) -> int:
        for key, value in self.to_property_dict().items():
            if not hasattr(value, "__hash__"):
                raise NotImplemented(f"Object of type {type(value)} has no __hash__ method.")

        return hash(((key, value).__hash__() for key, value in self.to_property_dict().items()))

    def __copy__(self):
        raise NotImplemented()

    def __deepcopy__(self):
        raise NotImplemented()

    @staticmethod
    @strategies.composite
    def strategy(draw, **keyword_arguments):
        raise NotImplemented()

    @staticmethod
    def validate_json(json_dictionary: typing.Dict[str, typing.Any]) -> bool:
        raise NotImplemented()
