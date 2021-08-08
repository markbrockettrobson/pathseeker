from abc import ABCMeta, abstractmethod

from pathseeker.interface.modifier.i_modifiable_brake_down import IModifiableBrakeDown


class IModifiableInt(metaclass=ABCMeta):
    @abstractmethod
    def get_value(self) -> int:
        pass

    @abstractmethod
    def get_brake_down(self) -> IModifiableBrakeDown:
        pass
