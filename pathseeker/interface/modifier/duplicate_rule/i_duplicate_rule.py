from abc import ABCMeta, abstractmethod

from typing import Collection

from pathseeker.interface.modifier.i_modifier import IModifier


class IDuplicateRule(metaclass=ABCMeta):
    @abstractmethod
    def get_simple_string(self) -> str:
        pass

    @abstractmethod
    def get_detailed_string(self) -> str:
        pass

    @abstractmethod
    def get_brake_down(self, modifiers: Collection[IModifier]) -> "IModifiableBrakeDown":
        pass
