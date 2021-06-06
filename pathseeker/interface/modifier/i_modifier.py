from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from pathseeker.src.data_types.modifier_type import ModifierType

ModifierValueType = TypeVar("ModifierValueType")


class IModifier(Generic[ModifierValueType], metaclass=ABCMeta):
    @abstractmethod
    def modify_value(self, value: ModifierValueType) -> ModifierValueType:
        pass

    @property
    @abstractmethod
    def type(self) -> ModifierType:
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
    def source(self) -> str:
        pass
