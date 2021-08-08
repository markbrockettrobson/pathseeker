from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from pathseeker.interface.modifier.i_modifiable_brakedown import IModifiableBrakedown

ModifierValueType = TypeVar("ModifierValueType")


class IModifiableValue(Generic[ModifierValueType], metaclass=ABCMeta):
    @abstractmethod
    def get_value(self) -> ModifierValueType:
        pass

    @abstractmethod
    def get_brake_down(self) -> IModifiableBrakedown[ModifierValueType]:
        pass
