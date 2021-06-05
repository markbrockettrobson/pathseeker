from abc import ABCMeta, abstractmethod

from pathseeker.src.data_types.modifier_type import ModifierType


class IIntModifier(metaclass=ABCMeta):
    @abstractmethod
    def modify_value(self, value: int) -> int:
        pass

    @property
    @abstractmethod
    def type(self) -> ModifierType:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def source(self) -> str:
        pass

