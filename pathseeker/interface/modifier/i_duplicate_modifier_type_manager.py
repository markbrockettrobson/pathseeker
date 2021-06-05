from abc import ABCMeta, abstractmethod

from typing import Collection


class IDuplicateModifierTypeManager(metaclass=ABCMeta):
    @abstractmethod
    def get_simple_string(self) -> str:
        pass

    @abstractmethod
    def get_detailed_string(self) -> str:
        pass

    @abstractmethod
    def get_brake_down(self, modifiers: Collection[IModifier]) -> "IModifiableBrakeDown":
        pass
