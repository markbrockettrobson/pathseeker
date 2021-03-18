import abc
import typing
import hypothesis.strategies as strategies


class IDataType(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def build_from_json_dict(cls, json_dict: typing.Dict):
        pass

    @abc.abstractmethod
    def to_property_dict(self) -> typing.Dict:
        pass

    @abc.abstractmethod
    def to_json_dict(self) -> typing.Dict:
        pass

    @abc.abstractmethod
    def to_json_string(self) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def validate_json(json_dictionary: typing.Dict[str, typing.Any]) -> bool:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass

    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        pass

    @abc.abstractmethod
    def __hash__(self) -> int:
        pass

    @abc.abstractmethod
    def __copy__(self):
        pass

    @abc.abstractmethod
    def __deepcopy__(self):
        pass

    @staticmethod
    @strategies.composite
    @abc.abstractmethod
    def strategy(draw, **keyword_arguments):
        pass
