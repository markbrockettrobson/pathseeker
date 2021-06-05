from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic

from pathseeker.src.data_types.modifier_type import ModifierType

T = TypeVar('T')


class IModifier(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def modify_value(self, value: T) -> T:
        pass

    @property
    @abstractmethod
    def type(self) -> ModifierType:
        pass

