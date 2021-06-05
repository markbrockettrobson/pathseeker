from abc import ABCMeta, abstractmethod


class IModifiableBrakeDown(metaclass=ABCMeta):
    @abstractmethod
    def get_simple_string(self) -> str:
        pass

    @abstractmethod
    def get_detailed_string(self) -> str:
        pass

    @abstractmethod
    def get_subsection(self, name: str) -> "IModifiableBrakeDown":
        pass
