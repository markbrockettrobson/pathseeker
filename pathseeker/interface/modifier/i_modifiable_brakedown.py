from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

ModifierValueType = TypeVar("ModifierValueType")


class IModifiableBrakedown(Generic[ModifierValueType], metaclass=ABCMeta):
    @abstractmethod
    def get_simple_string(self) -> str:
        pass

    @abstractmethod
    def get_detailed_string(self) -> str:
        pass

    @property
    @abstractmethod
    def value(self) -> ModifierValueType:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def priority(self) -> int:
        pass
